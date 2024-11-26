# Proyecto de Búsqueda de Caminos

Este proyecto implementa un algoritmo de búsqueda de caminos en un mapa utilizando Python. El objetivo es encontrar el camino más corto desde un punto de inicio hasta un punto de destino en un mapa que contiene diferentes tipos de celdas con distintos costos de movimiento.

## Estructura del Proyecto

- `mapa.py`: Contiene la clase `Mapa` que maneja la representación del mapa y la lógica para obtener vecinos y verificar caminos.
- `main.py`: Contiene la lógica principal del programa, incluyendo la búsqueda del camino utilizando el algoritmo A*.
- `celda.py`: Contiene la clase `Celda` que representa cada celda del mapa con sus propiedades y costos de movimiento.
- `jugador.py`: Contiene la clase `Jugador` que representa al jugador y su movimiento en el mapa.
- `heuristica.py`: Contiene la función `distancia_octile` que calcula la heurística para el algoritmo A*.

## Tipos de Celda

- **Normal**:
  - Representación: `.`
  - Costo de movimiento: `1`

- **Muro**:
  - Representación: `█`
  - Costo de movimiento: `infinito` (no transitable)

- **Peligrosa**:
  - Representación: `!!︎︎`
  - Costo de movimiento: `5`

- **Vida**:
  - Representación: ``
  - Costo de movimiento: `0.5`

## Uso

Para ejecutar el programa principal, usa el siguiente comando:
```sh
python main.py
