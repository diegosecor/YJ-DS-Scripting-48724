"""
Bridge between the code (tuples in mm) and Rhino/Grasshopper.

This is the ONLY file that imports Rhino.

In a Python 3 component in Grasshopper (Rhino 8), paste at the top:

    #! python3
    import sys, os, importlib
    gh_dir = os.path.dirname(ghenv.Component.OnPingDocument().FilePath)
    src = os.path.join(gh_dir, "..", "src")
    if src not in sys.path:
        sys.path.insert(0, src)

    import gh_bridge, systems, testing
    importlib.reload(gh_bridge)   # reloads changes while you code

(The .gh must be saved inside the gh/ folder so the path works on
both computers.)
"""

import Rhino.Geometry as rg


def to_curve(polyline):
    pts = [rg.Point3d(x, y, 0) for x, y in polyline]
    return rg.PolylineCurve(pts)


def to_curves(polylines):
    return [to_curve(p) for p in polylines]


def cells_to_curves(cells):
    return [to_curve(c.polygon) for c in cells]
