"""
Celdas FALSAS para probar sistemas sin esperar la gramatica.

    from testing import fake_cells
    cells = fake_cells(nx=8, ny=6, seed=1)
"""

import math
import random

from config import CANVAS_WIDTH, CANVAS_HEIGHT
from contract import Cell


def fake_cells(nx=8, ny=6, seed=0):
    rnd = random.Random(seed)
    w, h = CANVAS_WIDTH / nx, CANVAS_HEIGHT / ny
    cells = []
    for j in range(ny):
        for i in range(nx):
            x, y = i * w, j * h
            poly = [(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)]
            cells.append(Cell(
                polygon=poly,
                id=j * nx + i,
                tone=rnd.random(),
                direction=rnd.uniform(0, math.pi),
                detail=rnd.random(),
            ))
    return cells
