import os
from random import randint

i = 1
status = True
while True:
    d1 = randint(1,6)
    d2 = randint(1,6)
   
    print(f"Lanzamiento {i}: ")
    print(f"Dice 1: {d1}")
    print(f"Dice 2: {d2}")
    print("\n")
    i += 1

    status_try_again = True
    while status_try_again:
        try_again = input("¿Try again? [y/Y/n/N]: ")
        if try_again == 'y' or try_again == 'Y' or try_again == 'n' or try_again == 'N':
            status_try_again = False
        else:
            print("Invalide option, please press y/Y/n/N")    

    if try_again == 'n' or try_again == 'N':  
            break