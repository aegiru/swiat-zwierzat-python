import random


class Organism:
    _strength = 0
    _initiative = 0
    _x = 0
    _y = 0
    _age = 0
    _world = None
    _name = ""
    _range = 0
    _abilityCooldown = 0

    def __init__(self, x, y, world, strength, initiative, name, range):
        self._x = x
        self._y = y
        self._world = world
        self._strength = strength
        self._initiative = initiative
        self._name = name
        self._range = range



    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getStrength(self):
        return self._strength

    def getInitiative(self):
        return self._initiative

    def getAge(self):
        return self._age

    def getWorld(self):
        return self._world

    def getName(self):
        return self._name

    def getRange(self):
        return self._range

    def getAbilityCooldown(self):
        return self._abilityCooldown



    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    def setStrength(self, strength):
        self._strength = strength

    def setInitiative(self, initiative):
        self._initiative = initiative

    def setAge(self, age):
        self._age = age

    def setWorld(self, world):
        self._world = world

    def setName(self, name):
        self._name = name

    def setRange(self, range):
        self._range = range

    def setAbilityCooldown(self, abilityCooldown):
        self._abilityCooldown = abilityCooldown



    def action(self):
        pass

    def collision(self, org):
        return False

    def reflectsAttack(self, org):
        return False

    def escapesAttack(self, org):
        return False

    def escape(self, org):
        return False

    def dies(self):
        self.getWorld().clearOrganism(self.getX(), self.getY())

    def isEatenBy(self, org):
        return False

    def reproduction(self):
        if (self.getAge() < 5):
            return

        if (random.randint(0, 99) < 50):
            return

        neighbor = self._getRandomNeighbor()

        if (self.getWorld().isEmpty(neighbor[0], neighbor[1])):
            self.getWorld().getGUI().logReproduction(self)
            self.getWorld().setOrganism(self._clone(neighbor[0], neighbor[1], self.getWorld()))

    def wontEnter(self, org):
        return False

    def isAnimal(self):
        return False

    def isPlant(self):
        return False

    def isHuman(self):
        return False

    def isCyberSheep(self):
        return False



    def _wouldBeOutOfBounds(self, x, y):
        maxY = self.getWorld().getSizeY()
        maxX = self.getWorld().getSizeX()
        return x < 0 or y < 0 or x >= maxX or y >= maxY

    def _areOfSameType(self, org):
        return type(self) == type(org)

    def _eats(self, plant):
        self.getWorld().getGUI().logEating(self, plant)
        return plant.isEatenBy(self)

    def _fight(self, org):
        if (self.getStrength() >= org.getStrength()):
            self.getWorld().getGUI().logKill(self, org)
            org.dies()
            return True
        else:
            self.getWorld().getGUI().logKill(org, self)
            self.dies()
            return False

    def _getRandomNeighbor(self):
        x = self.getX()
        y = self.getY()

        rand = random.randint(0, 3)

        if (rand == 0):
            y -= 1
        elif (rand == 1):
            y += 1
        elif (rand == 2):
            x -= 1
        elif (rand == 3):
            x += 1

        if (self._wouldBeOutOfBounds(x, y)):
            return self._getRandomNeighbor()

        return (x, y)

    def _clone(self, x, y, world):
        return self.__class__(x, y, world)
