from stopwatch_timer import StopwatchTimer
from team_model import TeamModel

class GameModel:
    def __init__(self):
        # Initialize the game with two teams
        self.team1 : TeamModel = TeamModel("Team 1")
        self.team2 : TeamModel = TeamModel("Team 2")
        self.gameClock : StopwatchTimer = None

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
        if self.gameClock == None:
            return None
        clock = self.gameClock
        if(clock.running):
            clock.stop()
        else:
            clock.start()
    
    def get_current_clock_time(self):
        if self.gameClock == None:
            return None
        return self.gameClock.current_time

    def is_game_clock_running(self):
        if self.gameClock == None:
            return None
        return self.gameClock.running

    def set_game_clock(self, time_mins, count_direction, force_set = False):
        """
        Set or reset the game clock with the specified time and counting direction.

        If the clock has not been initialized, this function will initialize the 
        game clock with the provided values. If the clock is already initialized,
        it will only reset the clock if `force_set` is set to True.

        Parameters:
        ----------
        time_mins : int
            The initial time (in minutes) for the game clock. This is the time the 
            clock will start from, or count down from, depending on the direction.
        
        count_direction : str
            The direction the clock should count. Typically 'up' for counting 
            upwards and 'down' for counting downwards. This value determines the 
            behavior of the stopwatch timer.
        
        force_set : bool, optional (default=False)
            If True, the clock will be forcibly reset to the new values even if it 
            was already initialized. If False, the function will not modify an 
            already initialized clock.
        
        Returns:
        -------
        bool
            Returns True if the game clock was successfully set or reset. Returns 
            False if the clock was already initialized and `force_set` was not True.
        
        Examples:
        --------
        Initialize a clock with 15 minutes, counting upwards:
        
            game_model.set_game_clock(15, 'up')

        Force reset the clock to 10 minutes, counting downwards:
        
            game_model.set_game_clock(10, 'down', force_set=True)
        
        """
        if(self.gameClock == None):
            self.gameClock = StopwatchTimer(time_mins, count_direction)
            return True
        elif(force_set):
            self.gameClock = StopwatchTimer(time_mins, count_direction)
            return True
        else:
            return False       

    def on_timer_tick(self, current_time):
        # This is where you handle the timer tick. Update the UI based on the current time.
        print(f"Current Time: {current_time}")
