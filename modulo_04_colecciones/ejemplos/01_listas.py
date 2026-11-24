"""Módulo 4 - Ejemplo 1: listas."""

import copy

numeros = [4, 8, 15, 16, 23, 42]

# --- Acceso y slicing
print(numeros[0], numeros[-1], numeros[-2])
print(numeros[1:4], numeros[:3], numeros[-2:])
print (numeros)
print (numeros[:])
print(numeros[::2], numeros[::-1])
print(numeros[2:100])                    # un slice nunca da IndexError

# --- Modificación
tareas = ["diseñar", "programar"]
tareas.append("probar")
tareas.insert(0, "analizar")
tareas.extend(["desplegar", "medir"])
print(tareas)
print(tareas.pop(), tareas.pop(0), tareas)

a = [1, 2]
a.append([3, 4])
b = [1, 2]
b.extend([3, 4])
print(a, b)                              # append frente a extend

# --- sort() modifica y devuelve None; sorted() devuelve una lista nueva
desordenados = [23, 4, 42, 8]
print(sorted(desordenados), desordenados)
print(desordenados.sort(), desordenados)

# --- Alias, copia superficial y copia profunda
matriz = [[1, 2], [3, 4]]
alias = matriz
superficial = matriz.copy()
profunda = copy.deepcopy(matriz)
matriz[0].append(99)
matriz.append([5, 6])
print("alias:      ", alias)
print("superficial:", superficial)
print("profunda:   ", profunda)

# --- La trampa de multiplicar listas anidadas
mal = [[0] * 3] * 2
mal[0][0] = 1
bien = [[0] * 3 for _ in range(2)]
bien[0][0] = 1
print(mal, bien)

# --- No se borra mientras se recorre
valores = [1, 2, 2, 3]
for valor in valores:
    if valor == 2:
        valores.remove(valor)
print(valores)                           # [1, 2, 3]: se ha saltado un 2
valores = [valor for valor in [1, 2, 2, 3] if valor != 2]
print(valores)
