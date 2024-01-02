from assets import organism

class Plant(organism.Organism):
    def __init__(self, x, y, world, strength, initiative, name, range):
        super().__init__(x, y, world, strength, initiative, name, range)

    def action(self):
        self.reproduction()

    def collision(self, org):
        return True

    def isPlant(self):
        return True

    def isEatenBy(self, org):
        self.dies()
        return True