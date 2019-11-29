from unittest import TestCase
from Simulator import *
from numpy import array_equal


class TestSimulator(TestCase):
    """
    Tests for ``Simulator`` implementation.
    """
    def setUp(self):
        self.sim = Simulator()

    def test_update(self):
        """
        Tests that the update functions returns an object of World type.
        """
        self.assertIsInstance(self.sim.update(), World)
        world = World(5)
        world.set(1, 2)
        world.set(2, 2)
        world.set(3, 2)

        world2 = World(5)
        world2.set(2, 1)
        world2.set(2, 2)
        world2.set(2, 3)

        sim = Simulator(world=world)
        # In order to check equality between two numpy arrays, you have to use np.array_equal
        self.assertEqual(array_equal(sim.update().world, world2.world), True)

        

    def test_update_cell(self):
        """
        Tests that the update_cell function properly updates a single cell's state.
        """
        
        x1, y1 = 1, 1

        self.sim.world.set(1, 0)
        self.sim.world.set(0, 1)
        self.sim.world.set(2, 0)

        # Check if alive
        self.assertEqual(self.sim.update_cell(x1, y1), 1)
        

        # kill two cells so that (x1, y1) dies
        self.sim.world.set(1, 0, value=0)
        self.sim.world.set(0, 1, value=0)
        self.assertEqual(self.sim.update_cell(x1, y1), 0)
        
        # Make a new simulator with birth condition 1, surival condition 2
        sim2 = Simulator(world = self.sim.world, b=[1], s=[2])
        self.assertEqual(sim2.update_cell(x1, y1), 1)
        sim2.world.set(x1, y1)
        self.assertEqual(sim2.update_cell(x1, y1), 0)
        # Set survival condition to 1
        sim2.s = [1]
        sim2.world.set(x1, y1, value=0)
        self.assertEqual(sim2.update_cell(x1, y1), 1)
        sim2.world.set(x1, y1)
        self.assertEqual(sim2.update_cell(x1, y1), 1)


    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)
