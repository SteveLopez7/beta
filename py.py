'''
Dev: Steve López
Description:
Juego: Carrera Numérica
- Se elige el número de jugadores (2 a 4)
- Se elige el nivel de juego (distancia/meta)
- Cada jugador lanza dos dados por turno
- Gana quien llegue a la meta o saque 3 pares seguidos
'''

import os
import random

# Función de bienvenida
def bienvenida():
    print("###############################")
    print("#      CARRERA NUMÉRICA      #")
    print("###############################")
    print("\n")

# Función para lanzar dados
def lanzar_dados():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    return d1, d2

# Función principal del juego
def jugar():
    os.system('clear')  # Limpiar pantalla
    bienvenida()

    jugadores = int(input("¿Cuántos jugadores? (2 a 4): "))
    while jugadores < 2 or jugadores > 4:
        jugadores = int(input("Número no válido. Intenta otra vez (2 a 4): "))

    print("\nNiveles:")
    print("1. Básico (20)")
    print("2. Intermedio (30)")
    print("3. Avanzado (50)")
    print("4. Experto (100)")
    nivel = input("Selecciona el nivel: ")

    if nivel == '1':
        meta = 20
    elif nivel == '2':
        meta = 30
    elif nivel == '3':
        meta = 50
    elif nivel == '4':
        meta = 100
    else:
        meta = 20  # por defecto si se ingresa mal

    # Posiciones y contadores de pares
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0

    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0

    turno = 1
    ganador = False  # ← añadido para controlar el final del juego

    while ganador == False:
        print(f"\n=== Turno {turno} ===")

        if jugadores >= 1:
            d1, d2 = lanzar_dados()
            print(f"Jugador 1 lanza: {d1} y {d2}")
            if d1 == d2:
                c1 = c1 + 1
            else:
                c1 = 0
            p1 = p1 + d1 + d2
            print(f"Jugador 1 posición: {p1}")
            if c1 == 3 or p1 >= meta:
                print("🏁 Jugador 1 gana")
                ganador = True
                break

        if jugadores >= 2:
            d1, d2 = lanzar_dados()
            print(f"Jugador 2 lanza: {d1} y {d2}")
            if d1 == d2:
                c2 = c2 + 1
            else:
                c2 = 0
            p2 = p2 + d1 + d2
            print(f"Jugador 2 posición: {p2}")
            if c2 == 3 or p2 >= meta:
                print("🏁 Jugador 2 gana")
                ganador = True
                break

        if jugadores >= 3:
            d1, d2 = lanzar_dados()
            print(f"Jugador 3 lanza: {d1} y {d2}")
            if d1 == d2:
                c3 = c3 + 1
            else:
                c3 = 0
            p3 = p3 + d1 + d2
            print(f"Jugador 3 posición: {p3}")
            if c3 == 3 or p3 >= meta:
                print("🏁 Jugador 3 gana")
                ganador = True
                break

        if jugadores == 4:
            d1, d2 = lanzar_dados()
            print(f"Jugador 4 lanza: {d1} y {d2}")
            if d1 == d2:
                c4 = c4 + 1
            else:
                c4 = 0
            p4 = p4 + d1 + d2
            print(f"Jugador 4 posición: {p4}")
            if c4 == 3 or p4 >= meta:
                print("🏁 Jugador 4 gana")
                ganador = True
                break

        turno = turno + 1

# Llamado principal al juego
jugar()
