people = [
    {"Name":"Samyog","House":"Bhojpur"},
    {"Name":"Saugat","House":"Kathmandu"},
    {"Name":"Saurav","House":"Australia"}
]


# def f(person):
#     return person["House"]

# people.sort(key=f)

people.sort(key=lambda person: person["Name"])

print(people)

