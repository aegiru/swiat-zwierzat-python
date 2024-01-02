from assets import organism

class Animal(organism.Organism):
    def __init__(self, x, y, world, strength, initiative, name, range):
        super().__init__(x, y, world, strength, initiative, name, range)

    def action(self):
        newPos = self._getRandomNeighbor()

        potentialCollision = self.getWorld().getOrganism(newPos[0], newPos[1])

        if (self.collision(potentialCollision)):
            self.setX(newPos[0])
            self.setY(newPos[1])

    def collision(self, org):
        if (org == None):
            return True

        if (self._areOfSameType(org)):
            self.reproduction()
            return False
        else:
            if (org.reflectsAttack(self)):
                return False

            if (self.wontEnter(org)):
                return False

            if (org.isAnimal()):
                if (self.escapesAttack(org)):
                    return not self.escape(org)

                if (org.escapesAttack(self)):
                    return org.escape(self)

                return self._fight(org)

            if (org.isPlant()):
                return self._eats(org)

        return False

    def isAnimal(self):
        return True