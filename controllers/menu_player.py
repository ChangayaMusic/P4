from views.view_player import AddPlayerView
from models.player import Player
from datetime import datetime
import re


class AddPlayerController:
    def __init__(self, player_manager):
        self.view = AddPlayerView()
        self.player_manager = player_manager

    def validate_identification(self, identification):
        pattern = r'^[a-zA-Z]{2}\d{5}$'
        if re.match(pattern, identification):
            return identification
        else:
            self.view.display_identification_error()
            return None

    def validate_birth_date(self, date_string):
        try:
            birth_date = datetime.strptime(date_string, "%Y%m%d")
            return birth_date
        except ValueError:
            return None

    def add_player_to_db(self, player):
        in_db = self.player_manager.check(player)
        if in_db:
            self.view.already_in_db(player)
        else:
            self.player_manager.add(player)
            self.view.bd_validation(player)

        self.view.print_player_added(player)

    def add_new_player(self):

        identification = None
        first_name = None
        last_name = None
        birth_date = None
        date_string = None
        while not first_name:
            first_name = self.view.input_first_name()
        while not last_name:
            last_name = self.view.input_last_name()
        while not identification:
            identification = self.view.input_identification()
            identification = self.validate_identification(
                identification)  # validate identification

        while not birth_date:
            try:
                date_string = self.view.input_birth_date()
                birth_date = self.validate_birth_date(date_string)
            except ValueError:
                self.view.display_birth_date_error()

        player = Player(last_name=last_name,
                        first_name=first_name,
                        birth_date=birth_date,
                        identification=identification)
        self.add_player_to_db(player)

        return player
