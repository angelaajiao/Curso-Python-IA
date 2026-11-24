"""Recetas favoritas guardadas en un fichero JSON.

Cada favorita se guarda con lo justo para enseñarla en una tarjeta: su id,
su nombre y su foto. Al abrirla se piden el resto de datos a la API.

Las funciones no modifican la lista que reciben: devuelven una nueva.
"""

import json
from pathlib import Path


def resumen(receta: dict) -> dict:
    """Saca de una receta completa de la API los datos que se guardan.

    >>> resumen({"idMeal": "52772", "strMeal": "Teriyaki", "strMealThumb": "t.jpg", "strArea": "Japanese"})
    {'id': '52772', 'nombre': 'Teriyaki', 'foto': 't.jpg'}
    """
    return {"id": receta["idMeal"], "nombre": receta["strMeal"], "foto": receta["strMealThumb"]}


def es_favorita(favoritas: list[dict], id_receta: str) -> bool:
    """Indica si la receta con ese id está entre las favoritas.

    >>> es_favorita([{"id": "1"}, {"id": "2"}], "2"), es_favorita([], "2")
    (True, False)
    """
    return any(favorita["id"] == id_receta for favorita in favoritas)


def alternar(favoritas: list[dict], receta: dict) -> list[dict]:
    """Añade la receta a favoritas o, si ya estaba, la quita.

    ``receta`` es un resumen con id, nombre y foto. Devuelve una lista nueva.

    >>> favoritas = alternar([], {"id": "1", "nombre": "A", "foto": "a.jpg"})
    >>> [f["id"] for f in favoritas], [f["id"] for f in alternar(favoritas, {"id": "1"})]
    (['1'], [])
    """
    if es_favorita(favoritas, receta["id"]):
        return [favorita for favorita in favoritas if favorita["id"] != receta["id"]]
    return [*favoritas, receta]


def cargar(ruta: Path) -> list[dict]:
    """Lee las favoritas del fichero. Si no existe o está estropeado, lista vacía."""
    try:
        datos = json.loads(ruta.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    if not isinstance(datos, list):
        return []
    return [receta for receta in datos if isinstance(receta, dict) and "id" in receta]


def guardar(ruta: Path, favoritas: list[dict]) -> None:
    """Escribe las favoritas en el fichero, en un formato fácil de leer."""
    ruta.write_text(json.dumps(favoritas, ensure_ascii=False, indent=2), encoding="utf-8")
