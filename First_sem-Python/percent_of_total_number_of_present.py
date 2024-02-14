"""The Python code to know percent of class attend"""

# prompt user to enter total number of class
total_class=int(input("Enter total number of class you have:"))

#prompt user to enter number of classes he absent
absent_class=int(input("Enter number of class you absent:"))

present_days=total_class-absent_class

percent_class=int((present_days*100)/total_class)

print("The percent of you present in class is",percent_class)
if percent_class>=80:
    print("You can give exam")
else:
    print("You cannot give exam")
