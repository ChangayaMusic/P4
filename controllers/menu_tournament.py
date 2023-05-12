from views.viewtournament import AddTournamentView
from models.tournament import Tournament
class AddTournamentController:

    def __init__(self):
        self.view = AddTournamentView() 
        
    def validate_nb_rounds(self, nb_rounds):
        if nb_rounds isdigit():
            return nb_rounds
        else:
            self.view.display_nb_rounds_errors()
    
    def validate_descriptions(self, description, response): 
        if description is None:
            self.view.empty_tournament_description()
        if reponse.lower() == "yes":
            return description
        else reponse.lower() == "no":
            self.view.input_tournament_description()
            return description
                   
          
    def add_new_tournament(self):
            tournament_name = None
            place = None
            nb_rounds = 4
            description = None
            while not tournament_name:
                tournament_name = self.view.input_tournament_name()
            while not place:
                place = self.view.input_tournament_place()
            description = self.view.input_tournament_description()
            description = self.validate_descriptions
          
            tournament = Tournament(tournament_name=tournament_name, place=place, description = description)
            self.view.print_tournament_added(tournament)
            return tournament