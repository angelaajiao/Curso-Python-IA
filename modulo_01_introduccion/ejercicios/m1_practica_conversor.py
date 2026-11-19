"""Módulo 1 - Práctica 1: conversor de unidades.

Lee el enunciado en PRACTICA_1.md.
"""

# 1. Define aquí las constantes KM_POR_MILLA y KG_POR_LIBRA
KM_POR_MILLA = 1.609344
KG_POR_LIBRA = 0.45359237

def celsius_a_fahrenheit(grados):
    """Convierte grados Celsius a Fahrenheit."""
    return grados * 9/5 + 32


def fahrenheit_a_celsius(grados):
    """Convierte grados Fahrenheit a Celsius."""
    return (grados - 32) * 5/9


def km_a_millas(km):
    """Convierte kilómetros a millas."""
    return km / KM_POR_MILLA


def millas_a_km(millas):
    """Convierte millas a kilómetros."""
    return millas * KM_POR_MILLA


def kg_a_libras(kg):
    """Convierte kilogramos a libras."""
    return kg / KG_POR_LIBRA


def libras_a_kg(libras):
    """Convierte libras a kilogramos."""
    return libras * KG_POR_LIBRA


def formatear(valor, unidad_origen, resultado, unidad_destino):
    """Devuelve el texto de la conversión con dos decimales.

    >>> formatear(100, "°C", 212.0, "°F")
    '100.00 °C = 212.00 °F'
    """
    return f"{valor:.2f} {unidad_origen} = {resultado:.2f} {unidad_destino}"

def main():
    """Muestra el menú, pide los datos e imprime el resultado."""
    match input(
        "Elige la conversión:\n"
        "1. Celsius a Fahrenheit\n"
        "2. Fahrenheit a Celsius\n"
        "3. Kilómetros a millas\n"
        "4. Millas a kilómetros\n"
        "5. Kilogramos a libras\n"
        "6. Libras a kilogramos\n"
    ):
        case "1":
            grados = float(input("Grados Celsius: "))
            resultado = celsius_a_fahrenheit(grados)
            print(formatear(grados, "°C", resultado, "°F"))
        case "2":
            grados = float(input("Grados Fahrenheit: "))
            resultado = fahrenheit_a_celsius(grados)
            print(formatear(grados, "°F", resultado, "°C"))
        case "3":
            km = float(input("Kilómetros: "))
            resultado = km_a_millas(km)
            print(formatear(km, "km", resultado, "mi"))
        case "4":
            millas = float(input("Millas: "))
            resultado = millas_a_km(millas)
            print(formatear(millas, "mi", resultado, "km"))
        case "5":
            kg = float(input("Kilogramos: "))
            resultado = kg_a_libras(kg)
            print(formatear(kg, "kg", resultado, "lb"))
        case "6":
            libras = float(input("Libras: "))
            resultado = libras_a_kg(libras)
            print(formatear(libras, "lb", resultado, "kg"))
        case _:
            print("Opción no válida")

if __name__ == "__main__":
    main()
