"""
[PATTERN GENERATION] Recursive subdivision grammar.

    Input:  initial cell (the whole canvas) + image fields
    Output: list of Cell (see contract.py)

Initial rules (draft):
    R1: cell with high detail         -> 4 cells (quadrants)
    R2: cell with a clear direction   -> 2 rectangles oriented along it
    R3: cell with mid tone            -> 2 triangles (diagonal)
    R4: terminal cell                 -> handed to a line system

TODO: implement.
"""
