class Animal:
    def __init__(self, legs):
        self.legs = legs


class Dog(Animal):
    def __init__(self, color, legs):
        super().__init__(legs)
        self.color = color


class DogChild(Dog):
    def __init__(self, name, color, legs):
        super().__init__(color, legs)
        self.name = name

    def representation(self):
        return f"Dog name is {self.name} of color {self.color} and has {self.legs} legs"


d1 = DogChild("Bujo", "GoldenBrown", "4")
print(d1.representation())
