from assets import animal

class Fox(animal.Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 3, 7, "Fox", 1)

    def wontEnter(self, org):
        if (self.getStrength() >= org.getStrength()):
            self.getWorld().getGUI().logWontEnter(self, org)
            return True

        return False
