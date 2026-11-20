"""Módulo 1 - Ejercicio 1: saludo. SOLUCIÓN."""


def saludar(nombre):
    """Devuelve un saludo de bienvenida para ``nombre``.

    >>> saludar("  ada lovelace ")
    'Hola, Ada Lovelace. ¡Te damos la bienvenida al curso!'
    """
    # strip() quita los espacios de los extremos y title() pone en mayúscula
    # la inicial de cada palabra. Los métodos de str se pueden encadenar
    # porque cada uno devuelve una cadena nueva (las cadenas son inmutables).
    nombre_limpio = nombre.strip().title()

    # Una cadena vacía se evalúa como False. Es la forma idiomática de
    # comprobarlo, en lugar de len(nombre_limpio) == 0.
    if not nombre_limpio:
        nombre_limpio = "Anónimo"

    return f"Hola, {nombre_limpio}. ¡Te damos la bienvenida al curso!"


def main():
    """Pide el nombre por teclado e imprime el saludo."""
    nombre = input("¿Cómo te llamas? ")
    print(saludar(nombre))


if __name__ == "__main__":
    main()
