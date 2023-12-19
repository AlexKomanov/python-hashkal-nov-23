class Vehicle:
    my_brand = "Tesla"

    def __init__(self, color: str, max_speed: int):
        self.color = color
        self.max_speed = max_speed

    def get_info(self):
        print(f"I'm a '{self.color}' vehicle with max speed of {self.max_speed}")


class Car(Vehicle):
    def __init__(self, color: str, max_speed: int, brand: str):
        # Vehicle("Black", 150)
        super().__init__(color, max_speed)
        self.brand = brand

    def get_info(self):
        print(f"I'm a '{self.color}' car with brand '{self.brand}' with max speed of {self.max_speed}")


class Truck(Vehicle):
    def __init__(self, color: str, max_speed: int):
        super().__init__(color, max_speed)


my_vehicle = Vehicle("Black", 150)
my_vehicle_2 = Vehicle("White", 350)
my_vehicle.get_info()
my_vehicle_2.get_info()
print(my_vehicle_2.my_brand)

my_car = Car("Red", 400, "Tesla")
my_car.get_info()
my_truck = Truck("Green", 100)

my_vehicle = [my_vehicle_2, my_vehicle, my_car, my_truck]

for item in my_vehicle:
    item.get_info()
