from assets import plant

class Belladonna(plant.Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 99, 0, "Belladonna", 1)

    def isEatenBy(self, org):
        org.getWorld().getGUI().logAteDeath(org, self)
        org.dies()
        return super().isEatenBy(org)