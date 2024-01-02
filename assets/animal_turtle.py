import random
from assets import animal

class Turtle(animal.Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 2, 1, "Turtle", 1)

    def action(self):
        if (random.randint(0, 99) < 75):
            return

        super().action()

    def reflectsAttack(self, org):
        if (org.getStrength() < 5):
            self.getWorld().getGUI().logReflect(self, org)
            return True

        return False