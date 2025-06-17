'''
Dev: Steve López
Description: 
Get Player Name
Generate Two Random Number into 2 dices
Dice 1: 1-6
Dice 2: 1-6
Print dices values
'''
import os
from random import randint, uniform

os.system('clear')
print(":::WELCOME TO MY PARCHIS:::")

#print("player name: ")
player_name= input("Player name: ") 
dice1 = randint(1,6)
dice2 = randint(1,6)

print(f"Dice 1: {dice1}")
print(f"Dice 2: {dice2}")