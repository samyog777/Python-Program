"""Python code to make marked price into fixed price"""

#prompt user to enter marked price of rice
marked0=float(input("Enter marked price:"))
dicount0=float(input("Enter discount price:"))

#calculate fixed price
fixed0=marked0-dicount0

print("The fixed price of",marked0,"and",dicount0,"is",fixed0)


