import uuid


class Match:
    def __init__(self, player_1, player_2, match_id=uuid.uuid4()):
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_score = 0
        self.player_2_score = 0
        self.match_id = match_id

    @property
    def is_equality(self):
        return self.player_1_score != 0 and self.player_2_score != 0 \
            and self.player_1_score == self.player_2_score

    def set_result(self, result):
        if result == result.PLAYER_1_WINS:
            self.player_1_score = 1
        elif result == result.PLAYER_2_WINS:
            self.player_2_score = 1
        elif result == result.EQUALITY:
            self.player_1_score = self.player_2_score = 0.5
        else:
            raise ValueError("Unknown result match value")
