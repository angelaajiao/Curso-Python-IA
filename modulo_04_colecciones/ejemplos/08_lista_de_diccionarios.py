"""Módulo 4 - Ejemplo 8: buscar, filtrar, ordenar y agrupar registros."""

from collections import defaultdict
from operator import itemgetter

empleados = [
    {"nombre": "Ada", "departamento": "IT", "salario": 52000},
    {"nombre": "Linus", "departamento": "IT", "salario": 48000},
    {"nombre": "Grace", "departamento": "Ventas", "salario": 45000},
    {"nombre": "Alan", "departamento": "Ventas", "salario": 39000},
    {"nombre": "Guido", "departamento": "IT", "salario": 48000},
]

# --- Buscar
ada = next((e for e in empleados if e["nombre"] == "Ada"), None)
nadie = next((e for e in empleados if e["nombre"] == "Zoe"), None)
print(ada, nadie)

por_nombre = {e["nombre"]: e for e in empleados}          # índice
print(por_nombre["Grace"]["salario"])

# --- Filtrar y proyectar
print([e["nombre"] for e in empleados if e["departamento"] == "IT"])
print([e["nombre"] for e in empleados if e["salario"] > 45000])

# --- Ordenar
for e in sorted(empleados, key=itemgetter("salario"), reverse=True)[:3]:
    print(f"{e['nombre']:<8}{e['salario']:>8}")

# Departamento ascendente y, dentro, salario descendente y nombre ascendente
orden = sorted(empleados, key=lambda e: (e["departamento"], -e["salario"], e["nombre"]))
print([e["nombre"] for e in orden])

# --- Agrupar y resumir
masa_salarial = defaultdict(int)
plantilla = defaultdict(list)
for e in empleados:
    masa_salarial[e["departamento"]] += e["salario"]
    plantilla[e["departamento"]].append(e["nombre"])

print(dict(masa_salarial))
print(dict(plantilla))
print({dep: round(masa_salarial[dep] / len(nombres)) for dep, nombres in plantilla.items()})

# --- Informe
print(f"{'Departamento':<14}{'Personas':>9}{'Masa salarial':>15}")
for departamento in sorted(masa_salarial):
    personas = len(plantilla[departamento])
    print(f"{departamento:<14}{personas:>9}{masa_salarial[departamento]:>15,}")

# Traduzco una consulta SQL a Python:
# SELECT nombre FROM empleados
# WHERE departamento = 'IT'
# ORDER BY salario DESC, nombre
# LIMIT 2;


de_it = [e for e in empleados if e["departamento"] == "IT"]
orden = sorted(de_it, key=lambda e: (-e["salario"], e["nombre"]))
print([e["nombre"] for e in orden[:2]])




it_top2 = sorted(
    (e for e in empleados if e["departamento"] == "IT"),
    key=lambda e: (-e["salario"], e["nombre"])
)[:2]
print([e["nombre"] for e in it_top2])