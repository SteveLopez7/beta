import random

def lanzar_dados():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")

    if dice1 % 2 == 0 and dice2 % 2 == 0:
        print("YOU WIN")
    else:
        print("YOU LOSE")

lanzar_dados()
