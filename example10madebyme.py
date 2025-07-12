import os
from random import randint

lan = True
i = 0
while lan:
    d1 = randint(1,6)
    d2 = randint(1,6)
    
    i+=1

    print(f"Lanzamiento {i}: ")
    print(f"Dice 1: {d1}")
    print(f"Dice 2: {d2}")
    print("\n")

    

    print(f"¿Deseas lanzar los dados nuevamente?: ")
    question= input("y/n: ").lower()

    if question != "y":
        lan=False

    print(f"Usted lanzo los dados {i} veces")   



