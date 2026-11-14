"""
Shared project configuration.

All the work happens in 2D, in millimeters, inside the rectangle of the
"unrolled" bottle:
    x = 0 .. CANVAS_WIDTH   (around the bottle; x = 0 is the seam)
    y = 0 .. CANVAS_HEIGHT  (height, from the bottom)

Change these values only by mutual agreement.
"""

# TODO: measure the real bottle (drawable circumference x height)
CANVAS_WIDTH = 220.0   # mm
CANVAS_HEIGHT = 180.0  # mm

# Marker constraints
PEN_WIDTH = 1.0        # mm, stroke width
MIN_SPACING = 1.5      # mm, minimum distance between parallel lines
