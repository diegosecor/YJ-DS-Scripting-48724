"""
Sistema de EJEMPLO: lineas paralelas segun el tono y la direccion.

No es un sistema final; sirve para probar que el contrato funciona
de punta a punta (celdas -> lineas -> Grasshopper -> botella).
Usarlo como plantilla para los sistemas reales.
"""

import math

from . import register
from config import MIN_SPACING


@register("parallel")
def parallel(cell, max_spacing=6.0, **_):
    # tono alto (oscuro) = lineas mas juntas
    spacing = max_spacing - cell.tone * (max_spacing - MIN_SPACING)
    if cell.tone < 0.05:
        return []

    cx, cy = cell.center()
    x0, y0, x1, y1 = cell.bbox()
    radius = math.hypot(x1 - x0, y1 - y0) / 2.0
    a = cell.direction
    dx, dy = math.cos(a), math.sin(a)        # direccion de las lineas
    nx, ny = -dy, dx                         # normal

    lines = []
    n = int(radius // spacing)
    for k in range(-n, n + 1):
        ox, oy = cx + nx * k * spacing, cy + ny * k * spacing
        p = (ox - dx * radius, oy - dy * radius)
        q = (ox + dx * radius, oy + dy * radius)
        seg = clip_segment_to_box(p, q, x0, y0, x1, y1)
        if seg:
            lines.append(seg)
    return lines


def clip_segment_to_box(p, q, x0, y0, x1, y1):
    """Recorte Liang-Barsky de un segmento contra un rectangulo."""
    (px, py), (qx, qy) = p, q
    dx, dy = qx - px, qy - py
    t0, t1 = 0.0, 1.0
    for pk, qk in ((-dx, px - x0), (dx, x1 - px), (-dy, py - y0), (dy, y1 - py)):
        if pk == 0:
            if qk < 0:
                return None
        else:
            t = qk / pk
            if pk < 0:
                t0 = max(t0, t)
            else:
                t1 = min(t1, t)
    if t0 >= t1:
        return None
    return [(px + dx * t0, py + dy * t0), (px + dx * t1, py + dy * t1)]
