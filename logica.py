"""Lógica del buscador de recetas: todo lo que no depende de internet ni de la web.

Estas funciones reciben y devuelven datos normales (textos, listas y
diccionarios), así que se pueden probar con pytest sin conexión.
"""

import re

# Traducción de los ingredientes más habituales al inglés, que es el idioma de
# TheMealDB. Si un ingrediente no está aquí, se busca tal cual (así también se
# puede escribir directamente en inglés).
TRADUCCIONES = {
    "aceite": "olive oil",
    "aceite de oliva": "olive oil",
    "aguacate": "avocado",
    "ajo": "garlic",
    "almendras": "almonds",
    "arroz": "rice",
    "anchoas": "anchovy fillet",
    "atun": "tuna",
    "atún": "tuna",
    "azucar": "sugar",
    "azúcar": "sugar",
    "bacalao": "cod",
    "bacon": "bacon",
    "beicon": "bacon",
    "berenjena": "aubergine",
    "brocoli": "broccoli",
    "brócoli": "broccoli",
    "caballa": "mackerel",
    "calabacin": "courgette",
    "calamar": "squid",
    "calamares": "squid",
    "calabacín": "courgette",
    "cebolla": "onion",
    "cerdo": "pork",
    "champiñones": "mushrooms",
    "chocolate": "chocolate",
    "cordero": "lamb",
    "espaguetis": "spaghetti",
    "espinacas": "spinach",
    "fresas": "strawberries",
    "gambas": "prawns",
    "garbanzos": "chickpeas",
    "harina": "flour",
    "huevo": "egg",
    "huevos": "eggs",
    "fideos": "noodles",
    "jamon": "ham",
    "jamón": "ham",
    "judias": "beans",
    "judías": "beans",
    "lasaña": "lasagne sheets",
    "leche": "milk",
    "lentejas": "lentils",
    "limon": "lemon",
    "limón": "lemon",
    "lima": "lime",
    "maiz": "sweetcorn",
    "maíz": "sweetcorn",
    "mantequilla": "butter",
    "macarrones": "macaroni",
    "manzana": "apple",
    "mejillones": "mussels",
    "merluza": "haddock",
    "nata": "double cream",
    "pan": "bread",
    "patata": "potatoes",
    "patatas": "potatoes",
    "pavo": "turkey",
    "pepino": "cucumber",
    "pimiento": "red pepper",
    "platano": "banana",
    "plátano": "banana",
    "pollo": "chicken",
    "puerro": "leek",
    "queso": "cheese",
    "salchichas": "sausages",
    "sardinas": "sardines",
    "salmon": "salmon",
    "salmón": "salmon",
    "tomate": "tomato",
    "tomates": "tomatoes",
    "tallarines": "tagliatelle",
    "ternera": "beef",
    "trucha": "trout",
    "yogur": "yogurt",
    "zanahoria": "carrots",
    "zanahorias": "carrots",
}

# Palabras genéricas que no son un ingrediente concreto sino una categoría de
# TheMealDB. "pescado" no existe como ingrediente en la API, pero sí la
# categoría "Seafood" (pescado y marisco).
CATEGORIAS = {
    "pescado": "Seafood",
    "marisco": "Seafood",
    "mariscos": "Seafood",
    "pasta": "Pasta",
    "postre": "Dessert",
    "postres": "Dessert",
    "vegetariano": "Vegetarian",
    "vegano": "Vegan",
}

# Si el usuario dice que tiene "pescado" o "pasta", cualquiera de estos
# ingredientes de la receta cuenta como que lo tiene.
PESCADOS_Y_MARISCOS = [
    "fish", "salmon", "cod", "tuna", "haddock", "mackerel", "sardines",
    "anchov", "trout", "prawn", "shrimp", "mussels", "squid", "crab",
    "lobster", "clams", "oyster", "scallop", "monkfish", "sea bass",
    "tilapia", "herring", "kipper",
]

TIPOS_DE_PASTA = [
    "pasta", "spaghetti", "penne", "farfalle", "linguine", "lasagne",
    "fettuccine", "macaroni", "rigatoni", "tagliatelle", "fusilli",
    "noodles", "ravioli", "tortellini", "orzo",
]

EQUIVALENTES = {
    "Seafood": PESCADOS_Y_MARISCOS,
    "Pasta": TIPOS_DE_PASTA,
}

# Ingredientes que se dan por supuestos en cualquier cocina: no se cuentan
# como "te falta".
BASICOS = {"salt", "water", "pepper", "black pepper", "olive oil", "vegetable oil", "oil"}

MAX_INGREDIENTES_API = 20

# Numeración que traen algunas recetas: "STEP 1", "Step 2:", "1.", "3)"…
NUMERACION_DE_PASO = re.compile(r"^(?:step\s*\d+\s*[.:)\-–]?|\d+\s*[.:)\-–])\s*", re.IGNORECASE)
SOLO_NUMERACION = re.compile(r"(?:step\s*)?\d*[.:)\-–]?", re.IGNORECASE)


def limpiar_ingredientes(texto: str) -> list[str]:
    """Convierte el texto que escribe el usuario en una lista de ingredientes.

    Separa por comas, quita espacios, pasa a minúsculas, descarta los vacíos
    y elimina repetidos conservando el orden.

    >>> limpiar_ingredientes(" Pollo, arroz ,, TOMATE, pollo ")
    ['pollo', 'arroz', 'tomate']
    """
    ingredientes = []
    for trozo in texto.split(","):
        ingrediente = trozo.strip().lower()
        if ingrediente and ingrediente not in ingredientes:
            ingredientes.append(ingrediente)
    return ingredientes


def traducir(ingrediente: str) -> str:
    """Traduce un ingrediente al inglés. Si no se conoce, lo devuelve igual.

    >>> traducir("pollo"), traducir("chicken")
    ('chicken', 'chicken')
    """
    return TRADUCCIONES.get(ingrediente, ingrediente)


def categoria(ingrediente: str) -> str | None:
    """Devuelve la categoría de TheMealDB si la palabra es genérica, o None.

    >>> categoria("pescado"), categoria("pollo")
    ('Seafood', None)
    """
    return CATEGORIAS.get(ingrediente)


def palabras_para_comparar(ingredientes: list[str]) -> list[str]:
    """Pasa mis ingredientes a las palabras en inglés con las que se comparan.

    Traduce cada uno. Si alguno es una palabra genérica como "pescado" o
    "pasta", añade todos los ingredientes concretos de ese tipo.

    >>> palabras_para_comparar(["pollo", "arroz"])
    ['chicken', 'rice']
    >>> "salmon" in palabras_para_comparar(["pescado"])
    True
    """
    palabras = []
    for ingrediente in ingredientes:
        nombre_categoria = categoria(ingrediente)
        if nombre_categoria is None:
            palabras.append(traducir(ingrediente))
        else:
            palabras.extend(EQUIVALENTES.get(nombre_categoria, []))
    return palabras


def combinar_resultados(resultados: dict[str, list[dict]]) -> list[dict]:
    """Junta las recetas encontradas para cada ingrediente y las ordena.

    ``resultados`` relaciona cada ingrediente buscado con la lista de recetas
    que devuelve la API para él. Cada receta del resultado indica qué
    ingredientes del usuario usa. Primero van las que usan más; a igualdad,
    por orden alfabético.

    >>> datos = {
    ...     "pollo": [{"idMeal": "1", "strMeal": "B", "strMealThumb": "b.jpg"}],
    ...     "arroz": [{"idMeal": "1", "strMeal": "B", "strMealThumb": "b.jpg"},
    ...               {"idMeal": "2", "strMeal": "A", "strMealThumb": "a.jpg"}],
    ... }
    >>> [(r["nombre"], r["coincidencias"]) for r in combinar_resultados(datos)]
    [('B', ['pollo', 'arroz']), ('A', ['arroz'])]
    """
    recetas = {}
    for ingrediente, lista in resultados.items():
        for receta in lista:
            id_receta = receta["idMeal"]
            if id_receta not in recetas:
                recetas[id_receta] = {
                    "id": id_receta,
                    "nombre": receta["strMeal"],
                    "foto": receta["strMealThumb"],
                    "coincidencias": [],
                }
            recetas[id_receta]["coincidencias"].append(ingrediente)

    return sorted(
        recetas.values(),
        key=lambda receta: (-len(receta["coincidencias"]), receta["nombre"]),
    )


def extraer_ingredientes(receta: dict) -> list[tuple[str, str]]:
    """Devuelve los ingredientes de una receta como pares (ingrediente, cantidad).

    La API los da repartidos en ``strIngredient1`` … ``strIngredient20`` y
    ``strMeasure1`` … ``strMeasure20``, con huecos vacíos o ``None``.

    >>> extraer_ingredientes({"strIngredient1": "Rice", "strMeasure1": "200g ",
    ...                       "strIngredient2": "", "strMeasure2": " "})
    [('Rice', '200g')]
    """
    ingredientes = []
    for numero in range(1, MAX_INGREDIENTES_API + 1):
        nombre = (receta.get(f"strIngredient{numero}") or "").strip()
        cantidad = (receta.get(f"strMeasure{numero}") or "").strip()
        if nombre:
            ingredientes.append((nombre, cantidad))
    return ingredientes


def lo_tengo(ingrediente_receta: str, mis_ingredientes: list[str]) -> bool:
    """Indica si un ingrediente de la receta está entre los míos o es básico.

    Basta con que uno de los míos aparezca dentro del nombre: si tengo
    "chicken", tengo "Chicken Breast".

    >>> lo_tengo("Chicken Breast", ["chicken"]), lo_tengo("Salt", []), lo_tengo("Lime", ["rice"])
    (True, True, False)
    """
    nombre = ingrediente_receta.lower()
    if nombre in BASICOS:
        return True
    for mio in mis_ingredientes:
        if mio.lower() in nombre:
            return True
    return False


def ingredientes_que_faltan(receta: dict, mis_ingredientes: list[str]) -> list[str]:
    """Devuelve los ingredientes de la receta que no tengo (ni son básicos).

    ``mis_ingredientes`` tiene que estar en inglés, como los de la API.

    >>> receta = {"strIngredient1": "Chicken", "strIngredient2": "Salt",
    ...           "strIngredient3": "Lemon"}
    >>> ingredientes_que_faltan(receta, ["chicken"])
    ['Lemon']
    """
    return [
        nombre
        for nombre, _ in extraer_ingredientes(receta)
        if not lo_tengo(nombre, mis_ingredientes)
    ]


def lo_que_falta(marcas: dict[str, bool]) -> list[str]:
    """Devuelve los ingredientes que el usuario no ha marcado como que los tiene.

    ``marcas`` relaciona cada ingrediente con True (lo tengo) o False (no lo
    tengo). Si un ingrediente aparece repetido en la receta, sale una sola vez.

    >>> lo_que_falta({"Chicken": True, "Ginger": False, "Rice": False})
    ['Ginger', 'Rice']
    """
    return [ingrediente for ingrediente, tengo in marcas.items() if not tengo]


def cuantas_mas(mostradas: int, total: int, por_pagina: int) -> int:
    """Cuántas recetas más se enseñan al pulsar "Ver más" (0 si ya están todas).

    >>> cuantas_mas(12, 80, 12), cuantas_mas(12, 20, 12), cuantas_mas(20, 20, 12)
    (12, 8, 0)
    """
    return max(0, min(por_pagina, total - mostradas))


def agrupar_en_bloques(textos: list[str], max_caracteres: int) -> list[list[str]]:
    """Reparte las frases en bloques que, unidos con saltos de línea, no pasan
    de ``max_caracteres``. Una frase más larga que el máximo va sola.

    Sirve para traducir muchas frases con pocas peticiones.

    >>> agrupar_en_bloques(["aaa", "bb", "cccc", "d"], 7)
    [['aaa', 'bb'], ['cccc', 'd']]
    """
    bloques = []
    actual = []
    tamano = 0
    for frase in textos:
        extra = len(frase) + (1 if actual else 0)  # +1 por el salto de línea
        if actual and tamano + extra > max_caracteres:
            bloques.append(actual)
            actual = []
            tamano = 0
            extra = len(frase)
        actual.append(frase)
        tamano += extra
    if actual:
        bloques.append(actual)
    return bloques


def dividir_instrucciones(texto: str | None) -> list[str]:
    """Separa las instrucciones en pasos, uno por línea con contenido.

    Muchas recetas de TheMealDB traen líneas sueltas como "STEP 1" o "1." y
    pasos que empiezan por "1. " o "Step 2:". Las líneas sueltas se quitan y
    los números del principio también, porque la página ya numera los pasos.

    >>> dividir_instrucciones("STEP 1\\r\\nHeat the oil.\\r\\n\\r\\nstep 2\\r\\n2. Add the rice. ")
    ['Heat the oil.', 'Add the rice.']
    """
    if not texto:
        return []
    pasos = []
    for linea in texto.splitlines():
        paso = NUMERACION_DE_PASO.sub("", linea.strip()).strip()
        if paso and not SOLO_NUMERACION.fullmatch(paso):
            pasos.append(paso)
    return pasos
