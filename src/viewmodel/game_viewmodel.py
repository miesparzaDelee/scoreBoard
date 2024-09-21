class GameViewModel:
    def __init__(self, model):
        self.model = model

    def get_team1_name(self):
        return self.model.team1.name

    def get_team1_score(self):
        return str(self.model.team1.score)

    def get_team1_logo(self):
        return self.model.team1.image_logo

    def get_team1_description(self):
        return self.model.team1.description

    def get_team2_name(self):
        return self.model.team2.name

    def get_team2_score(self):
        return str(self.model.team2.score)

    def get_team2_logo(self):
        return self.model.team2.image_logo

    def get_team2_description(self):
        return self.model.team2.description

    def update_team_score(self, team_number, points=1):
        self.model.increment_team_score(team_number, points)
