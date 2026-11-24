"""Muestra todas las comidas de TheMealDB agrupadas por categoría.

Ejecutar con:  python listar_comidas.py
Para guardarlo en un fichero:  python listar_comidas.py > comidas.txt
"""

import requests

import api


def categorias() -> list[str]:
    """Nombres de todas las categorías de TheMealDB."""
    respuesta = requests.get(f"{api.URL_BASE}/list.php", params={"c": "list"},
                             timeout=api.TIEMPO_MAXIMO)
    respuesta.raise_for_status()
    return [categoria["strCategory"] for categoria in respuesta.json()["meals"]]


def main():
    total = 0
    for categoria in categorias():
        comidas = sorted(receta["strMeal"] for receta in api.buscar_por_categoria(categoria))
        total += len(comidas)
        print(f"\n{categoria} ({len(comidas)})")
        for comida in comidas:
            print(f"  - {comida}")
    print(f"\nTotal: {total} comidas")


if __name__ == "__main__":
    main()
