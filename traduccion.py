"""Traducción automática de las recetas (que vienen en inglés) al español.

Se usan dos servicios gratuitos que no necesitan clave, uno detrás de otro:

1. El traductor de Google (el mismo que usa el navegador).
2. MyMemory, como respaldo si Google falla o bloquea por demasiadas peticiones.

Además, cada frase traducida se guarda en una "memoria" (un diccionario que la
app guarda en traducciones.json). Lo que ya está en la memoria no se vuelve a
pedir a internet, así que una receta que se tradujo una vez sale en español
aunque los dos servicios fallen.

Si nada funciona, la receta se queda en inglés y la app sigue funcionando.
"""

import json
import os
from collections.abc import Callable
from pathlib import Path

import requests

import logica

URL_GOOGLE = "https://translate.googleapis.com/translate_a/single"
URL_MYMEMORY = "https://api.mymemory.translated.net/get"
MAX_CARACTERES_GOOGLE = 1800  # el texto va en la URL: bloques cortos
MAX_CARACTERES_MYMEMORY = 450  # MyMemory admite como mucho 500 por petición
TIEMPO_MAXIMO = 10  # segundos
SEPARADOR = "\n"
# Con un correo, MyMemory permite 50.000 caracteres al día en vez de 5.000.
# Se configura con la variable de entorno MYMEMORY_EMAIL (opcional).
CORREO_MYMEMORY = os.environ.get("MYMEMORY_EMAIL")


class TraductorNoDisponible(Exception):
    """El servicio de traducción ha respondido con un error o un aviso de límite."""


# ------------------------------------------------------------------ servicios
def unir_segmentos(respuesta_json: list) -> str:
    """Junta el texto traducido de la respuesta de Google.

    La respuesta es una lista cuyo primer elemento es una lista de segmentos
    ``[traducción, original, ...]``.

    >>> unir_segmentos([[["Hola\\n", "Hello\\n"], ["mundo", "world"]], None, "en"])
    'Hola\\nmundo'
    """
    segmentos = respuesta_json[0] if respuesta_json else None
    if not segmentos:
        return ""
    return "".join(segmento[0] for segmento in segmentos if segmento and segmento[0])


def texto_de_mymemory(respuesta_json: dict) -> str:
    """Saca la traducción de la respuesta de MyMemory, o lanza un error.

    MyMemory avisa de que se ha pasado el límite diario con un texto que
    empieza por "MYMEMORY WARNING" o con un ``responseStatus`` distinto de 200.

    >>> texto_de_mymemory({"responseStatus": 200, "responseData": {"translatedText": "Hola"}})
    'Hola'
    """
    traduccion = (respuesta_json.get("responseData") or {}).get("translatedText") or ""
    estado = str(respuesta_json.get("responseStatus"))
    if estado != "200" or traduccion.upper().startswith("MYMEMORY WARNING"):
        raise TraductorNoDisponible(traduccion or f"MyMemory respondió {estado}")
    return traduccion


def _traductor_google(destino: str) -> Callable[[str], str]:
    def traducir(texto: str) -> str:
        parametros = {"client": "gtx", "sl": "en", "tl": destino, "dt": "t", "q": texto}
        respuesta = requests.get(URL_GOOGLE, params=parametros, timeout=TIEMPO_MAXIMO)
        respuesta.raise_for_status()
        return unir_segmentos(respuesta.json())

    return traducir


def _traductor_mymemory(destino: str) -> Callable[[str], str]:
    def traducir(texto: str) -> str:
        parametros = {"q": texto, "langpair": f"en|{destino}"}
        if CORREO_MYMEMORY:
            parametros["de"] = CORREO_MYMEMORY
        respuesta = requests.get(URL_MYMEMORY, params=parametros, timeout=TIEMPO_MAXIMO)
        respuesta.raise_for_status()
        return texto_de_mymemory(respuesta.json())

    return traducir


def _servicios(destino: str) -> list[tuple[Callable[[str], str], int]]:
    """Los traductores que se prueban, en orden, con su tamaño máximo de bloque."""
    return [
        (_traductor_google(destino), MAX_CARACTERES_GOOGLE),
        (_traductor_mymemory(destino), MAX_CARACTERES_MYMEMORY),
    ]


# -------------------------------------------------------------------- traducir
def _traducir_bloque(bloque: list[str], traducir_texto: Callable[[str], str]) -> list[str]:
    """Traduce un bloque de frases en una sola petición.

    Si el traductor no respeta los saltos de línea y no salen las mismas
    frases que entraron, se traducen una a una.
    """
    traducido = traducir_texto(SEPARADOR.join(bloque)) or ""
    partes = traducido.split(SEPARADOR)
    if len(partes) == len(bloque):
        return [parte.strip() for parte in partes]
    return [(traducir_texto(frase) or frase).strip() for frase in bloque]


def _traducir_con(frases: list[str], traducir_texto: Callable[[str], str],
                  max_caracteres: int) -> list[str]:
    """Traduce todas las frases con un servicio. Si falla, lanza la excepción."""
    traducidas = []
    for bloque in logica.agrupar_en_bloques(frases, max_caracteres):
        traducidas.extend(_traducir_bloque(bloque, traducir_texto))
    return traducidas


def traducir_lista(textos: list[str], destino: str = "es",
                   traducir_texto: Callable[[str], str] | None = None,
                   memoria: dict[str, str] | None = None) -> tuple[list[str], bool]:
    """Traduce una lista de frases y devuelve ``(traducciones, todo_ok)``.

    - Las frases vacías se quedan como están.
    - Las que ya están en ``memoria`` no se piden a internet, y las nuevas que
      se traducen bien se añaden a ``memoria``.
    - Se prueba cada servicio en orden; si todos fallan, las frases que no
      estaban en la memoria se quedan en inglés y se devuelve ``False``.

    ``traducir_texto`` permite usar un traductor concreto, por ejemplo en los
    tests.

    >>> traducir_lista(["hello", "", "world"], traducir_texto=str.upper)
    (['HELLO', '', 'WORLD'], True)
    """
    if memoria is None:
        memoria = {}
    pendientes = list(dict.fromkeys(
        frase for frase in textos if frase.strip() and frase not in memoria
    ))

    ok = True
    if pendientes:
        if traducir_texto is not None:
            servicios = [(traducir_texto, MAX_CARACTERES_GOOGLE)]
        else:
            servicios = _servicios(destino)
        ok = False
        for servicio, max_caracteres in servicios:
            try:
                traducidas = _traducir_con(pendientes, servicio, max_caracteres)
            except Exception:  # sin conexión, límite superado, respuesta rara…
                continue
            memoria.update(
                (original, traducida) for original, traducida in zip(pendientes, traducidas) if traducida
            )
            ok = True
            break

    return [memoria.get(frase) or frase if frase.strip() else frase for frase in textos], ok


# --------------------------------------------------------- memoria en un fichero
def cargar_memoria(ruta: Path) -> dict[str, dict[str, str]]:
    """Lee las traducciones guardadas: {idioma: {frase en inglés: traducción}}.

    Si el fichero no existe o está estropeado, empieza vacía.
    """
    try:
        datos = json.loads(Path(ruta).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    if not isinstance(datos, dict):
        return {}
    return {idioma: frases for idioma, frases in datos.items() if isinstance(frases, dict)}


def guardar_memoria(ruta: Path, memoria: dict[str, dict[str, str]]) -> None:
    """Escribe las traducciones en el fichero."""
    Path(ruta).write_text(json.dumps(memoria, ensure_ascii=False, indent=1), encoding="utf-8")
