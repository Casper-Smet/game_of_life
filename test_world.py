from unittest import TestCase
from World import *


class TestWorld(TestCase):
    """
    Test cases for ``World`` data type.
    """
    def setUp(self):
        """
        Common setup for running tests
        """
        self.width, self.height = 10, 12
        self.world = World(self.width, self.height)

    def test_set(self):
        """
        Tests setting value on location (x,y).
        """
        x, y = 4, 6
        self.world.set(x, y)
        self.assertEqual(self.world.world[y][x], 1)
        value = 7
        self.world.set(x, y, 7)
        self.assertEqual(self.world.world[y][x], 7)

    def test_get(self):
        """
        Tests getting value from location (x, y).
        """
        x, y = 3, 5
        value = 3
        self.world.world[y][x] = 3
        self.assertEqual(self.world.get(x, y), value)

    def test_get_neighbours(self):
        """
        Tests getting neighbours from location.
        """
        x, y = 2, 0
        value = 4
        self.world.set(x, self.height-1, value)
        neighbours = self.world.get_neighbours(x, y)
        self.assertEqual(8, len(neighbours))
        self.assertIn(value, neighbours)

    def test_check_survive(self):
        """
        Tests if cell survives
        """
        x1, y1 = 4, 6  
        x2, y2 = 6, 7
        
        self.world.set(6, 6)
        self.world.set(5, 6)
        # Less than 2 living neighbours, dies
        print(self.world.get_neighbours(x1, y1))
        self.assertEqual(self.world.check_survive(x1, y1), False)
        # 2 living neighbours, survives
        self.assertEqual(self.world.check_survive(x2, y2), True)

        self.assertEqual(self.world.check_survive(x1, y1, [1]), True)
        # More than 3 living neighbours, dies #TODO

    def test_check_rebirth(self):
        """
        Check if cell is (re)born
        """
        x1, y1 = 7, 9
        x2, y2 = 1, 1

        self.world.set(1, 0)
        self.world.set(0, 1)
        self.world.set(2, 0)

        # Three living neighbours, (re)born
        self.assertEqual(self.world.check_rebirth(x2, y2), True)

        # Not three living neighbours, stays dead
        self.assertEqual(self.world.check_rebirth(x1, y1), False)

