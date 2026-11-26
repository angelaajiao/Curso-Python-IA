class Empleado:
    def __init__(self, nombre): self.nombre = nombre
    def saludar(self): return f"Hola, soy {self.nombre}"

ada = Empleado("Ada")
ada.saludar()
Empleado.saludar(ada)            # lo mismo
ada.__dict__
ada.departamento = "IT"          # ¿compila? ¿debería?

print(ada.saludar())
print(ada.__dict__)
print(ada.departamento)
print(Empleado.__dict__)
print(hasattr(ada, "departamento"))  # True
print(hasattr(Empleado, "departamento"))  # False
print(getattr(ada, "departamento", None))  # IT
print(getattr(Empleado, "departamento", None))  # None  