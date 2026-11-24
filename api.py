"""Acceso a TheMealDB (https://www.themealdb.com).

Usa la clave pública de pruebas "1", que no necesita registro. Con ella el
filtro por ingrediente admite solo un ingrediente por petición; por eso se hace
una petición por ingrediente y se combinan en logica.combinar_resultados.
"""

import requests

URL_BASE = "https://www.themealdb.com/api/json/v1/1"
TIEMPO_MAXIMO = 10  # segundos


def _pedir(endpoint: str, parametros: dict | None = None) -> list[dict]:
    """Hace la petición y devuelve la lista de recetas (vacía si no hay)."""
    respuesta = requests.get(
        f"{URL_BASE}/{endpoint}", params=parametros, timeout=TIEMPO_MAXIMO
    )
    respuesta.raise_for_status()
    return respuesta.json().get("meals") or []


def buscar_por_ingrediente(ingrediente: str) -> list[dict]:
    """Recetas que llevan un ingrediente (en inglés). Solo id, nombre y foto."""
    return _pedir("filter.php", {"i": ingrediente})


def buscar_por_categoria(nombre_categoria: str) -> list[dict]:
    """Recetas de una categoría ("Seafood", "Dessert"…). Solo id, nombre y foto."""
    return _pedir("filter.php", {"c": nombre_categoria})


def obtener_receta(id_receta: str) -> dict | None:
    """Receta completa: ingredientes, cantidades, instrucciones, foto…"""
    recetas = _pedir("lookup.php", {"i": id_receta})
    return recetas[0] if recetas else None


def receta_aleatoria() -> dict | None:
    """Una receta completa al azar."""
    recetas = _pedir("random.php")
    return recetas[0] if recetas else None


if __name__ == "__main__":
    # Prueba rápida desde la terminal: python api.py
    encontradas = buscar_por_ingrediente("chicken")
    print(f"Recetas con pollo: {len(encontradas)}")
    for receta in encontradas[:5]:
        print(f" - {receta['strMeal']} (id {receta['idMeal']})")
