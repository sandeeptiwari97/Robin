from Fighter import Fighter
from View import View
import numpy as np

class MatchController:

    class MatchDude:
        def __init__(self, dude):
            self.fighter = dude
            # self.attacksRemaining = dude.getAttacks()
        def getHealth(self):
            return self.fighter.getHealth()

        def getDamage(self):
            return self.fighter.getDamage()

        def slap(self, damage):
            currHealth = self.fighter.getHealth()
            currHealth -= damage
            self.fighter.setHealth(currHealth)
            print('slapped')

        def getName(self):
            return self.fighter.getName()

        def win(self):
            wins = self.fighter.getWins()
            wins += 1
            self.fighter.setWins(wins)


    def __init__(self, dude, otherdude, round):
        self.dudes = []
        self.dudes.append(self.MatchDude(dude))
        self.dudes.append(self.MatchDude(otherdude))
        self.round = round

    def start(self, view):
        self.view = view
        view.sendOutput("");
        view.sendOutput("Candidate 1:" + self.dudes[0].getName())
        view.sendOutput("\tHealth: " + str(self.dudes[0].getHealth()))
        view.sendOutput("\tDamage: " + str(self.dudes[0].getDamage()))
        view.sendOutput("");
        view.sendOutput("Candidate 2:" + str(self.dudes[1].getName()))
        view.sendOutput("\tHealth: " + str(self.dudes[1].getHealth()))
        view.sendOutput("\tDamage: " + str(self.dudes[1].getDamage()))
        view.sendOutput("");
        view.sendOutput("Round :" + str(self.round))

        istart = self.randomStart()

        if istart == 0:
            view.sendOutput(self.dudes[0].getName())
        else:
            view.sendOutput(self.dudes[1].getName() + ' is randomly selected to go first')

        while not self.isFightDone():
            print('fighting....')
            self.attack(istart)
            istart += 1
            if istart > 1:
                istart = 0

        self.decideWinner()


    def randomStart(self):
        min, max = 0, 1
        randNum = min + int(np.random.rand()*max)
        return randNum

    def isFightDone(self):
        if self.dudes[0].getHealth() <= 0 or self.dudes[1].getHealth() <= 0:
            return True
        return False

    def attack(self, iDudeAttacking):
        damage = self.dudes[iDudeAttacking].getDamage()

        punchingBag = iDudeAttacking+1
        if punchingBag > 1:
            punchingBag = 0
        prevHealth = self.dudes[punchingBag].getHealth()
        self.view.sendOutput(self.dudes[iDudeAttacking].getName() + ' hits ' +
                        self.dudes[punchingBag].getName() + ' ' + str(damage) + ' damage '+
                        "( " + str(prevHealth) + ' -> ' + str(prevHealth-damage) + ' )')

        self.dudes[punchingBag].slap(damage)

    def decideWinner(self):
        if self.dudes[0].getHealth() < self.dudes[1].getHealth():
            self.dudes[1].win()
            self.view.sendOutput(self.dudes[1].getName() + ' wins!')
        else:
            self.dudes[0].win()
            self.view.sendOutput(self.dudes[0].getName() + ' wins!')



