from assets import plant

class Grass(plant.Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 0, 0, "Grass", 1)