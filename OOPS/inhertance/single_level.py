class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):

    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def full_name(self):
        return super().full_name() + self.batterySize


my_car = ElectricCar("Tesla", "Model S", "80 kWh")
print(my_car.full_name())
