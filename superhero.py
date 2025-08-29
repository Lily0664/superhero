class Superhero:
    def __init__(self, name, power, secret_identity):
        self.name = name
        self.power = power
        self.__secret_identity = secret_identity  # Encapsulated attribute

    def reveal_identity(self):
        return f"{self.name}'s secret identity is {self.__secret_identity}."

    def use_power(self):
        return f"{self.name} uses {self.power}!"

    def __str__(self):
        return f"Superhero: {self.name}, Power: {self.power}"

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, secret_identity, flight_speed):
        super().__init__(name, power, secret_identity)
        self.flight_speed = flight_speed

    def use_power(self):
        # Polymorphism: overrides base method
        return f"{self.name} flies at {self.flight_speed} km/h using {self.power}!"

    def __str__(self):
        return f"FlyingSuperhero: {self.name}, Power: {self.power}, Flight Speed: {self.flight_speed} km/h"
