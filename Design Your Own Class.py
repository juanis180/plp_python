# Base class
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery   # Encapsulation: make battery private with __

    def get_battery(self):
        return f"{self.__battery}% battery remaining"

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        print(f"{self.brand} {self.model} charged to {self.__battery}%")

# Inherited class (child class)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, cooling_system):
        super().__init__(brand, model, battery)  # Call parent constructor
        self.cooling_system = cooling_system

    # Polymorphism: override call() method
    def call(self, number):
        print(f"{self.brand} {self.model} makes a video call to {number} with smooth graphics!")

    def play_game(self, game):
        print(f"{self.brand} {self.model} is playing {game} with {self.cooling_system} cooling system.")

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S21", 70)
phone2 = GamingPhone("Asus", "ROG Phone 6", 50, "liquid cooling")

# Use methods
phone1.call("123-456-7890")
print(phone1.get_battery())
phone1.charge(20)

print("---")

phone2.call("987-654-3210")
phone2.play_game("PUBG")
print(phone2.get_battery())
