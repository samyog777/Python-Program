"""Python code to take city name of user and displaying its popular Monuments"""

#Prompt user to enter name of the city

city=input("Enter name of city:")
if city== ("Kathmandu"):
    print("The most famous monument in",city,"is Pasupatinath Temple.")
elif city == ("Pokhara"):
    print("The most famous monument in",city,"is Fewa lake.")
elif city ==("Nepalgunj"):
    print("The most famous monument in",city,"is Bageshwori Temple.")
else:
    print("The most famous monument in",city,"is Birgunj Ghanta Ghar.")
