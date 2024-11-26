class Celda:
    def __init__(self, x, y, tipo='normal'):
        self.x = x
        self.y = y
        self.tipo = tipo  # 'normal', 'muro', 'peligrosa', 'vida'
        self.costo_movimiento = self.calcular_costo()

    def calcular_costo(self):
        if self.tipo == 'muro':
            return float('inf')  # Muro
        elif self.tipo == 'peligrosa':
            return 5
        elif self.tipo == 'vida':
            return 0.5
        else:
            return 1

    def es_transitable(self):
        return self.tipo != 'muro'