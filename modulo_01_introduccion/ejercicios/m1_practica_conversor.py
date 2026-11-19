"""Módulo 1 - Práctica 1: conversor de unidades.

Lee el enunciado en PRACTICA_1.md.
"""

# 1. Define aquí las constantes KM_POR_MILLA y KG_POR_LIBRA
KM_POR_MILLA = 1.609344
KG_POR_LIBRA = 0.45359237

def celsius_a_fahrenheit(grados):
    """Convierte grados Celsius a Fahrenheit."""
    raise NotImplementedError


def fahrenheit_a_celsius(grados):
    """Convierte grados Fahrenheit a Celsius."""
    raise NotImplementedError


def km_a_millas(km):
    """Convierte kilómetros a millas."""
    raise NotImplementedError


def millas_a_km(millas):
    """Convierte millas a kilómetros."""
    raise NotImplementedError


def kg_a_libras(kg):
    """Convierte kilogramos a libras."""
    raise NotImplementedError


def libras_a_kg(libras):
    """Convierte libras a kilogramos."""
    raise NotImplementedError


def formatear(valor, unidad_origen, resultado, unidad_destino):
    """Devuelve el texto de la conversión con dos decimales.

    >>> formatear(100, "°C", 212.0, "°F")
    '100.00 °C = 212.00 °F'
    """
    raise NotImplementedError


def main():
    """Muestra el menú, pide los datos e imprime el resultado."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
