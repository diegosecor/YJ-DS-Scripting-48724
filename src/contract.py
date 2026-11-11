"""
CONTRATO entre los dos modulos del proyecto.

    Estructura (fields / layers / grammar)  --->  lista de Cell
    Sistemas de lineas (systems/)           --->  recibe Cell, devuelve Polylines

Este archivo es compartido: cambiarlo SOLO de comun acuerdo.

La geometria se guarda como tuplas (x, y) en mm, sin depender de Rhino.
Asi el codigo se puede probar en Python normal; la conversion a curvas
de Rhino se hace en gh_bridge.py.
"""

from dataclasses import dataclass, field
from typing import List, Tuple

Point = Tuple[float, float]
Polyline = List[Point]          # lista de puntos; cerrada si el primero == el ultimo


@dataclass
class Cell:
    polygon: Polyline           # borde cerrado de la celda, en mm
    id: int = 0
    depth: int = 0              # nivel de recursion de la gramatica
    layer: int = 0              # capa a la que pertenece (= marcador)
    tone: float = 0.5           # 0 = blanco, 1 = negro (promedio de la celda)
    direction: float = 0.0      # angulo dominante de la imagen, en radianes
    detail: float = 0.0         # 0..1, cantidad de bordes en la celda
    tags: dict = field(default_factory=dict)  # etiquetas extra de la gramatica

    def bbox(self):
        xs = [p[0] for p in self.polygon]
        ys = [p[1] for p in self.polygon]
        return min(xs), min(ys), max(xs), max(ys)

    def center(self) -> Point:
        x0, y0, x1, y1 = self.bbox()
        return ((x0 + x1) / 2.0, (y0 + y1) / 2.0)


# Firma de todo sistema de lineas:
#
#     def mi_sistema(cell: Cell, **params) -> List[Polyline]
#
# Se registra con @register("nombre") en systems/__init__.py
