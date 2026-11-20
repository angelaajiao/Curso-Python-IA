"""Módulo 1 - Práctica 1: conversor de unidades. SOLUCIÓN DE REFERENCIA."""

<<<<<<< HEAD
Lee el enunciado en PRACTICA_1.md.
"""

# 1. Define aquí las constantes KM_POR_MILLA y KG_POR_LIBRA
KM_POR_MILLA = 1.609344
KG_POR_LIBRA = 0.45359237

def celsius_a_fahrenheit(grados):
    """Convierte grados Celsius a Fahrenheit."""
    return grados * 9/5 + 32
=======
KM_POR_MILLA = 1.609344
KG_POR_LIBRA = 0.45359237


def celsius_a_fahrenheit(grados):
    """Convierte grados Celsius a Fahrenheit."""
    return grados * 9 / 5 + 32
>>>>>>> c67e6ab911f0511b15210cc127f0d3c5623470b5


def fahrenheit_a_celsius(grados):
    """Convierte grados Fahrenheit a Celsius."""
<<<<<<< HEAD
    return (grados - 32) * 5/9
=======
    return (grados - 32) * 5 / 9
>>>>>>> c67e6ab911f0511b15210cc127f0d3c5623470b5


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
<<<<<<< HEAD

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
=======


def mostrar_menu():
    """Imprime el menú de opciones."""
    print("Conversor de unidades")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Kilómetros a millas")
    print("4. Millas a kilómetros")
    print("5. Kilogramos a libras")
    print("6. Libras a kilogramos")


def main():
    """Muestra el menú, pide los datos e imprime el resultado."""
    mostrar_menu()
    opcion = input("Elige una opción (1-6): ").strip()

    # Solución con lo visto en el módulo 1: una cadena de if / elif.
    # Se compara la opción como texto para no fallar si escriben letras.
    if opcion not in ("1", "2", "3", "4", "5", "6"):
        print("Opción no válida")
        return

    valor = float(input("Valor a convertir: "))

    if opcion == "1":
        print(formatear(valor, "°C", celsius_a_fahrenheit(valor), "°F"))
    elif opcion == "2":
        print(formatear(valor, "°F", fahrenheit_a_celsius(valor), "°C"))
    elif opcion == "3":
        print(formatear(valor, "km", km_a_millas(valor), "mi"))
    elif opcion == "4":
        print(formatear(valor, "mi", millas_a_km(valor), "km"))
    elif opcion == "5":
        print(formatear(valor, "kg", kg_a_libras(valor), "lb"))
    else:
        print(formatear(valor, "lb", libras_a_kg(valor), "kg"))

    # Al llegar al módulo 4 conviene volver a esta práctica y sustituir la
    # cadena de if por un diccionario {opción: (función, origen, destino)}.

>>>>>>> c67e6ab911f0511b15210cc127f0d3c5623470b5

if __name__ == "__main__":
    main()
