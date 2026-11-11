"""
Puente entre el codigo (tuplas en mm) y Rhino/Grasshopper.

Este es el UNICO archivo que importa Rhino.

En un componente Python 3 de Grasshopper (Rhino 8), pegar al inicio:

    #! python3
    import sys, os, importlib
    gh_dir = os.path.dirname(ghenv.Component.OnPingDocument().FilePath)
    src = os.path.join(gh_dir, "..", "src")
    if src not in sys.path:
        sys.path.insert(0, src)

    import gh_bridge, systems, testing
    importlib.reload(gh_bridge)   # recarga cambios mientras programan

(El .gh tiene que estar guardado dentro de la carpeta gh/ para que la ruta funcione
en ambos computadores.)
"""

import Rhino.Geometry as rg


def to_curve(polyline):
    pts = [rg.Point3d(x, y, 0) for x, y in polyline]
    return rg.PolylineCurve(pts)


def to_curves(polylines):
    return [to_curve(p) for p in polylines]


def cells_to_curves(cells):
    return [to_curve(c.polygon) for c in cells]
