from assets import plant


class PineBorscht(plant.Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 10, 0, "PineBorscht", 1)

    def isEatenBy(self, org):
        if (not org.isCyberSheep()):
            org.getWorld().getGUI().logAteDeath(org, self)
            org.dies()

        return super().isEatenBy(org)

    def kills(self, org):
        self.getWorld().getGUI().logPineBorscht(org, self)
        org.dies()

    def action(self):
        positions = ([-1, 0], [1, 0], [0, -1], [0, 1])

        for pos in positions:
            if not self.getWorld().isEmpty(self.getX() + pos[0], self.getY() + pos[1]):
                if self.getWorld().getOrganism(self.getX() + pos[0], self.getY() + pos[1]).isAnimal():
                    if not self.getWorld().getOrganism(self.getX() + pos[0], self.getY() + pos[1]).isCyberSheep():
                        self.kills(self.getWorld().getOrganism(self.getX() + pos[0], self.getY() + pos[1]))

        super().action()
        