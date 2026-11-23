"""Módulo 3 - Ejemplo 6: mirada de datos.

Las funciones son valores: se pueden pasar a otra función para decirle
qué cálculo aplicar. Es la idea que hay detrás de ``agg`` y ``apply`` en pandas.
"""

import statistics

IMPORTES = [120.0, 80.5, 310.0, 95.0, 150.25]


def rango(valores):
    """Devuelve la diferencia entre el mayor y el menor."""
    return max(valores) - min(valores)


def resumen(valores, *funciones):
    """Aplica cada función a los valores.

    Devuelve un diccionario que asocia el nombre de cada función con su
    resultado, redondeado a dos decimales.
    """
    resultado = {}
    for funcion in funciones:
        resultado[funcion.__name__] = round(funcion(valores), 2)
    return resultado


def normalizar(valores, *, referencia=None):
    """Devuelve cada valor dividido entre la referencia (por defecto, el máximo)."""
    referencia = referencia or max(valores)
    return [round(valor / referencia, 3) for valor in valores]


def main():
    # --- Funciones propias, integradas y de la librería estándar, todas como argumentos
    print(resumen(IMPORTES, min, max, statistics.mean, statistics.median, rango))

    # --- Una lambda como criterio: los dos importes más cercanos a la media
    media = statistics.mean(IMPORTES)
    print(sorted(IMPORTES, key=lambda importe: abs(importe - media))[:2])

    # --- Un parámetro solo por nombre cambia el comportamiento sin cambiar la llamada habitual
    print(normalizar(IMPORTES))
    print(normalizar(IMPORTES, referencia=1000))


if __name__ == "__main__":
    main()
