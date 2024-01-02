import random
from assets import animal

class Human(animal.Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 5, 4, "Human", 1)


    def isHuman(self):
        return True

    def action(self):
        self.__updateAbility()

        userInput = self.getWorld().getGUI().getUserInput()
        xDiff = 0
        yDiff = 0

        if (userInput == "w"):
            yDiff = -self.getRange()
        elif (userInput == "s"):
            yDiff = self.getRange()
        elif (userInput == "a"):
            xDiff = -self.getRange()
        elif (userInput == "d"):
            xDiff = self.getRange()
        elif (userInput == "e"):
            self.__activateAbility()
        else:
            return

        if (self._wouldBeOutOfBounds(self.getX() + xDiff, self.getY() + yDiff)):
            return

        potentialCollision = self.getWorld().getOrganism(self.getX() + xDiff, self.getY() + yDiff)

        if (self.collision(potentialCollision)):
            self.setX(self.getX() + xDiff)
            self.setY(self.getY() + yDiff)



    def __activateAbility(self):
        if (self.getAbilityCooldown() == 0):
            self.setAbilityCooldown(10)

    def __updateAbility(self):
        self.setRange(1)
        cooldown = self.getAbilityCooldown()

        if (cooldown > 7):
            self.setRange(2)

        if (cooldown > 5):
            if (random.randint(0,1) == 0):
                self.setRange(2)

        if (cooldown > 0):
            self.setAbilityCooldown(cooldown - 1)