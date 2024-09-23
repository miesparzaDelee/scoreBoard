from model.stopwatch_timer import StopwatchTimer
from model.team_model import TeamModel

class GameModel:
    def __init__(self):
        # Initialize the game with two teams
        self.team1 = TeamModel("Team 1")
        self.team2 = TeamModel("Team 2")
        #self.gameTime = GameTimeModel()

    def increment_team_score(self, team_number, points=1):
        """
        Increment the score of the specified team by a given number of points.
        
        :param team_number: 1 for team1, 2 for team2
        :param points: Number of points to add (default is 1)
        """
        if team_number == 1:
            self.team1.increment_score(points)
        elif team_number == 2:
            self.team2.increment_score(points)
