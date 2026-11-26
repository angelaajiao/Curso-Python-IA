"""Tests de logica.py. No necesitan internet: usan datos de ejemplo."""

import pytest

import logica

RECETA = {
    "idMeal": "52772",
    "strMeal": "Teriyaki Chicken Casserole",
    "strIngredient1": "soy sauce",
    "strMeasure1": "3/4 cup",
    "strIngredient2": "Chicken Breasts",
    "strMeasure2": "2",
    "strIngredient3": "Salt",
    "strMeasure3": "pinch",
    "strIngredient4": "Rice",
    "strMeasure4": " 3 cups ",
    "strIngredient5": "",
    "strMeasure5": "",
    "strIngredient6": None,
    "strMeasure6": None,
    "strInstructions": "Preheat oven.\r\n\r\nCook the rice.\r\nServe.",
}


# --------------------------------------------------------- limpiar_ingredientes
@pytest.mark.parametrize(
    "texto, esperado",
    [
        ("pollo, arroz, tomate", ["pollo", "arroz", "tomate"]),
        ("  Pollo ,ARROZ  ", ["pollo", "arroz"]),
        ("pollo, pollo, arroz", ["pollo", "arroz"]),
        ("pollo,, ,arroz", ["pollo", "arroz"]),
        ("", []),
        ("   ", []),
        ("aceite de oliva", ["aceite de oliva"]),
    ],
)
def test_limpiar_ingredientes(texto, esperado):
    assert logica.limpiar_ingredientes(texto) == esperado


# --------------------------------------------------------------------- traducir
@pytest.mark.parametrize(
    "ingrediente, esperado",
    [("pollo", "chicken"), ("atún", "tuna"), ("atun", "tuna"), ("chicken", "chicken")],
)
def test_traducir(ingrediente, esperado):
    assert logica.traducir(ingrediente) == esperado


# ---------------------------------------------------------- combinar_resultados
def _resumen(id_receta, nombre):
    return {"idMeal": id_receta, "strMeal": nombre, "strMealThumb": f"{id_receta}.jpg"}


def test_combinar_ordena_por_coincidencias():
    resultados = {
        "pollo": [_resumen("1", "Curry"), _resumen("2", "Paella")],
        "arroz": [_resumen("2", "Paella"), _resumen("3", "Arroz con leche")],
    }
    recetas = logica.combinar_resultados(resultados)
    assert [receta["nombre"] for receta in recetas] == ["Paella", "Arroz con leche", "Curry"]
    assert recetas[0]["coincidencias"] == ["pollo", "arroz"]


def test_combinar_guarda_id_y_foto():
    recetas = logica.combinar_resultados({"pollo": [_resumen("7", "Curry")]})
    assert recetas == [{"id": "7", "nombre": "Curry", "foto": "7.jpg", "coincidencias": ["pollo"]}]


def test_combinar_sin_resultados():
    assert logica.combinar_resultados({"pollo": [], "arroz": []}) == []


# --------------------------------------------------------- extraer_ingredientes
def test_extraer_ingredientes_salta_vacios_y_none():
    assert logica.extraer_ingredientes(RECETA) == [
        ("soy sauce", "3/4 cup"),
        ("Chicken Breasts", "2"),
        ("Salt", "pinch"),
        ("Rice", "3 cups"),
    ]


def test_extraer_ingredientes_receta_vacia():
    assert logica.extraer_ingredientes({}) == []


# ---------------------------------------------------- lo_tengo / que_faltan
@pytest.mark.parametrize(
    "ingrediente, mios, esperado",
    [
        ("Chicken Breasts", ["chicken"], True),
        ("Rice", ["rice"], True),
        ("RICE", ["rice"], True),
        ("Salt", [], True),
        ("Lemon", ["chicken"], False),
    ],
)
def test_lo_tengo(ingrediente, mios, esperado):
    assert logica.lo_tengo(ingrediente, mios) is esperado


def test_ingredientes_que_faltan():
    assert logica.ingredientes_que_faltan(RECETA, ["chicken"]) == ["soy sauce", "Rice"]


def test_no_falta_nada():
    assert logica.ingredientes_que_faltan(RECETA, ["chicken", "rice", "soy sauce"]) == []


# -------------------------------------------------------- dividir_instrucciones
def test_dividir_instrucciones():
    assert logica.dividir_instrucciones(RECETA["strInstructions"]) == [
        "Preheat oven.",
        "Cook the rice.",
        "Serve.",
    ]


@pytest.mark.parametrize("texto", [None, "", "  \r\n "])
def test_dividir_instrucciones_vacias(texto):
    assert logica.dividir_instrucciones(texto) == []


# ------------------------------------------------ categorías (pescado, postre…)
@pytest.mark.parametrize(
    "palabra, esperado",
    [
        ("pescado", "Seafood"),
        ("marisco", "Seafood"),
        ("pasta", "Pasta"),
        ("postre", "Dessert"),
        ("pollo", None),
    ],
)
def test_categoria(palabra, esperado):
    assert logica.categoria(palabra) == esperado


def test_palabras_para_comparar_traduce():
    assert logica.palabras_para_comparar(["pollo", "bacalao"]) == ["chicken", "cod"]


def test_palabras_para_comparar_con_pescado():
    palabras = logica.palabras_para_comparar(["pescado", "arroz"])
    assert "salmon" in palabras and "prawn" in palabras and "rice" in palabras


def test_palabras_para_comparar_ignora_postre():
    assert logica.palabras_para_comparar(["postre"]) == []


def test_con_pescado_no_falta_el_salmon():
    receta = {"strIngredient1": "Salmon", "strIngredient2": "King Prawns", "strIngredient3": "Lemon"}
    mios = logica.palabras_para_comparar(["pescado"])
    assert logica.ingredientes_que_faltan(receta, mios) == ["Lemon"]


def test_con_pasta_no_faltan_los_espaguetis():
    receta = {"strIngredient1": "Spaghetti", "strIngredient2": "Parmesan"}
    mios = logica.palabras_para_comparar(["pasta"])
    assert logica.ingredientes_que_faltan(receta, mios) == ["Parmesan"]


@pytest.mark.parametrize(
    "ingrediente, esperado",
    [("macarrones", "macaroni"), ("espaguetis", "spaghetti"), ("lasaña", "lasagne sheets")],
)
def test_traducir_pastas(ingrediente, esperado):
    assert logica.traducir(ingrediente) == esperado


# ------------------------------------------------------------------ lo_que_falta
def test_lo_que_falta():
    marcas = {"Chicken": True, "Ginger": False, "Salt": True, "Rice": False}
    assert logica.lo_que_falta(marcas) == ["Ginger", "Rice"]


def test_lo_que_falta_todo_marcado():
    assert logica.lo_que_falta({"Chicken": True, "Rice": True}) == []


def test_lo_que_falta_sin_ingredientes():
    assert logica.lo_que_falta({}) == []


# ------------------------------------------------------------ agrupar_en_bloques
def test_agrupar_en_bloques_respeta_el_maximo():
    frases = ["a" * 10] * 5
    bloques = logica.agrupar_en_bloques(frases, 25)
    assert bloques == [["a" * 10] * 2, ["a" * 10] * 2, ["a" * 10]]
    assert all(len("\n".join(bloque)) <= 25 for bloque in bloques)


def test_agrupar_en_bloques_frase_larga_va_sola():
    assert logica.agrupar_en_bloques(["corta", "x" * 50, "otra"], 20) == [
        ["corta"],
        ["x" * 50],
        ["otra"],
    ]


def test_agrupar_en_bloques_vacio():
    assert logica.agrupar_en_bloques([], 100) == []


# ------------------------------------------------------------------ cuantas_mas
@pytest.mark.parametrize(
    "mostradas, total, esperado",
    [(12, 80, 12), (12, 20, 8), (20, 20, 0), (12, 7, 0), (0, 5, 5)],
)
def test_cuantas_mas(mostradas, total, esperado):
    assert logica.cuantas_mas(mostradas, total, 12) == esperado


# ------------------------------------------- dividir_instrucciones: numeración
@pytest.mark.parametrize(
    "texto, esperado",
    [
        ("step 1\nHeat the oil.\nstep 2\nAdd the onion.", ["Heat the oil.", "Add the onion."]),
        ("STEP 1\r\n\r\nHeat the oil.", ["Heat the oil."]),
        ("1.\nHeat the oil.\n2.\nServe.", ["Heat the oil.", "Serve."]),
        ("1. Heat the oil.\n2) Serve.", ["Heat the oil.", "Serve."]),
        ("Step 3: Bake for 20 mins.", ["Bake for 20 mins."]),
        ("2 eggs, beaten.", ["2 eggs, beaten."]),
        ("Bake at 180C for 20-25 mins.", ["Bake at 180C for 20-25 mins."]),
    ],
)
def test_dividir_instrucciones_quita_la_numeracion(texto, esperado):
    assert logica.dividir_instrucciones(texto) == esperado


# -------------------------------------------------------------- rellenar_huecos
def test_rellenar_huecos():
    assert logica.rellenar_huecos([None, "Sal", None], ["Uno", "Dos"]) == ["Uno", "Sal", "Dos"]


def test_rellenar_huecos_todo_conocido_o_todo_automatico():
    assert logica.rellenar_huecos(["Sal", "Agua"], []) == ["Sal", "Agua"]
    assert logica.rellenar_huecos([None, None], ["A", "B"]) == ["A", "B"]
