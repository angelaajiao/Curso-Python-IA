"""Tests de traduccion.py con traductores falsos: no hace falta internet."""

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
