from assets import plant

class Dandelion(plant.Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 0, 0, "Dandelion", 1)

    def action(self):
        for _ in range(3):
            super().action()