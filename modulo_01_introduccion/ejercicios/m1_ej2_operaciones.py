"""Módulo 1 - Ejercicio 2: operaciones con dos números. SOLUCIÓN."""

def sumar(a, b):
    """Devuelve a + b."""
<<<<<<< HEAD
    suma = a + b
    return suma
=======
    return a + b
>>>>>>> c67e6ab911f0511b15210cc127f0d3c5623470b5


def restar(a, b):
    """Devuelve a - b."""
<<<<<<< HEAD
    resta = a - b
    return resta
=======
    return a - b
>>>>>>> c67e6ab911f0511b15210cc127f0d3c5623470b5


def multiplicar(a, b):
    """Devuelve a * b."""
<<<<<<< HEAD
    multiplicacion = a * b
    return multiplicacion
=======
    return a * b
>>>>>>> c67e6ab911f0511b15210cc127f0d3c5623470b5


def dividir(a, b):
    """Devuelve la división real de a entre b (siempre un float)."""
<<<<<<< HEAD
    division = a / b
    return division
=======
    # En Python 3, / devuelve float aunque la división sea exacta: 8 / 2 == 4.0
    return a / b
>>>>>>> c67e6ab911f0511b15210cc127f0d3c5623470b5


def division_entera(a, b):
    """Devuelve el cociente entero de a entre b."""
<<<<<<< HEAD
    division_entera = a // b
    return division_entera
=======
    # // redondea hacia abajo, no hacia cero: -7 // 2 == -4 (en Java es -3).
    return a // b
>>>>>>> c67e6ab911f0511b15210cc127f0d3c5623470b5


def resto(a, b):
    """Devuelve el resto de dividir a entre b."""
<<<<<<< HEAD
    resto = a % b
    return resto
=======
    # El resto tiene el signo del divisor: -7 % 2 == 1 (en Java es -1).
    return a % b
>>>>>>> c67e6ab911f0511b15210cc127f0d3c5623470b5


def potencia(a, b):
    """Devuelve a elevado a b."""
<<<<<<< HEAD
    potencia = a**b
    return potencia
    
=======
    # ** es el operador de potencia. Ojo: ^ es el XOR a nivel de bits.
    return a**b
>>>>>>> c67e6ab911f0511b15210cc127f0d3c5623470b5


def resumen(a, b):
    """Devuelve todas las operaciones en una sola cadena.

    >>> resumen(7, 2)
    '7 + 2 = 9 | 7 - 2 = 5 | 7 * 2 = 14 | 7 / 2 = 3.50 | 7 // 2 = 3 | 7 % 2 = 1 | 7 ** 2 = 49'
    """
<<<<<<< HEAD
    return f"{a} + {b} = {sumar(a,b)} | {a} - {b} = {restar(a,b)} | {a} * {b} = {multiplicar(a,b)} | {a} / {b} = {dividir(a,b):.2f} | {a} // {b} = {division_entera(a,b)} | {a} % {b} = {resto(a,b)} | {a} ** {b} = {potencia(a,b)}"
=======
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
>>>>>>> c67e6ab911f0511b15210cc127f0d3c5623470b5


def main():
    """Pide dos números enteros por teclado e imprime el resumen."""
<<<<<<< HEAD
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))

    while b==0:
        print("El segundo número no puede ser 0")
        b = int(input("Introduce el segundo número: "))

=======
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
>>>>>>> c67e6ab911f0511b15210cc127f0d3c5623470b5
    print(resumen(a, b))


if __name__ == "__main__":
    main()
