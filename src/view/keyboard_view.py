import threading
import keyboard
from abstract_view import AbstractView
from vm.game_viewmodel import GameViewModel

class KeyboardView(AbstractView):
    def __init__(self, viewmodel: GameViewModel):
        self._type = "keyboard"
        self.viewmodel = viewmodel
        self._thread = None

    def display(self):
        """Override the abstract display method to start the keyboard listener in a separate thread."""
        print("Keyboard control active. Press '1' to increment Team 1's score, '2' to increment Team 2's score.")
        if self._thread is None:
            self._thread = threading.Thread(target=self._run_keyboard_listener)
            self._thread.start()

    def close(self):
        """Override the abstract close method."""
        print("Keyboard control closed.")
        keyboard.unhook_all_hotkeys()  # Stop listening for hotkeys
        if self._thread:
            self._thread.join()  # Ensure the thread finishes

    def get_type(self):
        """Return the view type."""
        return self._type

    def _run_keyboard_listener(self):
        """Private method to handle the keyboard listener in a separate thread."""
        keyboard.add_hotkey('1', self.viewmodel.increment_team1_score)
        keyboard.add_hotkey('2', self.viewmodel.increment_team2_score)

        # Wait for 'esc' to stop the listener
        print("Press 'esc' to stop keyboard control.")
        keyboard.wait('esc')
        self.close()

# Example usage
if __name__ == "__main__":
    # Dummy GameModel and GameViewModel for demonstration purposes
    class GameModel:
        pass

    class DummyGameViewModel(GameViewModel):
        def __init__(self, model):
            super().__init__(model)
        
        def increment_team1_score(self):
            print("Team 1 score incremented")

        def increment_team2_score(self):
            print("Team 2 score incremented")

    # Initialize the GameModel and GameViewModel
    game_model = GameModel()
    game_viewmodel = DummyGameViewModel(game_model)

    # Initialize the KeyboardView
    keyboard_view = KeyboardView(game_viewmodel)
    keyboard_view.display()
