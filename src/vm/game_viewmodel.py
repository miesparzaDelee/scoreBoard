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
        self.continue_pause_command = Command(self.pause_continue)

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

    def increment_team1_score(self):
        self._game_model.increment_team_score(1)  # Call model to increment score
        self.notify_property_changed("team1_score")  # Notify the UI of the change

    def increment_team2_score(self):
        self._game_model.increment_team_score(2)  # Call model to increment score
        self.notify_property_changed("team2_score")  # Notify the UI of the change

    def pause_continue(self):
        self._game_model.pause_continue_game_clock()
        self.notify_property_changed("is_clock_running")

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
        print(f"Team 1 Score: {game_vm.team1_score}")
        print(f"Team 2 Score: {game_vm.team2_score}")
        print(f"Team 1 Name: {game_vm.team1_name}")
        print(f"Team 2 Name: {game_vm.team2_name}")
        print(f"Clock Status: {game_vm.is_clock_running}")
    
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
    
    print("\nStarting clock:")
    game_vm.pause_continue()

    time.sleep(5)
    
    print("\nStopping clock:")
    game_vm.pause_continue()