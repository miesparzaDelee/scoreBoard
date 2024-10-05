from stopwatch_timer import StopwatchTimer
from team_model import TeamModel

class GameModel:
    def __init__(self):
        # Initialize the game with two teams
        self.team1 : TeamModel = TeamModel("Team 1")
        self.team2 : TeamModel = TeamModel("Team 2")
        self.gameClock : StopwatchTimer = StopwatchTimer(15,"up")
        #self.gameClock.subscribe_on_elapsed(self.on_timer_tick, 1)

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

    def set_team_name(self, team_number, new_name):
            """
            Set the name of the specified team.
            
            :param team_number: 1 for team1, 2 for team2
            :param new_name: The new name for the team
            """
            if team_number == 1:
                self.team1.name = new_name
            elif team_number == 2:
                self.team2.name = new_name

    def pause_continue_game_clock(self):
        clock = self.gameClock
        if(clock.running):
            clock.stop()
        else:
            clock.start()
    
    def get_current_clock_time(self):
        return self.gameClock.current_time

    def is_game_clock_running(self):
        return self.gameClock.running

    def on_timer_tick(self, current_time):
        # This is where you handle the timer tick. Update the UI based on the current time.
        print(f"Current Time: {current_time}")
