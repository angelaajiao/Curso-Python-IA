"""Textos de la interfaz en español e inglés.

Toda frase que se ve en la página sale de aquí, así que cambiar o añadir un
idioma no obliga a tocar app.py.
"""

IDIOMAS = {"es": "🇪🇸 Español", "en": "🇬🇧 English"}
IDIOMA_POR_DEFECTO = "es"

TEXTOS = {
    "es": {
        "titulo": "¿Qué puedo cocinar?",
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
        "pie": "Recetas de TheMealDB · Hecho con Python y Streamlit",
        "seccion_buscar": "🔍 Buscar",
        "seccion_favoritas": "❤️ Favoritas ({n})",
        "titulo_favoritas": "Tus recetas favoritas",
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
