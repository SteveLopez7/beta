'''
Dev: Steve López
Game: Numerical Race
'''
import os
import random

def bienvenid():
    print("Carrera Numérica")
    print("\n")

def tirar_dados():
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    return dado1,dado2

def jugar():
    os.system('clear')
    bienvenid()

jugadores=int(input("Cuántos jugadores? (2 a 4): "))
while jugadores <2 or jugadores > 4:
    jugadores=int(input("Numero Invalido. Nuevamente (2 a 4): "))

print("\n")
print("Niveles")
print("1 Basico(20)")
print("2 Intermedio(30)")
print("3 Avanzado(50)")
print("4 Experto(100)")
print("\n")

nivel = input("Selecciona el nivel: ")
nivel=int(input("Erro Selecciona (1 al 4): "))

