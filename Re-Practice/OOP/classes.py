# class Point():
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2

# p = Point(2, 8)
# print(p.x)
# print(p.y)


class Flight():
    def __init__(self,capacity):
        self.x = capacity
        self.passenger = []

    def passenger_list(self, name):
        if not self.count():
            return False
        self.passenger.append(name)
        return True

    def count(self):
        return self.x - len(self.passenger)
    
flight = Flight(3)

people = ["Harry","Ron","Hermione","Ginny"]

for person in people:
    if flight.passenger_list(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")
