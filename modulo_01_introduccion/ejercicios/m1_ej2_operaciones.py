"""Módulo 1 - Ejercicio 2: operaciones con dos números. SOLUCIÓN."""

def sumar(a, b):
    """Devuelve a + b."""
    suma = a + b
    return suma


def restar(a, b):
    """Devuelve a - b."""
    resta = a - b
    return resta


def multiplicar(a, b):
    """Devuelve a * b."""
    multiplicacion = a * b
    return multiplicacion


def dividir(a, b):
    """Devuelve la división real de a entre b (siempre un float)."""
    division = a / b
    return division


def division_entera(a, b):
    """Devuelve el cociente entero de a entre b."""
    # // redondea hacia abajo, no hacia cero: -7 // 2 == -4 (en Java es -3).
    return a // b


def resto(a, b):
    """Devuelve el resto de dividir a entre b."""
    # El resto tiene el signo del divisor: -7 % 2 == 1 (en Java es -1).
    return a % b


def potencia(a, b):
    """Devuelve a elevado a b."""
    # ** es el operador de potencia. Ojo: ^ es el XOR a nivel de bits.
    return a**b


def resumen(a, b):
    """Devuelve todas las operaciones en una sola cadena.

    >>> resumen(7, 2)
    '7 + 2 = 9 | 7 - 2 = 5 | 7 * 2 = 14 | 7 / 2 = 3.50 | 7 // 2 = 3 | 7 % 2 = 1 | 7 ** 2 = 49'
    """
    partes = [
        f"{a} + {b} = {sumar(a, b)}",
        f"{a} - {b} = {restar(a, b)}",
        f"{a} * {b} = {multiplicar(a, b)}",
        f"{a} / {b} = {dividir(a, b):.2f}",
        f"{a} // {b} = {division_entera(a, b)}",
        f"{a} % {b} = {resto(a, b)}",
        f"{a} ** {b} = {potencia(a, b)}",
    ]
    # join() une una lista de cadenas con el separador indicado. Las listas se
    # ven en el módulo 4; en el módulo 1 también es válido concatenar las siete
    # f-strings con " | " a mano.
    return " | ".join(partes)


def main():
    """Pide dos números enteros por teclado e imprime el resumen."""
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    print(resumen(a, b))


if __name__ == "__main__":
    main()
