"""Python code to take two parameters and printing product and positive"""
def sum_product(x,y):
    sum=x+y
#using if else statement
    if x >= 0 and y>=0:
        product=x*y
        print(product)
    else:
        return(0)
sum_product(2,6)

