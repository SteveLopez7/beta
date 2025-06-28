#Script description: 
'''
1. Get 2 numbers(the Float or integer)
2. Show main menu: (1). Add, (2). Sub, (3). Mul, (4). Div 
3. Select an option 
4. Create a function get the result according with the opt
Other: Clear screen 
'''
import os
'''
def calc1(x, y, z):
    if(z == '1'):
        ans = x + y

    if(z == '2'):
        ans = x - y

    if(z == '3'):
        ans = x * y

    if(z == '4'):
        ans = x / y         

    return ans
'''
'''
def calc2(x, y, z):
    if(z == '1'):
        ans = x + y
    else:
        if (z =='2'):
            ans = x - y
        else:
            if(z == '3'):
                ans = x * y
            else:
                if(z == '4'):
                 ans = x / y   
    return ans
'''
def calc3(x, y, z):
    if(z == '1'):
        ans = x + y
    elif (z == '2'):
        ans = x - y
    elif (z == '3'):
        ans = x * y
    elif (z == '4'):
        if y == 0:
            ans = "error"
        else:    
            ans = x / y
    else:
        if y == 0:
            ans = "error"
        else:        
            ans = (x + y,x - y,x * y, x / y)
    return ans                            
####Main#################
num1 = float(input('Press first number:'))
num2 = float(input('Press second number:'))

print("### MAIN MENU ###")
print("[1].Add")
print("[2].Sub")
print("[3].Mul")
print("[4].Div")
print("[5]. all")
opt = input("::. Press any option: ")
#print(type(opt))
#os.system('pause')

#res1 = calc1(num1,num2,opt)
#print(f"The result f1 is: {res1}")
#res2 = calc2(num1,num2,opt)
#print(f"The result f2 is: {res2}")
res3 = calc3(num1,num2,opt)
#print(f"The result f3 is: {res3}")
print(f"The result Add is: {res3[0]}")
print(f"The result Sub is: {res3[1]}")
print(f"The result Mul is: {res3[2]}")
print(f"The result Div is: {res3[3]}")