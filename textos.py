"""Textos de la interfaz en español e inglés.

Toda frase que se ve en la página sale de aquí, así que cambiar o añadir un
idioma no obliga a tocar app.py.
"""

IDIOMAS = {"es": "🇪🇸 Español", "en": "🇬🇧 English"}
IDIOMA_POR_DEFECTO = "es"

TEXTOS = {
    "es": {
        "titulo": "¿Qué puedo cocinar hoy? 🤔",
        "subtitulo": "Escribe lo que tienes en la nevera, separado por comas, y te propongo recetas.",
        "campo_ingredientes": "Ingredientes",
        "placeholder": "pollo, arroz, tomate",
        "buscar": "Buscar recetas",
        "sorprendeme": "Sorpréndeme",
        "escribe_algo": "Escribe al menos un ingrediente.",
        "sin_conexion": "No se ha podido conectar con TheMealDB. Revisa tu conexión e inténtalo de nuevo.",
        "buscando": "Buscando recetas…",
        "traduciendo": "Traduciendo…",
        "encontradas": "{n} recetas encontradas",
        "encontradas_detalle": "Primero, las que usan más de tus ingredientes.",
        "sin_resultados": "No hay recetas con esos ingredientes. Prueba con otros o escríbelos en inglés.",
        "coincidencias": "{n} de {total} de tus ingredientes",
        "usa": "Usa: {lista}",
        "ver_receta": "Ver receta",
        "mostrando": "Mostrando {n} de {total} recetas",
        "ver_mas": "Ver {n} más",
        "volver": "Volver a los resultados",
        "n_ingredientes": "{n} ingredientes",
        "pestana_ingredientes": "Ingredientes",
        "pestana_preparacion": "Preparación",
        "pestana_video": "Vídeo",
        "marca_lo_que_tienes": "Marca lo que tienes en casa. La sal, la pimienta, el agua y el aceite vienen marcados por defecto.",
        "marcar_todo": "Marcar todo",
        "desmarcar_todo": "Desmarcar todo",
        "tienes": "Tienes {tengo} de {total} ingredientes",
        "te_falta": "Te falta: {lista}",
        "tienes_todo": "¡Tienes todo lo necesario!",
        "sin_pasos": "Esta receta no tiene instrucciones.",
        "sin_video": "Esta receta no trae vídeo, pero puedes buscar uno en YouTube.",
        "buscar_video": "Buscar vídeos en YouTube",
        "busqueda_video": "{receta} receta",
        "receta_original": "Ver la receta original",
        "no_encontrada": "No se ha encontrado la receta.",
        "sin_traduccion": "No se ha podido traducir la receta, así que se muestra en inglés. Vuelve a abrirla para intentarlo de nuevo.",
        "pie": "Recetas de TheMealDB · Angela Jiao",
        "seccion_buscar": "🔍 Buscar",
        "seccion_favoritas": "❤️ Favoritas ({n})",
        "titulo_favoritas": "Tus favoritos",
        "sin_favoritas": "Todavía no tienes favoritas. Abre una receta y pulsa «Guardar en favoritas», o toca el corazón de una tarjeta.",
        "guardar_favorita": "Guardar en favoritas",
        "quitar_favorita": "Quitar de favoritas",
        "aviso_guardada": "Receta guardada en favoritas",
        "aviso_quitada": "Receta quitada de favoritas",
    },
    "en": {
        "titulo": "What can I cook?",
        "subtitulo": "Type what you have in the fridge, separated by commas, and I'll suggest recipes.",
        "campo_ingredientes": "Ingredients",
        "placeholder": "chicken, rice, tomato",
        "buscar": "Search recipes",
        "sorprendeme": "Surprise me",
        "escribe_algo": "Type at least one ingredient.",
        "sin_conexion": "Couldn't connect to TheMealDB. Check your connection and try again.",
        "buscando": "Searching recipes…",
        "traduciendo": "Translating…",
        "encontradas": "{n} recipes found",
        "encontradas_detalle": "The ones that use more of your ingredients come first.",
        "sin_resultados": "No recipes with those ingredients. Try different ones.",
        "coincidencias": "{n} of your {total} ingredients",
        "usa": "Uses: {lista}",
        "ver_receta": "View recipe",
        "mostrando": "Showing {n} of {total} recipes",
        "ver_mas": "Show {n} more",
        "volver": "Back to results",
        "n_ingredientes": "{n} ingredients",
        "pestana_ingredientes": "Ingredients",
        "pestana_preparacion": "Method",
        "pestana_video": "Video",
        "marca_lo_que_tienes": "Tick what you have at home. Salt, pepper, water and oil are ticked by default.",
        "marcar_todo": "Tick all",
        "desmarcar_todo": "Untick all",
        "tienes": "You have {tengo} of {total} ingredients",
        "te_falta": "You're missing: {lista}",
        "tienes_todo": "You have everything you need!",
        "sin_pasos": "This recipe has no instructions.",
        "sin_video": "This recipe has no video, but you can look for one on YouTube.",
        "buscar_video": "Search YouTube videos",
        "busqueda_video": "{receta} recipe",
        "receta_original": "See the original recipe",
        "no_encontrada": "Recipe not found.",
        "sin_traduccion": "",
        "pie": "Recipes from TheMealDB · Made with Python and Streamlit",
        "seccion_buscar": "🔍 Search",
        "seccion_favoritas": "❤️ Favourites ({n})",
        "titulo_favoritas": "Your favourite recipes",
        "sin_favoritas": "You have no favourites yet. Open a recipe and press “Save to favourites”, or tap the heart on a card.",
        "guardar_favorita": "Save to favourites",
        "quitar_favorita": "Remove from favourites",
        "aviso_guardada": "Recipe saved to favourites",
        "aviso_quitada": "Recipe removed from favourites",
    },
}

# Categorías y cocinas de TheMealDB en español. Si alguna no está, se deja
# en inglés.
CATEGORIAS_ES = {
    "Beef": "Ternera",
    "Breakfast": "Desayuno",
    "Chicken": "Pollo",
    "Dessert": "Postre",
    "Goat": "Cabra",
    "Lamb": "Cordero",
    "Miscellaneous": "Variado",
    "Pasta": "Pasta",
    "Pork": "Cerdo",
    "Seafood": "Pescado y marisco",
    "Side": "Guarnición",
    "Starter": "Entrante",
    "Vegan": "Vegana",
    "Vegetarian": "Vegetariana",
}

COCINAS_ES = {
    "Algerian": "Argelina",
    "American": "Americana",
    "Argentinian": "Argentina",
    "Australian": "Australiana",
    "British": "Británica",
    "Canadian": "Canadiense",
    "Chinese": "China",
    "Croatian": "Croata",
    "Dutch": "Neerlandesa",
    "Egyptian": "Egipcia",
    "Filipino": "Filipina",
    "French": "Francesa",
    "Greek": "Griega",
    "Indian": "India",
    "Irish": "Irlandesa",
    "Italian": "Italiana",
    "Jamaican": "Jamaicana",
    "Japanese": "Japonesa",
    "Kenyan": "Keniana",
    "Malaysian": "Malasia",
    "Mexican": "Mexicana",
    "Moroccan": "Marroquí",
    "Norwegian": "Noruega",
    "Polish": "Polaca",
    "Portuguese": "Portuguesa",
    "Russian": "Rusa",
    "Saudi Arabian": "Saudí",
    "Slovakian": "Eslovaca",
    "Spanish": "Española",
    "Syrian": "Siria",
    "Thai": "Tailandesa",
    "Tunisian": "Tunecina",
    "Turkish": "Turca",
    "Ukrainian": "Ucraniana",
    "Unknown": "Desconocida",
    "Uruguayan": "Uruguaya",
    "Venezulan": "Venezolana",
    "Venezuelan": "Venezolana",
    "Vietnamese": "Vietnamita",
}


def texto(clave: str, idioma: str, **datos) -> str:
    """Devuelve el texto ``clave`` en el idioma pedido, con los datos rellenos.

    Si el idioma no existe se usa el español.

    >>> texto("tienes", "es", tengo=3, total=5)
    'Tienes 3 de 5 ingredientes'
    >>> texto("ver_receta", "en")
    'View recipe'
    """
    textos_idioma = TEXTOS.get(idioma, TEXTOS[IDIOMA_POR_DEFECTO])
    return textos_idioma[clave].format(**datos)


def nombre_categoria(categoria: str | None, idioma: str) -> str:
    """Nombre de la categoría en el idioma pedido.

    >>> nombre_categoria("Seafood", "es"), nombre_categoria("Seafood", "en")
    ('Pescado y marisco', 'Seafood')
    """
    if not categoria:
        return ""
    return CATEGORIAS_ES.get(categoria, categoria) if idioma == "es" else categoria


def nombre_cocina(cocina: str | None, idioma: str) -> str:
    """Nombre del tipo de cocina (país) en el idioma pedido.

    >>> nombre_cocina("Italian", "es"), nombre_cocina("Italian", "en")
    ('Italiana', 'Italian')
    """
    if not cocina:
        return ""
    return COCINAS_ES.get(cocina, cocina) if idioma == "es" else cocina


# Nombres de ingredientes de TheMealDB en español. Se usan antes que el
# traductor automático, porque una palabra suelta sin contexto se traduce mal
# ("Oil" sale "Petróleo", "Stock" sale "Existencias"…). Las claves van en
# minúsculas. Lo que no esté aquí se traduce automáticamente.
INGREDIENTES_ES = {
    "almonds": "almendras",
    "apple": "manzana",
    "aubergine": "berenjena",
    "avocado": "aguacate",
    "bacon": "beicon",
    "baking powder": "levadura química",
    "banana": "plátano",
    "basil": "albahaca",
    "bay leaf": "hoja de laurel",
    "bay leaves": "hojas de laurel",
    "beef": "ternera",
    "beef stock": "caldo de carne",
    "bicarbonate of soda": "bicarbonato",
    "black pepper": "pimienta negra",
    "bread": "pan",
    "breadcrumbs": "pan rallado",
    "broccoli": "brócoli",
    "brown sugar": "azúcar moreno",
    "butter": "mantequilla",
    "caster sugar": "azúcar extrafino",
    "carrot": "zanahoria",
    "carrots": "zanahorias",
    "celery": "apio",
    "cheddar cheese": "queso cheddar",
    "cheese": "queso",
    "chicken": "pollo",
    "chicken breast": "pechuga de pollo",
    "chicken breasts": "pechugas de pollo",
    "chicken stock": "caldo de pollo",
    "chicken thighs": "muslos de pollo",
    "chickpeas": "garbanzos",
    "chilli": "guindilla",
    "chilli powder": "chile en polvo",
    "chocolate": "chocolate",
    "chopped tomatoes": "tomate troceado",
    "cinnamon": "canela",
    "cloves": "clavos",
    "coconut milk": "leche de coco",
    "cod": "bacalao",
    "coriander": "cilantro",
    "courgette": "calabacín",
    "cream": "nata",
    "cucumber": "pepino",
    "cumin": "comino",
    "double cream": "nata para montar",
    "egg": "huevo",
    "egg yolks": "yemas de huevo",
    "eggs": "huevos",
    "flour": "harina",
    "garlic": "ajo",
    "garlic clove": "diente de ajo",
    "ginger": "jengibre",
    "green pepper": "pimiento verde",
    "ham": "jamón",
    "heavy cream": "nata para montar",
    "honey": "miel",
    "lamb": "cordero",
    "leek": "puerro",
    "lemon": "limón",
    "lemon juice": "zumo de limón",
    "lentils": "lentejas",
    "lettuce": "lechuga",
    "lime": "lima",
    "milk": "leche",
    "minced beef": "carne picada de ternera",
    "mint": "hierbabuena",
    "mushrooms": "champiñones",
    "mussels": "mejillones",
    "nutmeg": "nuez moscada",
    "oil": "aceite",
    "olive oil": "aceite de oliva",
    "onion": "cebolla",
    "onions": "cebollas",
    "oregano": "orégano",
    "paprika": "pimentón",
    "parmesan": "parmesano",
    "parsley": "perejil",
    "pasta": "pasta",
    "peas": "guisantes",
    "pepper": "pimienta",
    "plain flour": "harina de trigo",
    "pork": "cerdo",
    "potato": "patata",
    "potatoes": "patatas",
    "prawns": "gambas",
    "red onion": "cebolla morada",
    "red pepper": "pimiento rojo",
    "red wine": "vino tinto",
    "rice": "arroz",
    "rosemary": "romero",
    "salmon": "salmón",
    "salt": "sal",
    "sausages": "salchichas",
    "self-raising flour": "harina con levadura",
    "shallots": "chalotas",
    "single cream": "nata líquida",
    "soy sauce": "salsa de soja",
    "spaghetti": "espaguetis",
    "spinach": "espinacas",
    "spring onions": "cebolletas",
    "squid": "calamar",
    "stock": "caldo",
    "sugar": "azúcar",
    "sunflower oil": "aceite de girasol",
    "sweetcorn": "maíz dulce",
    "thyme": "tomillo",
    "tomato": "tomate",
    "tomato puree": "concentrado de tomate",
    "tomatoes": "tomates",
    "tuna": "atún",
    "turmeric": "cúrcuma",
    "vanilla extract": "extracto de vainilla",
    "vegetable oil": "aceite vegetal",
    "vegetable stock": "caldo de verduras",
    "vinegar": "vinagre",
    "water": "agua",
    "white wine": "vino blanco",
    "yeast": "levadura",
    "yogurt": "yogur",
}


def ingrediente_conocido(nombre: str, idioma: str) -> str | None:
    """Traducción fija de un ingrediente, o ``None`` si no está en el diccionario.

    En inglés no hay nada que traducir. Se respeta la mayúscula inicial.

    >>> ingrediente_conocido("Oil", "es"), ingrediente_conocido("olive oil", "es")
    ('Aceite', 'aceite de oliva')
    >>> ingrediente_conocido("Dragon fruit", "es") is None, ingrediente_conocido("Oil", "en") is None
    (True, True)
    """
    if idioma != "es":
        return None
    limpio = nombre.strip()
    traduccion = INGREDIENTES_ES.get(limpio.lower())
    if traduccion and limpio[:1].isupper():
        return traduccion[0].upper() + traduccion[1:]
    return traduccion
