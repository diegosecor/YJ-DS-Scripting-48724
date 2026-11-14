"""
Catalog of line systems.

Adding a new system:
    1. Create a file in systems/ (e.g. hankin.py)
    2. Write the function with @register("hankin")
    3. Import it in the list of imports below

Usage:
    from systems import SYSTEMS, run
    lines = run("parallel", cell, spacing=2.0)
"""

SYSTEMS = {}


def register(name):
    def deco(fn):
        SYSTEMS[name] = fn
        return fn
    return deco


def run(name, cell, **params):
    if name not in SYSTEMS:
        raise KeyError("System '%s' does not exist. Available: %s" % (name, list(SYSTEMS)))
    return SYSTEMS[name](cell, **params)


# --- register every system here ---
from . import example  # noqa: E402,F401
