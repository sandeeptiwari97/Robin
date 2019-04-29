from View import View

class Fighter:
    def __init__(self):
        self.losses = 0
        self.wins = 0

    def sendToView(self, view):
        view.sendOutput(self.toString())

    def toString(self):
        sb = ''
        sb += 'Name: ' + self.name
        sb += ', Health: ' + str(self.health)
        sb += ', Damage: ' + str(self.damage)
        sb += ', Win Count: ' + str(self.wins)
        return [self.name, self.wins]

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def setHealth(self, health):
        self.health = health

    def getDamage(self):
        return self.damage

    def setDamage(self, damage):
        self.damage = damage

    def setAttacks(self, attacks):
        self.attacks = attacks

    def getAttacks(self):
        return self.attacks

    def getWins(self):
        return self.wins

    def setWins(self, wins):
        self.wins = wins
