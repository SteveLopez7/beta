'''
Dev: Steve López
Activity: N° 8
Description: Programa que solicita N números enteros en un vector.
Si el nuevo valor a ingresar es igual a la SUMA del último y penúltimo valor ingresado,
el sistema arrojará un mensaje: 
Error: El número ingresado es igual a la suma de los dos antetiores. Intente con otro.
Esto hasta que el número sea difernete a la SUMA mencionada. 
'''
numeros = []

N = int(input("¿Cuantos números deseas ingresar?: "))

i = 0 

while i < N:
    nuevo = int(input("Ingrese un número: "))
    if i >= 2:
        suma = numeros[i - 1] + numeros[i - 2]
        if nuevo == suma:
            print("Error: El número ingresado es igual a la suma de los dos antetiores. Intente con otro.")
            continue

    numeros.append(nuevo)
    i = i + 1 

print("Lista final de números ingresados:")
print(numeros)   
