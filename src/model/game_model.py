class GameModel: 
    def __init__(self): 
        self.team1_name = "Team 1" 
        self.team2_name = "Team 2" 
        self.team1_score = 0 
        self.team2_score = 0 
 
    def increment_score(self, team): 
        if team == 1: 
            self.team1_score += 1 
        elif team == 2: 
            self.team2_score += 1 
