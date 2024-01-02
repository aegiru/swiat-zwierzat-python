from assets import animal

class Wolf(animal.Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 9, 5, "Wolf", 1)