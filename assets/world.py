class World:
    __organismList = []
    __gui = None
    __sizeX = 0
    __sizeY = 0
    __turn = 0

    def __init__(self, sizeX, sizeY, gui):
        self.__sizeX = sizeX
        self.__sizeY = sizeY
        self.__gui = gui
        self.__turn = 0
        self.__organismList = []



    def setOrganism(self, organism):
        self.__organismList.append(organism)

    def getOrganism(self, x, y):
        for org in self.__organismList:
            if (org.getX() == x and org.getY() == y):
                return org
        return None

    def clearOrganism(self, x, y):
        for org in self.__organismList:
            if (org.getX() == x and org.getY() == y):
                self.__organismList.remove(org)
                return True
        return False

    def getTurn(self):
        return self.__turn

    def setTurn(self, turn):
        self.__turn = turn

    def getGUI(self):
        return self.__gui

    def getSizeX(self):
        return self.__sizeX

    def getSizeY(self):
        return self.__sizeY

    def isEmpty(self, x, y):
        return self.getOrganism(x, y) == None

    def __sortOrganisms(self):
        self.__organismList.sort(key=lambda org: (org.getInitiative(), org.getAge()), reverse=True)

    def doTurn(self):
        self.setTurn(self.getTurn() + 1)
        self.__sortOrganisms()
        for org in self.__organismList:
            org.setAge(org.getAge() + 1)
            org.action()

    def getOrganismCount(self):
        c = 0

        for org in self.__organismList:
            if org != None:
                c += 1

        return c

    def outputString(self):
        s = ""
        s += str(self.getSizeX()) + "\n"
        s += str(self.getSizeY()) + "\n"
        s += str(self.getTurn()) + "\n"
        s += str(self.getOrganismCount()) + "\n"
        for org in self.__organismList:
            if (org == None):
                continue

            s += org.getName() + "\n"
            s += str(int(org.getX())) + "\n"
            s += str(int(org.getY())) + "\n"
            s += str(int(org.getStrength())) + "\n"
            s += str(int(org.getInitiative())) + "\n"
            s += str(int(org.getAge())) + "\n"
            s += str(int(org.getRange())) + "\n"
            s += str(int(org.getAbilityCooldown())) + "\n"

        return s

    def getNearestPine(self, x, y):
        nearest = None
        nearestDist = 0

        for org in self.__organismList:
            if (org == None):
                continue

            if (org.getName() == "PineBorscht"):
                dist = abs(org.getX() - x) + abs(org.getY() - y)
                if (nearest == None or dist < nearestDist):
                    nearest = org
                    nearestDist = dist

        return nearest
