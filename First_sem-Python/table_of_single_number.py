"""Python code to make table of users number"""

#prompt user to enter number
num=int(input("Enter a positive number to make its table:"))

#Using if else statemnt
if num < 1:
    print("Number must be positive!")
else:
    print("The table of",num,"is:")

#Using for loop to make multiplication table
    for i in range(1,11):

#For printing value
        print(num,"*",i,"=",num*i)


