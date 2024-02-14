"""Python code to know weather the letter user put vowel or consonant"""

letter=input("Enter a letter:")

#Check if a letter is vowel or consonant

if letter in ["a","A","e","E","i","I","o","O","u","U"]:
    print(letter,"is vowel")
else:
    print(letter,"is consoant")
