class Jugador:
    def __init__(self, posicion_inicial):
        self.posicion = posicion_inicial
        self.camino_recorrido = []

    def mover_a(self, nueva_celda):
        self.camino_recorrido.append(nueva_celda)
        self.posicion = nueva_celda