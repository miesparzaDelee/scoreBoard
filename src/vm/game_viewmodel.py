from PropertyChangedNotifier import PropertyChangedNotifier
from Command import Command
from model.game_model import GameModel

class GameViewModel(PropertyChangedNotifier):
    def __init__(self, game_model: GameModel):
        super().__init__()
        self._game_model:GameModel = game_model  # Store the reference to the model

        # Commands for updating the scores
        self.increment_team1_score_command = Command(self.increment_team1_score)
        self.increment_team2_score_command = Command(self.increment_team2_score)
        # Commands for clock
        self.add_clock_command = Command(self.add_clock)
        self.toggle_clock_command = Command(self.toggle_clock)
        self.set_update_time_interval_command = Command(self.set_update_time_interval)

    @property
    def team1_score(self):
        return self._game_model.team1.score  # Expose the team1 score

    @property
    def team2_score(self):
        return self._game_model.team2.score  # Expose the team2 score
    
    @property
    def team1_name(self):
        return self._game_model.team1.name

    @team1_name.setter
    def team1_name(self, value):
        self._game_model.team1.name = value  # Set the team1 name
        self.notify_property_changed("team1_name")

    @property
    def team2_name(self):
        return self._game_model.team2.name

    @team2_name.setter
    def team2_name(self, value):
        self._game_model.team2.name = value  # Set the team1 name
        self.notify_property_changed("team2_name")

    @property
    def is_clock_running(self):
        return self._game_model.is_game_clock_running()  # Expose the team1 score

    @property
    def has_clock(self):
        return self._game_model.gameClock != None
    
    @property
    def current_clock_time(self):
        return self._game_model.get_current_clock_time()

    def increment_team1_score(self):
        self._game_model.increment_team_score(1)  # Call model to increment score
        self.notify_property_changed("team1_score")  # Notify the UI of the change

    def increment_team2_score(self):
        self._game_model.increment_team_score(2)  # Call model to increment score
        self.notify_property_changed("team2_score")  # Notify the UI of the change

    def toggle_clock(self):
        """
        Toggles the game clock between running and paused states.
        """
        self._game_model.pause_continue_game_clock()
        self.notify_property_changed("is_clock_running")

    def add_clock(self, time_mins, direction):
        """
        Adds or initializes the game clock with the given time and direction.
        Notifies the UI if the clock is successfully initialized.
        """
        if time_mins <= 0 or direction not in ["up", "down"]:
            return   
        if self._game_model.set_game_clock(time_mins,direction):
            self.notify_property_changed("has_clock")
    
    def set_update_time_interval(self, update_time_secs):
        """
        Sets the interval at which the clock's elapsed time is updated and notifies the view.

        :param update_time_secs: The time in seconds between each update event.
        """
        if self.has_clock and update_time_secs > 0:
            self._game_model.gameClock.subscribe_on_elapsed(self._elapsed_time, update_time_secs)
    
    def _elapsed_time(self, currentTime):
        """
        Callback method triggered when the clock reaches the elapsed time.
        """
        self.notify_property_changed("current_clock_time")
        
# Example to demonstrate the working of GameViewModel
if __name__ == "__main__":
    from model.game_model import GameModel
    import time
    # Initialize the game model
    game_model = GameModel()

    # Initialize the view model
    game_vm = GameViewModel(game_model)

    # Simulate a property change handler
    def on_property_changed(property_name):
        print(f"Property '{property_name}' changed")
        if property_name in ["team1_score", "team2_score"]:
            print(f"Team 1 Score: {game_vm.team1_score}")
            print(f"Team 2 Score: {game_vm.team2_score}")
        if property_name in ["team1_name", "team2_name"]:
            print(f"Team 1 Name: {game_vm.team1_name}")
            print(f"Team 2 Name: {game_vm.team2_name}")
        if property_name == "is_clock_running":
            print(f"Clock Status: {game_vm.is_clock_running}")
        if property_name == "has_clock":
            print(f"Has Clock?: {game_vm.has_clock}")
        if property_name == "current_clock_time":
            print(f"Current Time: {game_vm.current_clock_time:.2f} secs")

    # Subscribe to property changes
    game_vm.subscribe_property_changed(on_property_changed)

    # Simulate some game actions
    print("Incrementing Team 1 Score:")
    game_vm.increment_team1_score()

    print("\nIncrementing Team 2 Score:")
    game_vm.increment_team2_score()

    print("\nIncrementing Team 1 Score again:")
    game_vm.increment_team1_score()

    print("\nSetting a new name:")
    game_vm.team1_name = "Chivas"
    game_vm.team2_name = "America"
    
    # add 1 minute clock
    print("\nAdding a clock:")
    game_vm.add_clock(1,"up")

    game_vm.set_update_time_interval(1)
    # start stop clock
    print("\nStarting clock:")
    game_vm.toggle_clock()

    time.sleep(5)
    
    print("\nStopping clock:")
    game_vm.toggle_clock()
