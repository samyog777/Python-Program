"""Creating function to add 2 numbers and displaying wrong answer"""
def sum_of_int():

    #prompt user to input numbers
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    sum_of_two=(num1+num2)
    if sum_of_two >= 15 and sum_of_two <= 20:
        print(20)
    else:
        print(sum_of_two)
    return
sum_of_int()



