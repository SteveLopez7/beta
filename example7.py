'''
Script description:
Crea un script PY que lance dos daods N veces, y visualice por pantalla los resultados.
Requisitos: 
La cantidad o número de veces debe ser ingresada por el usuario.
Deben lanzarse dos dasos
Usar funcion
'''

import os
from random import randint

lan = int(input('¿Cuantas veces deseas lanzar los dados?: '))

i = 1
while i <= lan :
    d1 = randint(1,6)
    d2 = randint(1,6)
    
    print(f"Lanzamiento {i}: ")
    print(f"Dice 1: {d1}")
    print(f"Dice 2: {d2}")
    print("\n")

    i+=1