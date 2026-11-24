"""Tests de favoritos.py. Usan una carpeta temporal para el fichero JSON."""

import favoritos

ADA = {"id": "1", "nombre": "Curry", "foto": "1.jpg"}
LINUS = {"id": "2", "nombre": "Paella", "foto": "2.jpg"}


def test_alternar_anade_y_quita():
    con_una = favoritos.alternar([], ADA)
    assert con_una == [ADA]
    con_dos = favoritos.alternar(con_una, LINUS)
    assert con_dos == [ADA, LINUS]
    assert favoritos.alternar(con_dos, ADA) == [LINUS]


def test_alternar_no_modifica_la_lista():
    originales = [ADA]
    favoritos.alternar(originales, LINUS)
    favoritos.alternar(originales, ADA)
    assert originales == [ADA]


def test_es_favorita():
    assert favoritos.es_favorita([ADA, LINUS], "2")
    assert not favoritos.es_favorita([ADA], "2")


def test_resumen_de_una_receta_de_la_api():
    receta = {"idMeal": "7", "strMeal": "Tacos", "strMealThumb": "7.jpg", "strInstructions": "..."}
    assert favoritos.resumen(receta) == {"id": "7", "nombre": "Tacos", "foto": "7.jpg"}


def test_guardar_y_cargar(tmp_path):
    ruta = tmp_path / "favoritos.json"
    favoritos.guardar(ruta, [ADA, LINUS])
    assert favoritos.cargar(ruta) == [ADA, LINUS]


def test_guardar_respeta_las_tildes(tmp_path):
    ruta = tmp_path / "favoritos.json"
    favoritos.guardar(ruta, [{"id": "3", "nombre": "Crème brûlée", "foto": "3.jpg"}])
    assert "Crème brûlée" in ruta.read_text(encoding="utf-8")


def test_cargar_sin_fichero(tmp_path):
    assert favoritos.cargar(tmp_path / "no_existe.json") == []


def test_cargar_fichero_estropeado(tmp_path):
    ruta = tmp_path / "favoritos.json"
    ruta.write_text("esto no es json", encoding="utf-8")
    assert favoritos.cargar(ruta) == []


def test_cargar_ignora_datos_raros(tmp_path):
    ruta = tmp_path / "favoritos.json"
    ruta.write_text('[{"id": "1", "nombre": "A", "foto": "a"}, "texto", {"sin_id": true}]', encoding="utf-8")
    assert favoritos.cargar(ruta) == [{"id": "1", "nombre": "A", "foto": "a"}]
    ruta.write_text('{"id": "1"}', encoding="utf-8")
    assert favoritos.cargar(ruta) == []
