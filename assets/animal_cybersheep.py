from assets import animal

class CyberSheep(animal.Animal):
    __target = None

    def __init__(self, x, y, world):
        super().__init__(x, y, world, 11, 4, "CyberSheep", 1)

    def action(self):
        self.__findNearestPine()
        if (self.__getTarget() != None):
            self.__moveTowardsPine()
        else:
            super().action()

    def isCyberSheep(self):
        return True

    def __setTarget(self, target):
        self.__target = target

    def __getTarget(self):
        return self.__target

    def __findNearestPine(self):
        self.__setTarget(self.getWorld().getNearestPine(self.getX(), self.getY()))

    def __moveTowardsPine(self):
        if (self.__getTarget() == None):
            return

        xDiff = 0
        yDiff = 0

        if (self.getX() < self.__getTarget().getX()):
            xDiff = 1
        elif (self.getX() > self.__getTarget().getX()):
            xDiff = -1
        elif (self.getY() < self.__getTarget().getY()):
            yDiff = 1
        elif (self.getY() > self.__getTarget().getY()):
            yDiff = -1

        if (self._wouldBeOutOfBounds(self.getX() + xDiff, self.getY() + yDiff)):
            return

        potentialCollision = self.getWorld().getOrganism(self.getX() + xDiff, self.getY() + yDiff)

        if (self.collision(potentialCollision)):
            self.setX(self.getX() + xDiff)
            self.setY(self.getY() + yDiff)