import random
from assets import animal

class Antilope(animal.Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 4, 4, "Antilope", 2)

    def escapesAttack(self, org):
        return random.randint(0, 1) == 1

    def escape(self, org):
        didEscape = False
        positions = ([-1, 0], [1, 0], [0, -1], [0, 1])

        for pos in positions:
            newPos = [self.getX() + pos[0], self.getY() + pos[1]]

            if (self.getWorld().isEmpty(newPos[0], newPos[1])):
                self.setX(newPos[0])
                self.setY(newPos[1])
                didEscape = True

        if (didEscape):
            self.getWorld().getGUI().logEscape(self, org)

        return didEscape