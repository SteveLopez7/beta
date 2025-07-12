'''
Generar lista de números teniendo en cuenta 
un número de incio (li) y un número de fin (ls).

Los números deben ser ingresados por el usuario.

Si el primer número es mayor que el segundo, la lista se debe 
imprimir en orden descendente.
'''
import os

os.system('clear')
li = int(input("Ingresa limite inferior: "))
ls = int(input("Ingresa limite superior: "))

i = li
if li <= ls:
    while i <= ls:
        print(i)
        i += 1
else: 
    while i >= ls:
        print(i)
        i -= 1


