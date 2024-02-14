college_credit=int(input("Enter your college credits:"))
if college_credit>=90:
    print("'Senior Status'")
elif college_credit>=60:
    print("'Junior Status'")
elif college_credit>=30:
    print("'Sophomore Status'")
else:
    print("'Freshman Status'")