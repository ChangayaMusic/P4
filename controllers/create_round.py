from views.viewround import RoundView
from models.round   import Round

class CreateRoundController:
    def __init__(self):
        self.view = RoundView()
        
    def new_round(self):
        round = Round()
        round.create_first_round()
        self.view.round_created()