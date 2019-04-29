import numpy as np
import pandas as pd
from Fighter import Fighter

class BattleData:
    def __init__(self):
        self.fighters = []

    def loadBattleData(self):
        fileData = pd.read_csv('candidates.csv')
        fileData = fileData.values
        for fighter in fileData:
            f = Fighter()
            f.setName(fighter[0])
            f.setHealth(fighter[1])
            f.setDamage(fighter[2])
            # f.setAttacks()
            self.fighters.append(f)

        return self.fighters

    def getFighterCount(self):
        return len(self.fighters)

    def getFighter(self, idx):
        return self.fighters[idx]

# bd = BattleData()
# print(bd.loadBattleData())

