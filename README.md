# Bottle Pattern Grammar

**Equipo:** YJ&DS SCRIPTING (48-724) — `YJ-DS-Scripting-48724` — Yewon Jang & Diego Serna
**Curso:** 48-724 Scripting and Parametric Design, CMU, Fall 2026

Plugin de Grasshopper que convierte una imagen en patrones generados por una
**shape grammar**, usando **solo líneas**, para que un brazo robótico ABB los
dibuje con marcador sobre la superficie curva de una botella.

```
Imagen → Campos → Capas → Gramática de subdivisión → Sistemas de líneas → Proyección a botella → RobotStudio
```

---

## División del trabajo

| Módulo | Archivos | Responsable |
|---|---|---|
| **Estructura** (campos, capas, gramática) | `src/fields.py`, `src/layers.py`, `src/grammar.py`, `gh/A_estructura.gh` | _(nombre)_ |
| **Sistemas de líneas** (Hankin + weaving, Hilbert/streamlines, glifos) | `src/systems/*`, `gh/B_sistemas.gh` | _(nombre)_ |
| **Integración** (proyección, robot) | `gh/MAIN.gh` | ambos, uno a la vez |
| **Compartidos** (cambiar solo de común acuerdo) | `src/contract.py`, `src/config.py` | ambos |

## El contrato

- La **Estructura** entrega una lista de `Cell` (ver `src/contract.py`):
  polígono en mm + `tone`, `direction`, `detail`, `layer`, `depth`.
- Cada **sistema** es una función `sistema(cell, **params) -> lista de polilíneas`.
- Todo es 2D, en **mm**, dentro del rectángulo de la botella desenrollada
  (`src/config.py`). `x = 0` es la costura.
- Para probar sistemas sin la gramática: `testing.fake_cells()`.

## Estructura de carpetas

```
src/            código Python (aquí vive la lógica)
  systems/      catálogo de sistemas de líneas
gh/             definiciones de Grasshopper (solo cargan el código de src/)
docs/           investigación, reglas de la gramática, presentación
test_images/    imágenes de prueba
outputs/        renders y test prints (videos pesados → OneDrive, no GitHub)
```

## Usar el código en Grasshopper (Rhino 8)

En un componente **Python 3**, al inicio:

```python
#! python3
import sys, os, importlib
gh_dir = os.path.dirname(ghenv.Component.OnPingDocument().FilePath)
src = os.path.join(gh_dir, "..", "src")
if src not in sys.path:
    sys.path.insert(0, src)

import gh_bridge, systems, testing
importlib.reload(gh_bridge)

cells = testing.fake_cells(8, 6)
a = gh_bridge.cells_to_curves(cells)
b = gh_bridge.to_curves([l for c in cells for l in systems.run("parallel", c)])
```

El `.gh` debe estar guardado dentro de `gh/` para que la ruta funcione en ambos computadores.

---

## Rutina con GitHub Desktop

```
1. Antes de trabajar  →  Fetch origin / Pull     (recibir lo de tu compañero/a)
2. Trabajar normal en Rhino / Grasshopper / Python
3. Al terminar        →  Commit  (mensaje claro: "R2 de subdivisión lista")
                      →  Push origin              (enviar)
```

### Reglas

1. **Pull antes de empezar, Push al terminar.**
2. Cada uno edita **solo sus archivos**.
3. `MAIN.gh` lo edita **uno a la vez**; avisar por chat ("estoy en MAIN").
4. `contract.py` y `config.py` se cambian **solo de común acuerdo**.
5. Archivos pesados (videos, `.3dm` grandes, fotos) van a **OneDrive/Drive**, no a GitHub.
6. Commits pequeños y frecuentes, con mensajes que digan qué cambió.
