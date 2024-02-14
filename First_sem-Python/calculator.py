""" Making a mini Calculator"""
def addition(a,b):
    return(a+b)
def subtraction(a,b):
    return(a-b)
def multiplication(a,b):
    return(a*b)
def division(a,b):
    return(a/b)
def modulus(a,b):
    return(a%b)
def exponentiation(a,b):
    return(a**b)

"""code for entering user input"""

num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))

"""Code to operate certain operation"""

print("addition:", addition(num1,num2))
print("subtraction:", subtraction(num1,num2))
print("multiplication:", multiplication(num1,num2))
print("division:", division(num1,num2))
print("Modulus:", modulus(num1,num2))
print("Exponentiation:", exponentiation(num1,num2))


help[addition]
