"""
Configuracion compartida del proyecto.

Todo el trabajo se hace en 2D, en milimetros, dentro del rectangulo
de la botella "desenrollada":
    x = 0 .. CANVAS_WIDTH   (alrededor de la botella; x = 0 es la costura)
    y = 0 .. CANVAS_HEIGHT  (altura, desde abajo)

Cambiar estos valores solo de comun acuerdo.
"""

# TODO: medir la botella real (circunferencia x altura dibujable)
CANVAS_WIDTH = 220.0   # mm
CANVAS_HEIGHT = 180.0  # mm

# Restricciones del marcador
PEN_WIDTH = 1.0        # mm, grosor del trazo
MIN_SPACING = 1.5      # mm, separacion minima entre lineas paralelas
