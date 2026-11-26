class Animal:
    def hablar(self):
        print("El animal hace un sonido")

class Volador:
    def volar(self):
        print("Puedo volar")

class Pajaro(Animal, Volador):
    pass

Piolin = Pajaro()

Piolin.hablar()
Piolin.volar()

# Clase padre
class A:
    def saludar(self):
        print("Esto es un Método de A")

# Primer nivel de herencia
class B(A):
    def saludar(self):
        print("Esto es un Método de B")
        super().saludar()

class C(A):
    def saludar(self):
        print("Esto es un Método de C")
        super().saludar()

class D(B, C):
    def saludar(self):
        print("Esto es un Método de D")
        super().saludar()

d = D()
d.saludar()

print(D.mro())



