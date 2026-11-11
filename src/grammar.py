"""
[ESTRUCTURA] Gramatica de subdivision recursiva.

    Entrada: celda inicial (el lienzo completo) + campos de la imagen
    Salida:  lista de Cell (ver contract.py)

Reglas iniciales (borrador):
    R1: celda con detalle alto     -> 4 celdas (cuadrantes)
    R2: celda con direccion clara  -> 2 rectangulos orientados
    R3: celda con tono medio       -> 2 triangulos (diagonal)
    R4: celda terminal             -> se entrega al sistema de lineas

TODO: implementar.
"""
