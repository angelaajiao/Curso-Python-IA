"""Módulo 3 - Ejemplo 1: definición de funciones."""


def precio_con_iva(precio: float, iva: float = 21) -> float:
    """Devuelve el precio con el IVA aplicado.

    ``iva`` es un porcentaje. El resultado se redondea a dos decimales.

    >>> precio_con_iva(100)
    121.0
    """
    return round(precio * (1 + iva / 100), 2)


def saludar(nombre):
    """Imprime un saludo. No devuelve nada."""
    print(f"Hola, {nombre}")


def doble(x):
    return x * 2


def aplicar_dos_veces(funcion, valor):
    """Función de orden superior: recibe otra función como argumento."""
    return funcion(funcion(valor))


def main():
    # --- Llamada y documentación
    print(precio_con_iva(100))
    print(precio_con_iva.__doc__.splitlines()[0]) #imprime el docstring

    # --- return frente a print
    resultado = saludar("Ada")       # imprime...
    print(resultado)                 # ...pero devuelve None

    # --- Las funciones son objetos
    operacion = doble                # sin paréntesis: la función, no su resultado
    print(operacion(5), doble.__name__)

    operaciones = {"doble": doble, "absoluto": abs, "iva": precio_con_iva}
    for nombre, funcion in operaciones.items():
        print(f"{nombre:>10}: {funcion(-50)}")

    print(aplicar_dos_veces(doble, 3))          # 12


if __name__ == "__main__":
    main()

# Los ejemplos >>> del docstring se pueden ejecutar como tests:
#     python -m doctest 01_definicion.py -v
