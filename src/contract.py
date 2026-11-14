"""
CONTRACT between the two modules of the project.

    Pattern generation (fields / layers / grammar)  --->  list of Cell
    Line systems (systems/)                         --->  take a Cell, return Polylines
    Fabrication                                     --->  takes Polylines, maps them to the bottle

This file is shared: change it ONLY by mutual agreement.

Geometry is stored as (x, y) tuples in mm, with no Rhino dependency.
That way the code can be tested in plain Python; the conversion to Rhino
curves happens in gh_bridge.py.
"""

from dataclasses import dataclass, field
from typing import List, Tuple

Point = Tuple[float, float]
Polyline = List[Point]          # list of points; closed if first == last


@dataclass
class Cell:
    polygon: Polyline           # closed boundary of the cell, in mm
    id: int = 0
    depth: int = 0              # recursion level of the grammar
    layer: int = 0              # layer it belongs to (= marker)
    tone: float = 0.5           # 0 = white, 1 = black (cell average)
    direction: float = 0.0      # dominant image direction, in radians
    detail: float = 0.0         # 0..1, amount of edges in the cell
    tags: dict = field(default_factory=dict)  # extra grammar labels

    def bbox(self):
        xs = [p[0] for p in self.polygon]
        ys = [p[1] for p in self.polygon]
        return min(xs), min(ys), max(xs), max(ys)

    def center(self) -> Point:
        x0, y0, x1, y1 = self.bbox()
        return ((x0 + x1) / 2.0, (y0 + y1) / 2.0)


# Signature of every line system:
#
#     def my_system(cell: Cell, **params) -> List[Polyline]
#
# Registered with @register("name") in systems/__init__.py
