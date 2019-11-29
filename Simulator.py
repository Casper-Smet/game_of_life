from World import *
from typing import List

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None, b: List[int] = None, s: List[int] = None, a: int = None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world

        if b == None:
            self.b = [3]
        else:
            self.b = b
        
        if s == None:
            self.s = [2, 3]
        else:
            self.s = s
        if type(a) == int():
            assert a >= 4 and a < 10
        self.a = a

    def update_cell(self, x: int, y: int):
        """
        Returns the state of a single cell to the next generation. Uses rules for evolution.
        """
        value = self.get_world().get(x, y)
        if value == 0:
            reborn = self.get_world().check_rebirth(x, y, b = self.b, a=self.a)
            if reborn:
                if self.a:
                    new_state = self.a
                else:
                    new_state = 1
            else:
                new_state = 0

        else:
            survived = self.get_world().check_survive(x, y, s = self.s)
            if self.a: 
                if survived:
                    new_state = value
                else:
                    new_state = value - 1
            else:
                if survived:
                    new_state = value
                else:
                    new_state = 0
            
        return new_state


    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        
        next_flat_world = []
        for y in range(self.get_world().height):
            for x in range(self.get_world().width):
                value = self.update_cell(x, y)
                next_flat_world.append((x, y, value))
        
        for cell in next_flat_world:
            x, y, value = cell
            self.world.set(x, y, value=value)
        
        self.generation += 1

        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world