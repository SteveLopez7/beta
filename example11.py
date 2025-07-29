# import os
# os.system('cls')

#Listas (Mutable)
my_list = [1,2,3,True, False, 'Apple', 2j, 3.14, ['Mazda','Ford','Audi']]
for x in my_list:
    print(x)
my_list[1] = ['Banana','Manzana']
print(my_list)

# print(my_list)
# print("\n")
# print(my_list[8])
# print(my_list[8][1])
# print(type(my_list[8]))

#Tuplas (Inmutable)
print("\n")
my_tupla = (1,2,3)
print(type(my_tupla))
print(my_tupla)
# my_tupla[0] = 10
print(my_tupla)

#Diccionarios (Mutables)
print("\n")
my_data = {
    "firstname ": "Steve",
    "lastname ": "Lopez",
    "city": "Pasto",
    "country": "COL"
}
print(my_data)
print(my_data["firstname "])

name = "Steve"
for n in name:
    print(n)
print(name[0])