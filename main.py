import random
from mapa import Mapa
from jugador import Jugador
from heuristica import distancia_octile
import heapq

class Nodo:
    def __init__(self, celda, padre=None, g=0, h=0):
        self.celda = celda
        self.padre = padre
        self.g = g  # Costo desde el inicio hasta este nodo
        self.h = h  # Heurística estimada hasta el destino
        self.f = g + h  # Costo total

    def __lt__(self, other):
        return self.f < other.f

def buscar_camino(mapa):
    inicio = Nodo(mapa.inicio)
    destino_celda = mapa.destino

    lista_abierta = []
    heapq.heappush(lista_abierta, inicio)
    lista_cerrada = set()

    while lista_abierta:
        nodo_actual = heapq.heappop(lista_abierta)

        if nodo_actual.celda == destino_celda:
            return reconstruir_camino(nodo_actual)

        lista_cerrada.add((nodo_actual.celda.x, nodo_actual.celda.y))

        vecinos = mapa.obtener_vecinos(nodo_actual.celda)
        for vecino_celda in vecinos:
            if (vecino_celda.x, vecino_celda.y) in lista_cerrada:
                continue

            # Calcular el costo de movimiento
            costo_movimiento = nodo_actual.g + vecino_celda.costo_movimiento
            # Si el movimiento es diagonal, agregar el costo extra
            if abs(vecino_celda.x - nodo_actual.celda.x) == 1 and abs(vecino_celda.y - nodo_actual.celda.y) == 1:
                costo_movimiento += (1.41 - 1)  # Diferencia entre diagonal y ortogonal

            h_nuevo = distancia_octile(vecino_celda, destino_celda)
            nodo_vecino = Nodo(vecino_celda, nodo_actual, costo_movimiento, h_nuevo)

            # Verificar si ya está en la lista abierta con un costo menor
            en_lista_abierta = False
            for nodo_abierto in lista_abierta:
                if nodo_abierto.celda == vecino_celda and nodo_abierto.g <= costo_movimiento:
                    en_lista_abierta = True
                    break

            if not en_lista_abierta:
                heapq.heappush(lista_abierta, nodo_vecino)
    return None  # No se encontró camino

def reconstruir_camino(nodo):
    camino = []
    while nodo:
        camino.append(nodo)
        nodo = nodo.padre
    return camino[::-1]  # Invertir el camino

def generar_posicion_aleatoria(mapa):
    x = random.randint(0, mapa.ancho - 1)
    y = random.randint(0, mapa.alto - 1)
    return mapa.obtener_celda(x, y)

def main():
    mapa = Mapa()

    while True:
        inicio = generar_posicion_aleatoria(mapa)
        destino = generar_posicion_aleatoria(mapa)
        if distancia_octile(inicio, destino) >= 5:
            break

    mapa.inicio = inicio
    mapa.destino = destino

    print("Mapa inicial:")
    mapa.imprimir_mapa()

    jugador = Jugador(mapa.inicio)

    # Buscar el camino
    camino_nodos = buscar_camino(mapa)

    if camino_nodos:
        camino_celdas = [nodo.celda for nodo in camino_nodos]
        costo_total = camino_nodos[-1].g  # El costo total es el g del último nodo

        print("\nCamino encontrado:")
        for nodo in camino_nodos:
            celda = nodo.celda
            print(f"({celda.x}, {celda.y}) Tipo: {celda.tipo} Costo acumulado: {nodo.g:.2f}")
            jugador.mover_a(celda)

        print(f"\nCosto total del camino: {costo_total:.2f}")

        # Imprimir el mapa con el camino
        print("\nMapa con camino:")
        mapa.imprimir_mapa(camino=camino_celdas)
    else:
        print("No se encontró un camino")

if __name__ == "__main__":
    main()