"""Python code to make table of users number"""

#prompt user to enter number
num=int(input("Enter a number to find its factorial value:"))

#Using if else statemnt
if num < 1:
    print("Negative number's factorial cannot be found!")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    factorial=1
#Usinf for loop
    for i in range(1,num+1):
        factorial*=i

#Printing function's output
print("The factorial of",num,"is",factorial)
