'''
Dev: Steve López
Game: Numerical Race
'''
import os
import random

def bienvenida():
    print("Carrera Numérica")
    print("\n")

def tirar_dados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    return dado1, dado2

def jugar():
    os.system('clear')
    bienvenida()

jugadores=int(input("Cuántos jugadores? (2 a 4): "))
while jugadores <2 or jugadores > 4:
    jugadores=int(input("Numero Invalido. Intenta Nuevamente (2 a 4): "))

print("\n")
print("Niveles")
print("1 Basico(20)")
print("2 Intermedio(30)")
print("3 Avanzado(50)")
print("4 Experto(100)")
print("\n")
nivel = int(input("Selecciona el nivel (1 al 4): "))  
while nivel < 1 or nivel > 4:  
    nivel = int(input("Error. Selecciona un nivel válido (1 al 4): "))  


if nivel == '1':
    meta = 20
elif nivel == '2':
    meta = 30
elif nivel == '3':
    meta = 50
elif nivel == '4':
    meta = 100
else:
    meta = 20

p1 = 0
p2 = 0
p3 = 0
p4 = 0

c1 = 0
c2 = 0
c3 = 0
c4 = 0

turno = 1
ganador = False

while ganador == False:
    print(f"\n=== Turno {turno} ===")

    if jugadores >= 1:
        dado1,dado2 = tirar_dados()
        print(f"Jugador 1 tira: {dado1} y {dado2}")
        if dado1 == dado2:
            c1 = c1 + 1
        else:
            c1 = 0
        p1 = p1 + dado1 + dado2
        print(f"Jugador 1 posición: {p1}")
        if c1 == 3 or p1 >= meta:
            print("Jugador 1 gana")
            ganador = True
            break

    if jugadores >= 2:
        dado1, dado2 = tirar_dados()
        print(f"Jugador 2 tira: {dado1} y {dado2}")
        if dado1 == dado2:
            c2 = c2 + 1
        else:
            c2 = 0
        p2 = p2 + dado1 + dado2
        print(f"Jugador 2 posición: {p2}")
        if c2 == 3 or p2 >= meta:
            print("Jugador 2 gana")
            ganador = True
            break

    if jugadores >= 3:
        dado1, dado2 = tirar_dados()
        print(f"Jugador 3 tira: {dado1} y {dado2}")
        if dado1 == dado2:
            c3 = c3 + 1
        else:
            c3 = 0
        p3 = p3 + dado1 + dado2
        print(f"Jugador 3 posición: {p3}")
        if c3 == 3 or p3 >= meta:
            print("Jugador 3 gana")
            ganador = True
            break

    if jugadores == 4:
        dado1, dado2 = tirar_dados()
        print(f"Jugador 4 lanza: {dado1} y {dado2}")
        if dado1 == dado2:
            c4 = c4 + 1
        else:
            c4 = 0
        p4 = p4 + dado1 + dado2
        print(f"Jugador 4 posición: {p4}")
        if c4 == 3 or p4 >= meta:
            print("Jugador 4 gana")
            ganador = True
            break
    turno = turno + 1

# jugar()        