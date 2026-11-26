"""¿Qué puedo cocinar? Página web hecha con Streamlit.

Ejecutar con:  streamlit run app.py

Este fichero solo muestra cosas y recoge lo que hace el usuario. La lógica
está en logica.py, las llamadas a internet en api.py, la traducción en
traduccion.py y los textos de la interfaz en textos.py.
"""

import html
import urllib.parse
from pathlib import Path

import requests
import streamlit as st

import api
import favoritos
import logica
import textos
import traduccion

POR_PAGINA = 12
COLUMNAS = 3
URL_BUSQUEDA_YOUTUBE = "https://www.youtube.com/results?search_query="
FICHERO_FAVORITAS = Path(__file__).with_name("favoritos.json")

st.set_page_config(page_title="¿Qué puedo cocinar?", page_icon="🍳", layout="wide")

ESTILOS = """
<style>
/* Fuente de emojis de Google: en Windows hace que se vean las banderas. */
@import url('https://fonts.googleapis.com/css2?family=Noto+Color+Emoji&display=swap');

.st-key-idioma, .st-key-idioma * {
    font-family: "Source Sans 3", "Source Sans Pro", "Noto Color Emoji", sans-serif !important;
}

/* Cabecera */
.cabecera {
    background: linear-gradient(135deg, #ff7a45 0%, #ffb347 100%);
    border-radius: 24px;
    padding: 2.2rem 2.4rem;
    color: white;
    box-shadow: 0 12px 30px rgba(255, 122, 69, 0.25);
    margin-bottom: 0.5rem;
}
.cabecera h1 {
    color: white;
    margin: 0;
    padding: 0;
    font-size: 2.6rem;
    font-weight: 800;
}
.cabecera p {
    margin: 0.5rem 0 0;
    font-size: 1.15rem;
    opacity: 0.95;
}

/* Tarjetas de resultados */
[class*="st-key-tarjeta_"] {
    border-radius: 20px !important;
    background: white;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}
[class*="st-key-tarjeta_"]:hover {
    transform: translateY(-4px);
    box-shadow: 0 14px 28px rgba(0, 0, 0, 0.12);
}
[class*="st-key-tarjeta_"] img {
    height: 210px;
    object-fit: cover;
    border-radius: 14px;
}
[class*="st-key-tarjeta_"] h4 {
    min-height: 3.2rem;
    padding-bottom: 0;
}

/* Detalle de la receta */
.st-key-foto_receta img {
    border-radius: 24px;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
}
.paso {
    display: flex;
    gap: 1rem;
    align-items: flex-start;
    background: #fff1e6;
    border-radius: 16px;
    padding: 0.9rem 1.1rem;
    margin-bottom: 0.7rem;
    line-height: 1.55;
}
.paso .numero {
    flex: 0 0 2.1rem;
    height: 2.1rem;
    border-radius: 50%;
    background: #ff7a45;
    color: white;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
}
.pie {
    text-align: center;
    color: #9a8f86;
    font-size: 0.85rem;
    margin-top: 3rem;
}
</style>
"""


# ------------------------------------------------------------ datos con caché
# st.cache_data guarda los resultados: si se repite la misma petición no se
# vuelve a pedir a internet ni a traducir.
@st.cache_data(show_spinner=False)
def buscar_cacheado(ingrediente: str) -> list[dict]:
    return api.buscar_por_ingrediente(ingrediente)


@st.cache_data(show_spinner=False)
def categoria_cacheada(nombre_categoria: str) -> list[dict]:
    return api.buscar_por_categoria(nombre_categoria)


@st.cache_data(show_spinner=False)
def receta_cacheada(id_receta: str) -> dict | None:
    return api.obtener_receta(id_receta)


class TraduccionFallida(Exception):
    """La traducción no ha funcionado (sin conexión, límite superado…)."""


@st.cache_data(show_spinner=False)
def _traduccion_guardada(frases: tuple[str, ...], idioma: str) -> list[str]:
    # Si falla se lanza una excepción: st.cache_data no guarda los errores,
    # así que la próxima vez se vuelve a intentar en vez de quedarse en inglés.
    traducidas, ok = traduccion.traducir_lista(list(frases), destino=idioma)
    if not ok:
        raise TraduccionFallida
    return traducidas


def traducir_cacheado(frases: tuple[str, ...], idioma: str) -> tuple[list[str], bool]:
    """Traduce al idioma de la interfaz. En inglés no hay nada que traducir."""
    if idioma == "en":
        return list(frases), True
    try:
        return _traduccion_guardada(frases, idioma), True
    except TraduccionFallida:
        return list(frases), False


# ----------------------------------------------------------------- acciones
def buscar(texto: str) -> None:
    """Busca recetas para los ingredientes escritos y guarda el resultado."""
    ingredientes = logica.limpiar_ingredientes(texto)
    resultados = {}
    for ingrediente in ingredientes:
        nombre_categoria = logica.categoria(ingrediente)
        if nombre_categoria:
            resultados[ingrediente] = categoria_cacheada(nombre_categoria)
        else:
            resultados[ingrediente] = buscar_cacheado(logica.traducir(ingrediente))
    st.session_state.ingredientes_buscados = ingredientes
    st.session_state.mis_ingredientes = logica.palabras_para_comparar(ingredientes)
    st.session_state.recetas = logica.combinar_resultados(resultados)
    st.session_state.mostradas = POR_PAGINA
    st.session_state.receta_elegida = None


def ver_mas(clave_pagina: str) -> None:
    st.session_state[clave_pagina] = st.session_state.get(clave_pagina, POR_PAGINA) + POR_PAGINA


def elegir_receta(id_receta: str) -> None:
    st.session_state.receta_elegida = id_receta


def volver() -> None:
    st.session_state.receta_elegida = None


def alternar_favorita(receta: dict, mensaje_guardada: str, mensaje_quitada: str) -> None:
    """Guarda la receta en favoritas o la quita, y lo apunta en el fichero."""
    ya_estaba = favoritos.es_favorita(st.session_state.favoritas, receta["id"])
    st.session_state.favoritas = favoritos.alternar(st.session_state.favoritas, receta)
    favoritos.guardar(FICHERO_FAVORITAS, st.session_state.favoritas)
    if ya_estaba:
        st.toast(mensaje_quitada, icon=":material/heart_broken:")
    else:
        st.toast(mensaje_guardada, icon=":material/favorite:")


def marcar_todas(claves: list[str], valor: bool) -> None:
    """Marca o desmarca de golpe todas las casillas de ingredientes."""
    for clave in claves:
        st.session_state[clave] = valor


# ------------------------------------------------------------------ dibujar
def mostrar_cabecera(t) -> None:
    st.html(
        f'<div class="cabecera"><h1>🍳 {html.escape(t("titulo"))}</h1>'
        f'<p>{html.escape(t("subtitulo"))}</p></div>'
    )


def mostrar_tarjetas(recetas: list[dict], idioma: str, t, *,
                     clave_pagina: str = "mostradas", con_coincidencias: bool = True) -> None:
    """Muestra recetas en una cuadrícula de tarjetas con foto.

    Se enseñan de POR_PAGINA en POR_PAGINA, con un botón para ver más. Sirve
    para los resultados de la búsqueda y para las favoritas.
    """
    mostradas = st.session_state.get(clave_pagina, POR_PAGINA)
    visibles = recetas[:mostradas]
    nombres, _ = traducir_cacheado(tuple(receta["nombre"] for receta in visibles), idioma)
    total_buscados = len(st.session_state.get("ingredientes_buscados", []))

    columnas = st.columns(COLUMNAS, gap="medium")
    for posicion, (receta, nombre) in enumerate(zip(visibles, nombres)):
        with columnas[posicion % COLUMNAS]:
            with st.container(border=True, key=f"tarjeta_{clave_pagina}_{receta['id']}"):
                st.image(receta["foto"], width="stretch")
                st.markdown(f"#### {nombre}")
                if con_coincidencias:
                    st.badge(
                        t("coincidencias", n=len(receta["coincidencias"]), total=total_buscados),
                        icon=":material/check_circle:",
                        color="green",
                    )
                    st.caption(t("usa", lista=", ".join(receta["coincidencias"])))
                guardada = favoritos.es_favorita(st.session_state.favoritas, receta["id"])
                with st.container(horizontal=True):
                    st.button(
                        t("ver_receta"),
                        key=f"ver_{clave_pagina}_{receta['id']}",
                        on_click=elegir_receta,
                        args=(receta["id"],),
                        type="primary",
                        icon=":material/restaurant_menu:",
                        width="stretch",
                    )
                    st.button(
                        "❤️" if guardada else "🤍",
                        key=f"fav_{clave_pagina}_{receta['id']}",
                        help=t("quitar_favorita") if guardada else t("guardar_favorita"),
                        on_click=alternar_favorita,
                        args=(
                            {"id": receta["id"], "nombre": receta["nombre"], "foto": receta["foto"]},
                            t("aviso_guardada"),
                            t("aviso_quitada"),
                        ),
                    )

    st.caption(t("mostrando", n=len(visibles), total=len(recetas)))
    siguientes = logica.cuantas_mas(len(visibles), len(recetas), POR_PAGINA)
    if siguientes:
        st.button(t("ver_mas", n=siguientes), on_click=ver_mas, args=(clave_pagina,),
                  key=f"ver_mas_{clave_pagina}", icon=":material/expand_more:", width="stretch")


def traducir_receta(receta: dict, ingredientes: list[tuple[str, str]],
                    pasos: list[str], idioma: str) -> tuple[str, list[str], list[str], list[str], bool]:
    """Traduce de una vez el título, los ingredientes, las cantidades y los pasos.

    Los ingredientes que están en el diccionario de textos.py usan esa
    traducción; solo los demás se mandan al traductor automático.
    """
    nombres = [nombre for nombre, _ in ingredientes]
    cantidades = [cantidad for _, cantidad in ingredientes]
    conocidos = [textos.ingrediente_conocido(nombre, idioma) for nombre in nombres]
    pendientes = [nombre for nombre, conocido in zip(nombres, conocidos) if conocido is None]

    frases = [receta["strMeal"], *pendientes, *cantidades, *pasos]
    traducidas, ok = traducir_cacheado(tuple(frases), idioma)

    n_pendientes = len(pendientes)
    n_cantidades = len(cantidades)
    titulo = traducidas[0]
    nombres_traducidos = traducidas[1:1 + n_pendientes]
    cantidades_vistas = traducidas[1 + n_pendientes:1 + n_pendientes + n_cantidades]
    pasos_vistos = traducidas[1 + n_pendientes + n_cantidades:]
    nombres_vistos = logica.rellenar_huecos(conocidos, nombres_traducidos)
    return titulo, nombres_vistos, cantidades_vistas, pasos_vistos, ok


def mostrar_pasos(pasos: list[str], t) -> None:
    if not pasos:
        st.info(t("sin_pasos"))
        return
    bloques = "".join(
        f'<div class="paso"><div class="numero">{numero}</div><div>{html.escape(paso)}</div></div>'
        for numero, paso in enumerate(pasos, start=1)
    )
    st.html(bloques)


def mostrar_video(receta: dict, titulo: str, t) -> None:
    """Vídeo de la receta si lo tiene; si no, un botón para buscarlo en YouTube."""
    if receta.get("strYoutube"):
        st.video(receta["strYoutube"])
    else:
        st.info(t("sin_video"), icon=":material/movie:")

    busqueda = t("busqueda_video", receta=titulo)
    with st.container(horizontal=True):
        st.link_button(
            t("buscar_video"),
            URL_BUSQUEDA_YOUTUBE + urllib.parse.quote_plus(busqueda),
            icon=":material/smart_display:",
            type="primary",
        )
        if receta.get("strSource"):
            st.link_button(t("receta_original"), receta["strSource"], icon=":material/open_in_new:")


def mostrar_detalle(receta: dict, idioma: str, t) -> None:
    """Muestra una receta completa: foto, ingredientes, pasos y vídeo."""
    st.button(t("volver"), on_click=volver, icon=":material/arrow_back:", type="tertiary")

    ingredientes = logica.extraer_ingredientes(receta)
    pasos = logica.dividir_instrucciones(receta.get("strInstructions"))
    with st.spinner(t("traduciendo")):
        titulo, nombres_vistos, cantidades_vistas, pasos_vistos, ok = traducir_receta(
            receta, ingredientes, pasos, idioma
        )

    foto, datos = st.columns([2, 3], gap="large")
    with foto:
        with st.container(key="foto_receta"):
            st.image(receta["strMealThumb"], width="stretch")
    with datos:
        st.title(titulo)
        with st.container(horizontal=True):
            if receta.get("strCategory"):
                st.badge(textos.nombre_categoria(receta["strCategory"], idioma),
                         icon=":material/restaurant:", color="orange")
            if receta.get("strArea"):
                st.badge(textos.nombre_cocina(receta["strArea"], idioma),
                         icon=":material/public:", color="blue")
            st.badge(t("n_ingredientes", n=len(ingredientes)),
                     icon=":material/grocery:", color="violet")
        guardada = favoritos.es_favorita(st.session_state.favoritas, receta["idMeal"])
        st.button(
            t("quitar_favorita") if guardada else t("guardar_favorita"),
            on_click=alternar_favorita,
            args=(favoritos.resumen(receta), t("aviso_guardada"), t("aviso_quitada")),
            icon=":material/heart_broken:" if guardada else ":material/favorite:",
            type="secondary" if guardada else "primary",
        )
        # El resumen depende de las casillas, que se dibujan más abajo: se
        # reserva el sitio aquí y se rellena después.
        resumen = st.container()
        if not ok:
            st.warning(t("sin_traduccion"), icon=":material/translate:")

    pestana_ingredientes, pestana_preparacion, pestana_video = st.tabs([
        f":material/grocery: {t('pestana_ingredientes')}",
        f":material/menu_book: {t('pestana_preparacion')}",
        f":material/smart_display: {t('pestana_video')}",
    ])

    with pestana_ingredientes:
        mis_ingredientes = st.session_state.get("mis_ingredientes", [])
        claves = [f"tengo_{receta['idMeal']}_{numero}" for numero in range(len(ingredientes))]
        # Valor inicial de cada casilla: marcado si lo escribiste o es básico.
        for clave, (nombre, _) in zip(claves, ingredientes):
            if clave not in st.session_state:
                st.session_state[clave] = logica.lo_tengo(nombre, mis_ingredientes)

        with st.container(horizontal=True):
            st.button(t("marcar_todo"), on_click=marcar_todas, args=(claves, True),
                      icon=":material/done_all:")
            st.button(t("desmarcar_todo"), on_click=marcar_todas, args=(claves, False),
                      icon=":material/remove_done:")
        st.caption(t("marca_lo_que_tienes"))

        marcas = {}
        nombre_visible = {}
        columna_izquierda, columna_derecha = st.columns(2)
        datos_casillas = zip(claves, ingredientes, nombres_vistos, cantidades_vistas)
        for posicion, (clave, (nombre, _), nombre_visto, cantidad_vista) in enumerate(datos_casillas):
            nombre_visible[nombre] = nombre_visto
            etiqueta = f"**{nombre_visto}**" + (f" · {cantidad_vista}" if cantidad_vista else "")
            columna = columna_izquierda if posicion % 2 == 0 else columna_derecha
            marcas[nombre] = columna.checkbox(etiqueta, key=clave)

    with pestana_preparacion:
        mostrar_pasos(pasos_vistos, t)

    with pestana_video:
        mostrar_video(receta, titulo, t)

    with resumen:
        faltan = logica.lo_que_falta(marcas)
        total = len(marcas)
        tengo = total - len(faltan)
        st.progress(tengo / total if total else 0.0, text=t("tienes", tengo=tengo, total=total))
        if faltan:
            lista = ", ".join(nombre_visible[nombre] for nombre in faltan)
            st.warning(t("te_falta", lista=lista), icon=":material/shopping_cart:")
        else:
            st.success(t("tienes_todo"), icon=":material/celebration:")


# ------------------------------------------------------------------- página
st.html(ESTILOS)

if "favoritas" not in st.session_state:
    st.session_state.favoritas = favoritos.cargar(FICHERO_FAVORITAS)

columna_seccion, columna_idioma = st.columns([3, 1])
with columna_idioma:
    idioma = st.segmented_control(
        "Idioma",
        options=list(textos.IDIOMAS),
        format_func=textos.IDIOMAS.get,
        default=textos.IDIOMA_POR_DEFECTO,
        required=True,
        key="idioma",
        label_visibility="collapsed",
    )


def t(clave: str, **datos) -> str:
    """Atajo para pedir un texto de la interfaz en el idioma elegido."""
    return textos.texto(clave, idioma, **datos)


with columna_seccion:
    seccion = st.segmented_control(
        "Sección",
        options=["buscar", "favoritas"],
        format_func=lambda opcion: (
            t("seccion_buscar") if opcion == "buscar"
            else t("seccion_favoritas", n=len(st.session_state.favoritas))
        ),
        default="buscar",
        required=True,
        key="seccion",
        on_change=volver,
        label_visibility="collapsed",
    )

mostrar_cabecera(t)


def seccion_buscar() -> None:
    with st.form("busqueda", border=False):
        texto = st.text_input(t("campo_ingredientes"), placeholder=t("placeholder"))
        with st.container(horizontal=True):
            pulsado_buscar = st.form_submit_button(t("buscar"), type="primary", icon=":material/search:")
            pulsado_azar = st.form_submit_button(t("sorprendeme"), icon=":material/casino:")

    if pulsado_buscar:
        if logica.limpiar_ingredientes(texto):
            with st.spinner(t("buscando")):
                buscar(texto)
        else:
            st.warning(t("escribe_algo"))
    if pulsado_azar:
        aleatoria = api.receta_aleatoria()
        if aleatoria:
            st.session_state.mis_ingredientes = []
            st.session_state.receta_elegida = aleatoria["idMeal"]

    if st.session_state.get("receta_elegida"):
        mostrar_receta_elegida()
        return
    recetas = st.session_state.get("recetas")
    if recetas is None:
        return
    if recetas:
        st.subheader(t("encontradas", n=len(recetas)))
        st.caption(t("encontradas_detalle"))
        mostrar_tarjetas(recetas, idioma, t)
    else:
        st.info(t("sin_resultados"))


def seccion_favoritas() -> None:
    if st.session_state.get("receta_elegida"):
        mostrar_receta_elegida()
        return
    st.subheader(t("titulo_favoritas"))
    favoritas = st.session_state.favoritas
    if not favoritas:
        st.info(t("sin_favoritas"), icon=":material/favorite:")
        return
    mostrar_tarjetas(favoritas, idioma, t, clave_pagina="mostradas_favoritas", con_coincidencias=False)


def mostrar_receta_elegida() -> None:
    receta = receta_cacheada(st.session_state.receta_elegida)
    if receta:
        mostrar_detalle(receta, idioma, t)
    else:
        st.error(t("no_encontrada"))


try:
    if seccion == "favoritas":
        seccion_favoritas()
    else:
        seccion_buscar()
except requests.RequestException:
    st.error(t("sin_conexion"))

st.html(f'<div class="pie">{html.escape(t("pie"))}</div>')
