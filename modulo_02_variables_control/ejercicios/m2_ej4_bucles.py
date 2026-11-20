"""Módulo 2 - Ejercicio 4: bucles."""


def factorial(n: int) -> int:
    """Devuelve el factorial de ``n`` (n >= 0) usando un bucle.

    >>> factorial(5), factorial(0)
    (120, 1)
    """
    resultado = 1
    for numero in range(1, n + 1):
        resultado *= numero
    return resultado


def es_primo(n: int) -> bool:
    """Indica si ``n`` es un número primo.

    >>> es_primo(13), es_primo(15), es_primo(1)
    (True, False, False)
    """
    if n < 2:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True


def invertir(texto: str) -> str:
    """Devuelve ``texto`` del revés usando un bucle.

    >>> invertir("Python")
    'nohtyP'
    """
    resultado = ""
    for letra in texto:
        resultado = letra + resultado
    return resultado

def contar_vocales(texto: str) -> int:
    """Cuenta las vocales de ``texto``, sin distinguir mayúsculas ni tildes.

    >>> contar_vocales("Programación")
    5
    """
    texto = texto.lower()
    VOCALES = "aeiouáéíóúü"
    contador = 0
    for letra in texto:
        if letra in VOCALES:
            contador += 1
    return contador

def suma_digitos(numero: int) -> int:
    """Suma los dígitos de un entero, ignorando el signo. Usa un while.

    >>> suma_digitos(1234), suma_digitos(-905)
    (10, 14)
    """
    numero = abs(numero)
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma


def fizzbuzz(n: int) -> str:
    """Devuelve la secuencia FizzBuzz de 1 a ``n`` separada por espacios.

    Los múltiplos de 3 se sustituyen por "Fizz", los de 5 por "Buzz" y los de
    ambos por "FizzBuzz".

    >>> fizzbuzz(5)
    '1 2 Fizz 4 Buzz'
    """
    elementos = []
    for numero in range(1, n + 1):
        if numero % 15 == 0:
            elementos.append("FizzBuzz")
        elif numero % 3 == 0:
            elementos.append("Fizz")
        elif numero % 5 == 0:
            elementos.append("Buzz")
        else:
            elementos.append(str(numero))
    return " ".join(elementos)


def tabla_multiplicar(numero: int) -> str:
    """Devuelve la tabla de multiplicar del 1 al 10, una línea por producto.

    >>> print(tabla_multiplicar(7).splitlines()[2])
    7 x  3 =  21
    """
    lineas = []
    for i in range(1, 11):
        producto = numero * i
        lineas.append(f"{numero} x {i:2d} = {producto:3d}")
    return "\n".join(lineas)

def primer_multiplo_comun(a: int, b: int) -> int:
    """Devuelve el mínimo común múltiplo de dos enteros positivos con un while.

    >>> primer_multiplo_comun(4, 6)
    12
    """
    multiplo = max(a, b)
    while multiplo % a != 0 or multiplo % b != 0:
        multiplo += 1
    return multiplo
