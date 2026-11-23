def sumar(elementos):
    total = 0
    for elemento in elementos:
        total += elemento
    return total

elementos = [1, 2, 3, 4, 5]
print(sumar(elementos))


# Tu lista se puede entregar de dos formas:
#
# 1. Como una sola caja que contiene todos los números.
def mostrar_lista_completa(elementos):
    print("Sin *: elementos es", elementos)
    print("Contiene:", len(elementos), "números")


# 2. Como números separados.
def mostrar_argumentos_separados(*elementos):
    print("Con *: elementos es", elementos)
    print("Contiene:", len(elementos), "argumentos separados")


mostrar_lista_completa(elementos)
mostrar_argumentos_separados(*elementos)

# mostrar_lista_completa(elementos):
# -> La función recibe directamente [1, 2, 3, 4, 5].
#
# mostrar_argumentos_separados(*elementos):
# -> El * abre la lista, así que es equivalente a:
#    mostrar_argumentos_separados(1, 2, 3, 4, 5)
#
# -> Dentro de la función, el * vuelve a agruparlos en esta tupla:
#    (1, 2, 3, 4, 5)


# **kwargs permite recibir una cantidad variable de argumentos con nombre.
def mostrar_kwargs(**kwargs):
    print("\nCon **kwargs: los datos se reciben como un diccionario")
    print("kwargs =", kwargs)

    for clave, valor in kwargs.items():
        print("Clave:", clave, "| Valor:", valor)


mostrar_kwargs(nombre="Ana", edad=25, ciudad="Madrid")

# Esta llamada:
# mostrar_kwargs(nombre="Ana", edad=25, ciudad="Madrid")
#
# equivale a recibir:
# kwargs = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}


# ** también se puede utilizar al llamar a una función.
def mostrar_persona(nombre, edad, ciudad):
    print("\nCon un diccionario desempaquetado mediante **")
    print(nombre, "tiene", edad, "años y vive en", ciudad)


persona = {
    "nombre": "Luis",
    "edad": 32,
    "ciudad": "Sevilla",
}

mostrar_persona(**persona)

# mostrar_persona(**persona) es equivalente a:
# mostrar_persona(nombre="Luis", edad=32, ciudad="Sevilla")

