import datetime

import json
import os


class Tournament:
    tournaments = []  # List to store tournament objects
    round_list = []  # List to store rounds of the tournament
    
    def __init__(self, tournament_name="", place="", nb_rounds=4, players=[], description='', round_list=None, start_time=None, **kwargs):
        self.tournament_name = tournament_name
        self.place = place
        self.nb_rounds = nb_rounds
        self.players = []
        self.description = description
        self.round_list = round_list
        self.start_time = start_time if start_time else self.get_current_time()
    
    @staticmethod
    def get_current_time():
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def end_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")
   
    def to_dict(self):
            return {
                'tournament_name': self.tournament_name,
                'place': self.place,
                'nb_rounds': self.nb_rounds,
                'players': [player.to_dict() for player in self.players],  # Include player data
                'description': self.description,
                'round_list': self.round_list,
                'start_time': self.start_time,
                'end_time': self.end_time
            }
        
    @staticmethod
    def json_encoder(obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, Player):
            return obj.__dict__
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")
    
    
class TournamentManager:
    def __init__(self) -> None:
        
        self.tournaments = self.load_tournaments_from_file()
        self.tournament_name = ''

   
    def save_tournaments_to_file(self):
        tournaments_data = [tournament.to_dict() for tournament in self.tournaments]  # Convert tournaments to dictionaries
        with open('tournaments.json', 'w') as file:
            json.dump(tournaments_data, file, default=Tournament.json_encoder)  # Use custom JSON encoder
            
   
    def add_to_database(cls, tournament):
        tournaments = cls.load_tournaments_from_file()
        tournaments.append(tournament.__dict__)
        cls.save_tournaments_to_file(tournaments)
    
    def load_tournament_by_name(self, tournament_name):
        tournaments = self.load_tournaments_from_file()
        for tournament in tournaments:
            if tournament.tournament_name == tournament_name:
                return tournament
        return None
        
    def load_tournaments_from_file(self):
        if not os.path.exists('tournaments.json'):
            return []
        with open('tournaments.json', 'r') as file:
            tournaments_data = json.load(file)
        self.tournaments = [Tournament(**data) for data in tournaments_data]
        return self.tournaments

    def add_player_to_tournament(self, tournament_name, player):
        for tournament in self.tournaments:
            if tournament.tournament_name == tournament_name:
                tournament.players.append(player)
                self.update_tournaments_file()
                break
            else:
                print("no tournament RRrrrrRRRRRRrRRRrRR")
                
                                    


            
    def update_tournaments_file(self):
        tournaments_data = [tournament.to_dict() for tournament in self.tournaments]  # Serialize tournament objects
        with open('tournaments.json', 'w') as file:
            json.dump(tournaments_data, file, indent=4)