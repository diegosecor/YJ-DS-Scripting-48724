"""
Catalogo de sistemas de lineas.

Agregar un sistema nuevo:
    1. Crear un archivo en systems/ (ej. hankin.py)
    2. Escribir la funcion con @register("hankin")
    3. Importarlo abajo en la lista de imports

Uso:
    from systems import SYSTEMS, run
    lineas = run("parallel", cell, spacing=2.0)
"""

SYSTEMS = {}


def register(name):
    def deco(fn):
        SYSTEMS[name] = fn
        return fn
    return deco


def run(name, cell, **params):
    if name not in SYSTEMS:
        raise KeyError("Sistema '%s' no existe. Disponibles: %s" % (name, list(SYSTEMS)))
    return SYSTEMS[name](cell, **params)


# --- registrar aqui cada sistema ---
from . import example  # noqa: E402,F401
