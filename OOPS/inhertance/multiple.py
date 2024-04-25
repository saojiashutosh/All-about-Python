class Bat:
    def __init__(self, brand, willow):
        self.brand = brand
        self.willow = willow


class Ball:
    def __init__(self, color):
        self.color = color


class BatBall(Bat, Ball):
    def __init__(self, brand, willow, color):
        Bat.__init__(self, brand, willow)
        Ball.__init__(self, color)

    def cricket(self):
        return f"We have {self.brand} {self.willow} willow bat and ball of color {self.color}"


c1 = BatBall("MRF", "English", "Red")
print(c1.cricket())
