<<<<<<< HEAD
import datetime
import random
from tinydb import TinyDB, Query
import os

class Tournament:
    def __init__(self, tournament_name, place, nb_rounds=4, players = [],
                description = '', round_list = [], **kwargs):
        
        self.tournament_name = tournament_name
        self.place = place
        self.nb_rounds = nb_rounds
        self.players = players
        self.description = description
        self.round_list = round_list
    
    @property
    def start_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def end_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")
   
    def check_if_in_database(self, tournament):
        db = TinyDB('tournaments.json')
        TournamentTable = Query()
        result = db.search(TournamentTable.tournament_name == tournament.tournament_name)
        return result
    
    def add_to_database(self,tournament):
        
        db = TinyDB('tournaments.json')
        db.insert(tournament.__dict__)
        
    def sort_by_name(self, players):
        
       players = players.sort()
    
    def get_tournaments_names(self):
        db = TinyDB('tournaments.json')
        TournamentTable = Query()
        results = db.search(TournamentTable.tournament_name.exists())
        tournament_names = [result['tournament_name'] for result in results]
        return tournament_names
    
    def get_dates_names(self):
        db = TinyDB('tournaments.json')
        tournament_dict = {}
        tournaments = db.all()

        for tournament in tournaments:
            tournament_name = tournament.get('tournament_name')
            start_time = tournament.get('start_time')
            if tournament_name and start_time:
                tournament_dict[tournament_name] = start_time
        
    def all_player_by_name(self,players):
        db = TinyDB('tournaments.json')
        players = db.table('players').all()
        sorted_players = sorted(players, key=lambda x: x['name'])
        
            

        
        
        
        
    
        
    
        
        
            
        

=======
import datetime
import random
import json
import os


class Tournament:
    tournaments = []  # List to store tournament objects
    round_list = []  # List to store rounds of the tournament
    def __init__(self, tournament_name="", place="",
                 nb_rounds=4, players=[], description='',
                 round_list=None,**kwargs):
        self.tournament_name = tournament_name
        self.place = place
        self.nb_rounds = nb_rounds
        self.players = players
        self.description = description
        self.round_list = round_list
       
    
    @property
    def start_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def end_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")
   
    def check_if_in_database(self, tournament):
        tournaments = self.load_tournaments_from_file()
        result = [t for t in tournaments if t['tournament_name'] == tournament.tournament_name]
        return result
    
    def add_to_database(self, tournament):
        tournaments = self.load_tournaments_from_file()
        tournaments.append(tournament.__dict__)
        self.save_tournaments_to_file(tournaments)
        
    def sort_by_name(self, players):
        players.sort(key=lambda player: player.name)
    
    def get_tournaments_names(self):
        tournaments = self.load_tournaments_from_file()
        tournament_names = [tournament['tournament_name'] for tournament in tournaments]
        return tournament_names
    
    def get_dates_names(self):
        tournaments = LoadTournament.load_tournament_by_name()
        tournament_dict = {}

        for tournament in tournaments:
            tournament_name = tournament.get('tournament_name')
            start_time = tournament.get('start_time')
            if tournament_name and start_time:
                tournament_dict[tournament_name] = start_time
        
    def get_all_players_by_name(self):
        tournaments = self.load_tournaments_from_file()
        all_players = [player for tournament in tournaments for player in tournament['players']]
        sorted_players = sorted(all_players, key=lambda x: x['name'])
        return sorted_players
    
   
    
    def load_tournament_by_name(self, tournament_name):
        tournaments = self.load_tournaments_from_file()
        for tournament in tournaments:
            if tournament['tournament_name'] == tournament_name:
                return tournament
        
    def save_tournaments_to_file(self, tournaments):
        with open('tournaments.json', 'w') as file:
            json.dump(tournaments, file)
>>>>>>> 65e8627d2701bdb0513e83d0c76cf664d7b1c328
