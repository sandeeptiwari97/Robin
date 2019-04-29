from BattleData import BattleData
from Fighter import Fighter
from View import View
from MatchController import MatchController

class TournamentController:
    def start(self, bd, view):
        round = 0
        for i in range(bd.getFighterCount()):
            dude = bd.getFighter(i)
            for j in range(bd.getFighterCount()):
                otherdude = bd.getFighter(j)
                round += 1
                match = MatchController(dude, otherdude, round)
                view.sendOutput("*******************************************************************")
                view.sendOutput("****************           MATCH START           ******************")
                view.sendOutput("*******************************************************************")
                match.start(view)
                view.sendOutput("*******************************************************************")
                view.sendOutput("****************           MATCH END             ******************")
                view.sendOutput("*******************************************************************")
