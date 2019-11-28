from Visualisation import *
from Simulator import *
import time

# Configuratie
VISUALISATION=True

if __name__ == "__main__":
    w = World(110)
    glider = input("Y/n")
    if  glider.capitalize() == "Y":
        w.set(2, 0)
        w.set(2, 1)
        w.set(2, 2)
        w.set(0, 1)
        w.set(1, 2)
    sim = Simulator(w)

    if VISUALISATION:
        vis = Visualisation(sim)
    else:
        while True:
            # Create new world and print to screen
            print(sim.update())
            # slow down simulation
            time.sleep(0.5)