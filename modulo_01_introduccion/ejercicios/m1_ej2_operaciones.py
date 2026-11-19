"""Módulo 1 - Ejercicio 2: operaciones con dos números."""

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
    division_entera = a // b
    return division_entera


def resto(a, b):
    """Devuelve el resto de dividir a entre b."""
    resto = a % b
    return resto


def potencia(a, b):
    """Devuelve a elevado a b."""
    potencia = a**b
    return potencia
    


def resumen(a, b):
    """Devuelve todas las operaciones en una sola cadena.

    >>> resumen(7, 2)
    '7 + 2 = 9 | 7 - 2 = 5 | 7 * 2 = 14 | 7 / 2 = 3.50 | 7 // 2 = 3 | 7 % 2 = 1 | 7 ** 2 = 49'
    """
    return f"{a} + {b} = {sumar(a,b)} | {a} - {b} = {restar(a,b)} | {a} * {b} = {multiplicar(a,b)} | {a} / {b} = {dividir(a,b):.2f} | {a} // {b} = {division_entera(a,b)} | {a} % {b} = {resto(a,b)} | {a} ** {b} = {potencia(a,b)}"


def main():
    """Pide dos números enteros por teclado e imprime el resumen."""
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))

    while b==0:
        print("El segundo número no puede ser 0")
        b = int(input("Introduce el segundo número: "))

    print(resumen(a, b))


if __name__ == "__main__":
    main()
