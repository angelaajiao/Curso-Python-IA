"""Módulo 5 - Ejercicio 6: dataclasses y composición.

En este ejercicio las clases se escriben enteras: no hay plantilla. El
enunciado está en ejercicios/README.md.
"""

from dataclasses import dataclass, field
from math import hypot


@dataclass(frozen=True)
class Punto:
    """Un punto inmutable del plano."""

    x: float = 0.0
    y: float = 0.0

    def distancia(self, otro: "Punto") -> float:
        return round(((self.x - otro.x) ** 2 + (self.y - otro.y) ** 2) ** 0.5, 2)


@dataclass
class LineaPedido:
    """Una línea de un pedido."""

    producto: str
    unidades: int
    precio: float

    def __post_init__(self):
        if self.unidades <= 0:
            raise ValueError("Las unidades deben ser positivas")

    @property
    def importe(self) -> float:
        return round(self.unidades * self.precio, 2)


@dataclass
class Pedido:
    """Un pedido compuesto por líneas."""

    numero: int
    cliente: str
    lineas: list[LineaPedido] = field(default_factory=list)

    def anadir(self, producto: str, unidades: int, precio: float) -> LineaPedido:
        linea = LineaPedido(producto, unidades, precio)
        self.lineas.append(linea)
        return linea

    @property
    def total(self) -> float:
        return round(sum(linea.importe for linea in self.lineas), 2)

    def __len__(self) -> int:
        return len(self.lineas)

    def productos(self) -> list[str]:
        return sorted({linea.producto for linea in self.lineas})
