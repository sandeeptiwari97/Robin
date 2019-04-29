from BattleData import BattleData
from View import View
from TournamentController import TournamentController

class Main:
    def main(self):
        print("starting new game")
        bd = BattleData()
        bd.loadBattleData()
        view = View()
        view.sendOutput("Loaded all fighter data. Count: " + str(bd.getFighterCount()))
        for i in range(bd.getFighterCount()):
            bd.getFighter(i).sendToView(view)

        tournament = TournamentController()
        tournament.start(bd, view)

        view.sendOutput('Tournament is over')
        view.sendOutput('display all fighters stats')

        for i in range(bd.getFighterCount()):
            bd.getFighter(i).sendToView(view)

bd = BattleData()
bd.loadBattleData()
model = Main()
model.main()