"""Módulo 2 - Ejercicio 3: condicionales. SOLUCIÓN."""


def calificacion(nota: float) -> str:
    """Traduce una nota de 0 a 10 a su calificación.

    Menos de 5 "Suspenso", de 5 a menos de 7 "Aprobado", de 7 a menos de 9
    "Notable" y de 9 a 10 "Sobresaliente". Fuera de rango, "Nota no válida".

    >>> calificacion(7.5)
    'Notable'
    """
    # Guarda para el caso inválido y luego ramas de mayor a menor: así cada
    # condición solo necesita un límite.
    if not 0 <= nota <= 10:
        return "Nota no válida"
    if nota >= 9:
        return "Sobresaliente"
    if nota >= 7:
        return "Notable"
    if nota >= 5:
        return "Aprobado"
    return "Suspenso"


def precio_entrada(edad: int, es_festivo: bool = False) -> float:
    """Calcula el precio de una entrada de cine.

    Menores de 4 años: gratis. De 4 a 12: 5 €. De 13 a 64: 9 €. Desde 65: 6 €.
    En festivo se suma un recargo de 2 € a las entradas de pago.

    >>> precio_entrada(30), precio_entrada(30, es_festivo=True), precio_entrada(2, True)
    (9, 11, 0)
    """
    if edad < 4:
        return 0
    if edad <= 12:
        precio = 5
    elif edad < 65:
        precio = 9
    else:
        precio = 6
    return precio + 2 if es_festivo else precio


def describir_http(codigo: int) -> str:
    """Describe un código de estado HTTP.

    200 "Correcto", 201 "Creado", 301 y 302 "Redirección", 400 "Petición
    incorrecta", 401 y 403 "Sin autorización", 404 "No encontrado", cualquier
    otro entre 500 y 599 "Error del servidor" y el resto "Desconocido".

    >>> describir_http(302), describir_http(503)
    ('Redirección', 'Error del servidor')
    """
    match codigo:
        case 200:
            return "Correcto"
        case 201:
            return "Creado"
        case 301 | 302:
            return "Redirección"
        case 400:
            return "Petición incorrecta"
        case 401 | 403:
            return "Sin autorización"
        case 404:
            return "No encontrado"
        # Un patrón puede llevar una condición adicional con if (guarda).
        case _ if 500 <= codigo <= 599:
            return "Error del servidor"
        case _:
            return "Desconocido"


def mayor_de_tres(a: float, b: float, c: float) -> float:
    """Devuelve el mayor de tres números sin usar max().

    >>> mayor_de_tres(3, 9, 5)
    9
    """
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor


def tipo_triangulo(a: float, b: float, c: float) -> str:
    """Clasifica un triángulo por sus lados.

    Devuelve "no es un triángulo" si algún lado no es positivo o si no se
    cumple la desigualdad triangular; si no, "equilátero", "isósceles" o
    "escaleno".

    >>> tipo_triangulo(3, 3, 3), tipo_triangulo(3, 4, 5), tipo_triangulo(1, 2, 3)
    ('equilátero', 'escaleno', 'no es un triángulo')
    """
    if min(a, b, c) <= 0 or a + b <= c or a + c <= b or b + c <= a:
        return "no es un triángulo"
    if a == b == c:
        return "equilátero"
    if a == b or a == c or b == c:
        return "isósceles"
    return "escaleno"
