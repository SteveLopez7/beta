import os

def cal(x, y):
    #Process
    add = x + y 
    return add

############Main##################################
os.system('clear')
#Inputs
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

ans = cal(num1, num2)

#Outputs form 1
print(f"The additio is: {ans}")

#Outputs form 2
print("The additio is: ", cal(num1, num2))