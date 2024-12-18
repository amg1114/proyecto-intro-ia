
from abc import ABC, abstractmethod

import random

from search.a_star_search import a_star_search
from search.bfs_search import bfs
from search.deep_search import deep_search


class Agente(ABC):
    def __init__(self, position):
        self.position = position
        self.encontrado = False
        self.movimientos = [
            (-1, 0),  # ARRIBA
            (0, 1),  # DERECHA
            (1, 0),  # ABAJO
            (0, -1),  # IZQUIERDA
        ]


class Piggy(Agente):
    def __init__(self, position):
        self.use_a_star = False
        self.find_rene = False
        self.find_galleta = False
        super().__init__(position)

    def move(self, goal_position, grid):
        costo = 1
        if self.position == goal_position:
            self.find_rene = True
            print("¡Piggy ha encontrado a René!")
            return self.position

        self.use_a_star = random.random() < 0.4

        if self.use_a_star:
            print("Moviendo a Piggy usando A*")
            path = a_star_search(
                self.position, goal_position, grid, self.movimientos, self)
            try:
                self.position = path[1][0]
                costo = path[1][1]
            except IndexError:
                costo = 0
                return self.position, costo
        else:
            print("Moviendo a Piggy usando BFS")
            path = bfs(self.position, goal_position,
                       grid, self.movimientos, self)
            try:
                self.position = path[1]
            except IndexError:
                costo = 0
                return self.position, costo
        if not path:
            return self.position, costo
            
        if self.position == goal_position:
            self.find_rene = True
            print("¡Piggy ha encontrado a René!")
        elif grid[self.position[0]][self.position[1]] == "G":
            print("¡Piggy ha encontrado la galleta!")
            
        return self.position, costo

class Rene(Agente):
    def __init__ (self, position):
        self.has_path = True
        
        super().__init__(position)
    def get_path(self, grid):
        ruta = deep_search(self.position, grid, self.movimientos)

        if ruta:
            return ruta
        else:
            print("Rene no encontro camino")
            self.has_path = False
            return None
