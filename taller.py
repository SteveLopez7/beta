'''
Dev: Steve López
Fecha: 29-junio-2025
Script: Simular reporte financiero para 5 clientes
'''
import random  

print("BIENVENIDO AL SISTEMA FINANSMART")

for i in range(5):
    print("\nCLIENTE #" + str(i + 1)) 

    nombre = input("Ingrese nombre completo: ")
    cedula = input("Ingrese número de identificación: ")
    edad = int(input("Ingrese edad: "))
    gastos = float(input("Ingrese gastos mensuales: "))
    telefono = input("Ingrese número de teléfono: ")
    direccion = input("Ingrese dirección: ")
    estado = True 

    ingreso = random.randint(1000000, 8000000)
    balance = ingreso - gastos

    print("\n REPORTE DEL CLIENTE ")
    print(f"Nombre     : {nombre}")
    print(f"Cédula     : {cedula}")
    print(f"Edad       : {edad} años")
    print(f"Teléfono   : {telefono}")
    print(f"Dirección  : {direccion}")
    print(f"Estado     : {estado}")
    print(f"Ingreso    : {ingreso}")
    print(f"Gastos     : {gastos}")
    print(f"Balance    : {balance}")
    
print("\nREPORTE FINALIZADO PARA 5 CLIENTES")
print("Gracias por usar FinanSmart.")
