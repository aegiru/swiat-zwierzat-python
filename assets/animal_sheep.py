from assets import animal

class Sheep(animal.Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 4, 4, "Sheep", 1)