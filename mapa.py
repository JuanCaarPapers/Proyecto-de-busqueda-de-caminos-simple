from celda import Celda
import random

class Mapa:
    def __init__(self, ancho=6, alto=6):
        self.ancho = ancho
        self.alto = alto
        self.celdas = []
        self.inicio = None
        self.destino = None
        self.generar_mapa()

    def generar_mapa(self):
        for y in range(self.alto):
            fila = []
            for x in range(self.ancho):
                celda = Celda(x, y)
                fila.append(celda)
            self.celdas.append(fila)

        # in y dest
        self.establecer_inicio(0, 0)
        self.establecer_destino(self.ancho - 1, self.alto - 1)

        # Colocar muros, zonas peligrosas y zonas de vida
        self.colocar_elementos_mapa()

    def colocar_elementos_mapa(self):
        celdas_disponibles = [
            celda for fila in self.celdas for celda in fila
            if celda != self.inicio and celda != self.destino
        ]

        # MUROS
        num_muros = int((self.ancho * self.alto) * 0.15)  # 15% del mapa
        self.colocar_elemento(celdas_disponibles, num_muros, 'muro')

        # PELIGRO
        num_peligrosas = int((self.ancho * self.alto) * 0.10)  # 10% del mapa
        self.colocar_elemento(celdas_disponibles, num_peligrosas, 'peligrosa')

        # VIDA
        num_vidas = int((self.ancho * self.alto) * 0.05)  # 5% del mapa
        self.colocar_elemento(celdas_disponibles, num_vidas, 'vida')

    def colocar_elemento(self, celdas_disponibles, cantidad, tipo):
        colocados = 0
        intentos = 0
        max_intentos = cantidad * 10

        while colocados < cantidad and intentos < max_intentos:
            celda = random.choice(celdas_disponibles)
            # Comprobar que no bloquea el camino entre inicio y destino
            if self.verificar_accesibilidad(celda, tipo):
                celda.tipo = tipo
                celda.costo_movimiento = celda.calcular_costo()
                celdas_disponibles.remove(celda)
                colocados += 1
            intentos += 1

    def verificar_accesibilidad(self, celda, tipo):
        tipo_original = celda.tipo
        celda.tipo = tipo

        hay_camino = self.hay_camino()
        celda.tipo = tipo_original

        return hay_camino

    def hay_camino(self):
        visitados = set()
        stack = [self.inicio]

        while stack:
            celda_actual = stack.pop()
            if celda_actual == self.destino:
                return True
            visitados.add((celda_actual.x, celda_actual.y))
            vecinos = self.obtener_vecinos(celda_actual)
            for vecino in vecinos:
                if (vecino.x, vecino.y) not in visitados:
                    stack.append(vecino)
        return False
    # INCIOS Y DESTINOS
    def establecer_inicio(self, x, y):
        self.inicio = self.obtener_celda(x, y)

    def establecer_destino(self, x, y):
        self.destino = self.obtener_celda(x, y)

    def obtener_celda(self, x, y):
        if 0 <= x < self.ancho and 0 <= y < self.alto:
            return self.celdas[y][x]
        else:
            return None
    #MOVIMIENTO
    def obtener_vecinos(self, celda):
        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1),  # Ortogonales
                       (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonales
        vecinos = []
        for dx, dy in movimientos:
            nx, ny = celda.x + dx, celda.y + dy
            vecino = self.obtener_celda(nx, ny)
            if vecino and vecino.es_transitable():
                vecinos.append(vecino)
        return vecinos

    def imprimir_mapa(self, camino=None):
        simbolos = {
            'normal': '.',
            'muro': '█',
            'peligrosa': '!!︎︎',
            'vida': '',
        }
        for y in range(self.alto):
            fila = ''
            for x in range(self.ancho):
                celda = self.celdas[y][x]
                if celda == self.inicio:
                    fila += 'I '
                elif celda == self.destino:
                    fila += 'D '
                elif camino and celda in camino:
                    fila += '* '
                else:
                    fila += simbolos.get(celda.tipo, '.') + ' '
            print(fila)