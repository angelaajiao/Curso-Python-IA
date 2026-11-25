"""Módulo 5 - Ejemplo 5: convenciones de privacidad y propiedades."""


class Producto:
    IVA = 21

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio                 # pasa por el setter: valida desde el principio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor                 # con guion bajo; self.precio sería recursión infinita

    @property
    def precio_con_iva(self):               # calculada y de solo lectura
        return round(self._precio * (1 + self.IVA / 100), 2)

    def __repr__(self):
        return f"Producto({self.nombre!r}, {self.precio!r})"


class Cuenta:
    def __init__(self, titular):
        self.titular = titular
        self._saldo = 0.0
        self._movimientos = []
        self.__pin = "1234"                  # Python lo renombra a _Cuenta__pin

    @property
    def saldo(self):
        return self._saldo

    @property
    def movimientos(self):
        return tuple(self._movimientos)      # copia inmutable del estado interno

    def ingresar(self, importe):
        if importe <= 0:
            raise ValueError("El importe debe ser positivo")
        self._saldo += importe
        self._movimientos.append(importe)

    def retirar(self, importe):
        if importe <= 0:
            raise ValueError("El importe debe ser positivo")
        if importe > self._saldo:
            raise ValueError("Saldo insuficiente")
        self._saldo -= importe
        self._movimientos.append(-importe)


def main():
    teclado = Producto("Teclado", 45.0)
    teclado.precio = 59.0                    # sintaxis de atributo; ejecuta el setter
    print(teclado, teclado.precio, teclado.precio_con_iva)

    try:
        teclado.precio = -1
    except ValueError as error:
        print("ValueError:", error)

    try:
        teclado.precio_con_iva = 10          # sin setter no se puede asignar
    except AttributeError as error:
        print("AttributeError:", error)

    try:
        Producto("Ratón", -5)                # el constructor también valida
    except ValueError as error:
        print("ValueError:", error)

    cuenta = Cuenta("Ada")
    cuenta.ingresar(100)
    cuenta.retirar(30)
    print(cuenta.saldo, cuenta.movimientos)

    try:
        cuenta.saldo = 1_000_000             # sin setter no se puede asignar
    except AttributeError as error:
        print("AttributeError:", error)

    try:
        cuenta.retirar(500)
    except ValueError as error:
        print("ValueError:", error)

    # --- El guion bajo es un aviso, no un candado
    cuenta._saldo = 1_000_000                # funciona; quien lo hace sabe que no debe
    print(cuenta.saldo)
    print(hasattr(cuenta, "__pin"), cuenta._Cuenta__pin)


if __name__ == "__main__":
    main()
