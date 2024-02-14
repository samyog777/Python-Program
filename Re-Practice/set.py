# creating an empty set

s = set()

#Adding elements to set
s.add(3)
s.add(2)
s.add(1)
s.add(4)
s.add(4) # one 4 will be printed cause set is for unique values
s.add(6)

print(s)

s.remove(1) #remove number 1 

print(f"The set has {len(s)}") #leb(s) will calculate the range or number of set

