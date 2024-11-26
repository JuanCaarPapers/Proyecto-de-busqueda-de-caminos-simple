import math

def distancia_octile(celda_actual, celda_destino):
    dx = abs(celda_actual.x - celda_destino.x)
    dy = abs(celda_actual.y - celda_destino.y)
    return (dx + dy) + (math.sqrt(2) - 2) * min(dx, dy)