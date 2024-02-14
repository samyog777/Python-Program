"""Creating Fibonacci series"""
# Asking user to input to enter limit to Fibonacci series
limit=int(input("Enter your limit for Fibonacci series:"))
num1=0
num2=1
print(num1)
print(num2)
#Using while loop
while num1+num2 <=limit:
    num3=num1+num2
    print(num3)
    num1=num2
    num2=num3
