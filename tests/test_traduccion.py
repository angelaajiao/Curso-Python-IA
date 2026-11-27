"""Tests de traduccion.py con traductores falsos: no hace falta internet."""

import pytest

import traduccion


def test_traduce_y_respeta_vacios():
    traducidas, ok = traduccion.traducir_lista(["chicken", "", "rice"], traducir_texto=str.upper)
    assert (traducidas, ok) == (["CHICKEN", "", "RICE"], True)


def test_lista_vacia():
    assert traduccion.traducir_lista([], traducir_texto=str.upper) == ([], True)


def test_si_se_pierden_los_saltos_de_linea_traduce_una_a_una():
    def traductor_que_junta_lineas(texto):
        return texto.replace("\n", " ").upper()

    traducidas, ok = traduccion.traducir_lista(["one", "two"], traducir_texto=traductor_que_junta_lineas)
    assert (traducidas, ok) == (["ONE", "TWO"], True)


def test_si_falla_devuelve_el_original():
    def traductor_roto(texto):
        raise ConnectionError("sin conexión")

    assert traduccion.traducir_lista(["chicken"], traducir_texto=traductor_roto) == (["chicken"], False)


def test_agrupa_en_pocas_peticiones():
    llamadas = []

    def traductor_contador(texto):
        llamadas.append(texto)
        return texto

    frases = [f"step {numero}" for numero in range(50)]
    traducidas, ok = traduccion.traducir_lista(frases, traducir_texto=traductor_contador)
    assert traducidas == frases and ok
    assert len(llamadas) == 1


def test_unir_segmentos():
    respuesta = [[["Calienta el aceite.\n", "Heat the oil.\n"], ["Sirve.", "Serve."]], None, "en"]
    assert traduccion.unir_segmentos(respuesta) == "Calienta el aceite.\nSirve."


def test_unir_segmentos_respuesta_vacia():
    assert traduccion.unir_segmentos([]) == ""
    assert traduccion.unir_segmentos([None]) == ""


# ------------------------------------------------------------ memoria y respaldo
def test_lo_que_esta_en_la_memoria_no_se_pide():
    llamadas = []

    def traductor(texto):
        llamadas.append(texto)
        return texto.upper()

    memoria = {"chicken": "pollo"}
    traducidas, ok = traduccion.traducir_lista(["chicken", "rice"], traducir_texto=traductor, memoria=memoria)
    assert (traducidas, ok) == (["pollo", "RICE"], True)
    assert llamadas == ["rice"]
    assert memoria == {"chicken": "pollo", "rice": "RICE"}


def test_con_todo_en_la_memoria_funciona_sin_traductor():
    def traductor_roto(texto):
        raise ConnectionError("sin conexión")

    memoria = {"chicken": "pollo"}
    assert traduccion.traducir_lista(["chicken"], traducir_texto=traductor_roto, memoria=memoria) == (["pollo"], True)


def test_si_falla_lo_que_ya_estaba_sale_traducido():
    def traductor_roto(texto):
        raise ConnectionError("sin conexión")

    memoria = {"chicken": "pollo"}
    traducidas, ok = traduccion.traducir_lista(["chicken", "rice"], traducir_texto=traductor_roto, memoria=memoria)
    assert (traducidas, ok) == (["pollo", "rice"], False)


def test_si_falla_el_primer_servicio_usa_el_segundo(monkeypatch):
    def google_bloqueado(texto):
        raise ConnectionError("429 Too Many Requests")

    monkeypatch.setattr(
        traduccion, "_servicios",
        lambda destino: [(google_bloqueado, 1800), (str.upper, 450)],
    )
    assert traduccion.traducir_lista(["chicken", "rice"]) == (["CHICKEN", "RICE"], True)


def test_texto_de_mymemory_detecta_el_limite():
    respuesta = {"responseStatus": 429, "responseData": {"translatedText": "MYMEMORY WARNING: YOU USED ALL"}}
    with pytest.raises(traduccion.TraductorNoDisponible):
        traduccion.texto_de_mymemory(respuesta)


def test_guardar_y_cargar_memoria(tmp_path):
    ruta = tmp_path / "traducciones.json"
    traduccion.guardar_memoria(ruta, {"es": {"Heat the oil.": "Calienta el aceite."}})
    assert traduccion.cargar_memoria(ruta) == {"es": {"Heat the oil.": "Calienta el aceite."}}


def test_cargar_memoria_sin_fichero_o_estropeada(tmp_path):
    assert traduccion.cargar_memoria(tmp_path / "no_existe.json") == {}
    estropeado = tmp_path / "mal.json"
    estropeado.write_text("no es json", encoding="utf-8")
    assert traduccion.cargar_memoria(estropeado) == {}
