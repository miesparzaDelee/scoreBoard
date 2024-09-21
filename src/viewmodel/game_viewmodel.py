class GameViewModel: 
    def __init__(self, model): 
        self.model = model 
 
    def get_team1_name(self): 
        return self.model.team1_name 
 
    def get_team2_name(self): 
        return self.model.team2_name 
 
    def get_team1_score(self): 
        return str(self.model.team1_score) 
 
    def get_team2_score(self): 
        return str(self.model.team2_score) 
 
    def update_score(self, team): 
        self.model.increment_score(team) 
