# Base class: Superhero
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I'm {self.name}, protector of {self.city} with the power of {self.power}.")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Inheritance: Subclass with extra ability and method overriding
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    # Polymorphism: Overriding use_power method
    def use_power(self):
        print(f"{self.name} flies at {self.flight_speed} mph and uses {self.power}!")

# Create instances
hero1 = Superhero("ShadowBlade", "invisibility", "Metro City")
hero2 = FlyingSuperhero("SkyFlash", "lightning", "Cloud City", 300)

# Use methods
hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()
