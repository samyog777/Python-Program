"""Finding if a number user put is divided by 2 and 3 or not"""
num=float(input("Enter a number:"))
if num%2==0 and num%3==0:
    print(num,"The number is divisible by 2 and 3")
else:
    print(num,"The number is not divisible by 2 and 3")
