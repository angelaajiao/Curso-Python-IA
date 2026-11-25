"""Módulo 5 - Ejemplo 3: herencia, clases abstractas y mixins."""

import math
from abc import ABC, abstractmethod


class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def salario_mensual(self):
        return round(self.salario / 12, 2)

    def descripcion(self):
        return f"{self.nombre} ({type(self).__name__}): {self.salario_mensual():.2f} €/mes"


class Comercial(Empleado):
    def __init__(self, nombre, salario, comision):
        super().__init__(nombre, salario)        # inicializa la parte heredada
        self.comision = comision

    def salario_mensual(self):                   # sobrescritura que reutiliza la base
        return round(super().salario_mensual() + self.comision, 2)


class Becario(Empleado):
    """No necesita __init__ propio: lo hereda."""

    def salario_mensual(self):
        return round(self.salario / 12 * 0.6, 2)


class ConSuper(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)             # MAL: no llama a super().__init__
        
    def __len__(self):
        return len(self.nombre)

class SinSuper(Empleado):
    def __init__(self, nombre):                  # MAL: no llama a super().__init__
        self.alias = nombre


class Figura(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def area(self):
        """Devuelve el área de la figura."""

    def descripcion(self):
        return f"{self.nombre} de área {self.area():.2f}"


class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado

    def area(self):
        return self.lado ** 2


class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


class Registrable:
    """Mixin: aporta una capacidad y no tiene estado propio."""

    def registrar(self, mensaje):
        return f"[{type(self).__name__}] {mensaje}"


class Serializable:
    def a_diccionario(self):
        return dict(self.__dict__)


class Pedido(Registrable, Serializable):
    def __init__(self, numero, importe):
        self.numero = numero
        self.importe = importe


def main():
    pepe = ConSuper("Pepe", 45000)
    print(len(pepe))

    print(pepe.descripcion())

    manolo = ConSuper("Manolo", 45000)

    print(manolo.descripcion())


    plantilla = [Empleado("Ada", 52000), Comercial("Grace", 36000, 400), Becario("Alan", 18000), ConSuper("Pepe", 45000)]



    for persona in plantilla:
        print(persona.descripcion())

    grace = plantilla[1]
    print(isinstance(grace, Empleado), isinstance(grace, Comercial), issubclass(Becario, Empleado))

    try:
        ConSuper("Pepe", 45000).salario_mensual()
    except AttributeError as error:
        print("AttributeError:", error)

    try:
        Figura("genérica")
    except TypeError as error:
        print("TypeError:", error)

    for figura in (Cuadrado(2), Circulo(1)):
        print(figura.descripcion())

    pedido = Pedido(1042, 199.9)
    print(pedido.registrar("creado"), pedido.a_diccionario())
    print([clase.__name__ for clase in Pedido.__mro__])


if __name__ == "__main__":
    main()
