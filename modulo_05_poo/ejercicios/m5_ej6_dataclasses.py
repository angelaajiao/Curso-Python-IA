"""Módulo 5 - Ejercicio 6: dataclasses y composición.

En este ejercicio las clases se escriben enteras: no hay plantilla. El
enunciado está en ejercicios/README.md.
"""

from dataclasses import dataclass, field
import math

# TODO: escribe aquí las dataclasses Punto, LineaPedido y Pedido
@dataclass(frozen=True)
class Punto:
    """Un punto inmutable del plano."""

    x: float = 0.0
    y: float = 0.0

    def distancia(self, otro: "Punto") -> float:
        """Distancia entre los dos puntos, redondeada a dos decimales.

        >>> Punto().distancia(Punto(3, 4))
        5.0
        """
        return round(math.hypot(self.x - otro.x, self.y - otro.y), 2)


@dataclass
class LineaPedido:
    """Una línea de un pedido: un producto, sus unidades y su precio."""

    producto: str
    unidades: int
    precio: float

    def __post_init__(self):
        if self.unidades <= 0:
            raise ValueError("Las unidades tienen que ser positivas")

    @property
    def importe(self) -> float:
        """Unidades por precio, con dos decimales."""
        return round(self.unidades * self.precio, 2)


@dataclass
class Pedido:
    """Un pedido de un cliente, compuesto por líneas de pedido.

    >>> pedido = Pedido(1042, "Ada")
    >>> pedido.anadir("Teclado", 2, 45.0)
    LineaPedido(producto='Teclado', unidades=2, precio=45.0)
    >>> pedido.anadir("Ratón", 1, 19.9)
    LineaPedido(producto='Ratón', unidades=1, precio=19.9)
    >>> pedido.total, len(pedido), pedido.productos()
    (109.9, 2, ['Ratón', 'Teclado'])
    """

    numero: int
    cliente: str
    lineas: list[LineaPedido] = field(default_factory=list)

    def anadir(self, producto: str, unidades: int, precio: float) -> LineaPedido:
        """Crea una línea, la añade al pedido y la devuelve."""
        linea = LineaPedido(producto, unidades, precio)
        self.lineas.append(linea)
        return linea

    @property
    def total(self) -> float:
        """Suma de los importes de las líneas, con dos decimales."""
        return round(sum(linea.importe for linea in self.lineas), 2)

    def __len__(self) -> int:
        return len(self.lineas)

    def productos(self) -> list[str]:
        """Nombres de los productos, sin repetir y en orden alfabético."""
        return sorted({linea.producto for linea in self.lineas})