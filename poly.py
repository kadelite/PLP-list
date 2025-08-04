class Vehicle:
    def move(self):
        pass  # Base method, to be overridden

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Using polymorphism
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
