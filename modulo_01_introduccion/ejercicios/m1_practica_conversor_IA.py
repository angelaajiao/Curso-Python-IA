"""Módulo 1 - Práctica 1: conversor de unidades."""

from collections.abc import Callable

KM_POR_MILLA = 1.609344
KG_POR_LIBRA = 0.45359237


def celsius_a_fahrenheit(grados: float) -> float:
    """Convierte grados Celsius a Fahrenheit."""
    return grados * 9 / 5 + 32


def fahrenheit_a_celsius(grados: float) -> float:
    """Convierte grados Fahrenheit a Celsius."""
    return (grados - 32) * 5 / 9


def km_a_millas(km: float) -> float:
    """Convierte kilómetros a millas."""
    return km / KM_POR_MILLA


def millas_a_km(millas: float) -> float:
    """Convierte millas a kilómetros."""
    return millas * KM_POR_MILLA


def kg_a_libras(kg: float) -> float:
    """Convierte kilogramos a libras."""
    return kg / KG_POR_LIBRA


def libras_a_kg(libras: float) -> float:
    """Convierte libras a kilogramos."""
    return libras * KG_POR_LIBRA


def formatear(
    valor: float,
    unidad_origen: str,
    resultado: float,
    unidad_destino: str,
) -> str:
    """Devuelve la conversión con los dos valores a dos decimales."""
    return f"{valor:.2f} {unidad_origen} = {resultado:.2f} {unidad_destino}"


def mostrar_menu() -> None:
    """Imprime el menú de conversiones disponibles."""
    print("Conversor de unidades")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Kilómetros a millas")
    print("4. Millas a kilómetros")
    print("5. Kilogramos a libras")
    print("6. Libras a kilogramos")
    print("0. Salir")


CONVERSIONES: dict[str, tuple[Callable[[float], float], str, str]] = {
    "1": (celsius_a_fahrenheit, "°C", "°F"),
    "2": (fahrenheit_a_celsius, "°F", "°C"),
    "3": (km_a_millas, "km", "mi"),
    "4": (millas_a_km, "mi", "km"),
    "5": (kg_a_libras, "kg", "lb"),
    "6": (libras_a_kg, "lb", "kg"),
}


def main() -> None:
    """Muestra conversiones hasta que el usuario elige salir."""
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (0-6): ").strip()

        if opcion == "0":
            print("Hasta luego.")
            return

        conversion = CONVERSIONES.get(opcion)
        if conversion is None:
            print("Opción no válida")
            continue

        valor = float(input("Valor a convertir: "))
        convertir, unidad_origen, unidad_destino = conversion
        resultado = convertir(valor)
        print(formatear(valor, unidad_origen, resultado, unidad_destino))


if __name__ == "__main__":
    main()
