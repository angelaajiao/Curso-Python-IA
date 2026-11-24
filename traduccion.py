"""Traducción automática de las recetas (que vienen en inglés) al español.

Usa el servicio gratuito de traducción de Google (el mismo que usa el
navegador), que responde en JSON y no necesita clave. Si no hay conexión o
falla, la receta se queda en inglés y la app sigue funcionando.

Para no hacer una petición por cada frase, las frases se juntan en bloques
separados por saltos de línea y se traducen de una vez.
"""

from collections.abc import Callable

import requests

import logica

URL_TRADUCTOR = "https://translate.googleapis.com/translate_a/single"
MAX_CARACTERES = 1800  # el texto va en la URL: bloques cortos para no pasarse
TIEMPO_MAXIMO = 10  # segundos
SEPARADOR = "\n"


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


def _traductor_google(destino: str) -> Callable[[str], str]:
    """Devuelve una función que traduce un texto del inglés a ``destino``."""

    def traducir(texto: str) -> str:
        parametros = {"client": "gtx", "sl": "en", "tl": destino, "dt": "t", "q": texto}
        respuesta = requests.get(URL_TRADUCTOR, params=parametros, timeout=TIEMPO_MAXIMO)
        respuesta.raise_for_status()
        return unir_segmentos(respuesta.json())

    return traducir


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


def traducir_lista(textos: list[str], destino: str = "es",
                   traducir_texto: Callable[[str], str] | None = None) -> tuple[list[str], bool]:
    """Traduce una lista de frases y devuelve ``(traducciones, todo_ok)``.

    Las frases vacías se quedan como están. Si algo falla, devuelve las
    frases originales y ``False``. ``traducir_texto`` permite cambiar el
    traductor, por ejemplo en los tests.

    >>> traducir_lista(["hello", "", "world"], traducir_texto=str.upper)
    (['HELLO', '', 'WORLD'], True)
    """
    posiciones = [posicion for posicion, frase in enumerate(textos) if frase.strip()]
    no_vacias = [textos[posicion] for posicion in posiciones]
    resultado = list(textos)
    if not no_vacias:
        return resultado, True

    if traducir_texto is None:
        traducir_texto = _traductor_google(destino)
    try:
        traducidas = []
        for bloque in logica.agrupar_en_bloques(no_vacias, MAX_CARACTERES):
            traducidas.extend(_traducir_bloque(bloque, traducir_texto))
    except Exception:  # sin conexión, respuesta rara, límite superado…
        return list(textos), False

    for posicion, frase in zip(posiciones, traducidas):
        resultado[posicion] = frase
    return resultado, True
