"""Tests de textos.py: que los dos idiomas tengan los mismos textos."""

import pytest

import textos


def test_los_dos_idiomas_tienen_las_mismas_claves():
    assert set(textos.TEXTOS["es"]) == set(textos.TEXTOS["en"])


def test_hay_un_texto_por_cada_idioma_del_selector():
    assert set(textos.IDIOMAS) == set(textos.TEXTOS)


@pytest.mark.parametrize("idioma", ["es", "en"])
def test_textos_con_datos(idioma):
    assert "3" in textos.texto("tienes", idioma, tengo=3, total=5)
    assert "Ginger" in textos.texto("te_falta", idioma, lista="Ginger")


def test_idioma_desconocido_usa_espanol():
    assert textos.texto("ver_receta", "fr") == "Ver receta"


@pytest.mark.parametrize(
    "categoria, idioma, esperado",
    [("Chicken", "es", "Pollo"), ("Chicken", "en", "Chicken"), ("Nueva", "es", "Nueva"), (None, "es", "")],
)
def test_nombre_categoria(categoria, idioma, esperado):
    assert textos.nombre_categoria(categoria, idioma) == esperado


@pytest.mark.parametrize(
    "cocina, idioma, esperado",
    [("Chinese", "es", "China"), ("Chinese", "en", "Chinese"), ("Atlantis", "es", "Atlantis")],
)
def test_nombre_cocina(cocina, idioma, esperado):
    assert textos.nombre_cocina(cocina, idioma) == esperado


@pytest.mark.parametrize(
    "nombre, esperado",
    [
        ("Oil", "Aceite"),
        ("oil", "aceite"),
        ("Olive Oil", "Aceite de oliva"),
        ("Stock", "Caldo"),
        (" Salt ", "Sal"),
        ("Dragon fruit", None),
    ],
)
def test_ingrediente_conocido_en_espanol(nombre, esperado):
    assert textos.ingrediente_conocido(nombre, "es") == esperado


def test_ingrediente_conocido_en_ingles_no_traduce():
    assert textos.ingrediente_conocido("Oil", "en") is None


def test_diccionario_de_ingredientes_en_minusculas():
    assert all(clave == clave.lower().strip() for clave in textos.INGREDIENTES_ES)
