from assets import plant

class Guarana(plant.Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 0, 0, "Guarana", 1)

    def collision(self, org):
        org.setStrength(org.getStrength() + 3)
        return super().isEatenBy(org)