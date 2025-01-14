from Visualisation import *
from Simulator import *
import time

# Configuratie
VISUALISATION=True

if __name__ == "__main__":
    w = World(110)

    glider = input("Glider: Y/n\n")
    if  glider.capitalize() == "Y":
        w.set(2, 0)
        w.set(2, 1)
        w.set(2, 2)
        w.set(0, 1)
        w.set(1, 2)

    variant = input("Variant: Y/n\n")
    if variant.capitalize() == "Y":
        split_input = input("BX/SY[/AZ]\n").split("/")
        if len(split_input) == 3:
            b, s, a = split_input[:3]

            b = [int(con) for con in b[1:]]
            s = [int(con) for con in s[1:]]
            a = int(a[1:])
        elif len(split_input) == 2:
            b, s = split_input[:2]
            b = [int(con) for con in b[1:]]
            s = [int(con) for con in s[1:]]
            a = None
        else:
            b = [3]
            s = [2,3]
            a = None
    else:
        b = [3]
        s = [2,3]
        a = None
    
    print(f"Rules;\nb={b}\ts={s}\ta={a}")
    sim = Simulator(w, b=b, s=s, a=a)

    if VISUALISATION:
        vis = Visualisation(sim)
    else:
        while True:
            # Create new world and print to screen
            print(sim.update())
            # slow down simulation
            time.sleep(0.5)