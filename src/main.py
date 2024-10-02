import threading
from hardware_manager import HardwareManager
from model.game_model import GameModel 
from vm.game_viewmodel import GameViewModel 
from view.game_view import GameView 
from view_manager_viewmodel import ViewManager
from keyboard_view import KeyboardView

def run_keyboard_view(keyboard_view):
    """Function to run the KeyboardView in a separate thread."""
    keyboard_view.display()  # This will block and listen for keyboard input

if __name__ == '__main__':
    hw_man = HardwareManager()
    game_vm = GameViewModel(GameModel()) 
    view_man_vm = ViewManager()

    if hw_man.has_connected_keyboard:
        keyboard_view = KeyboardView(game_vm)
        view_man_vm.add_view(keyboard_view)
        keyboard_thread = threading.Thread(target=run_keyboard_view, args=(keyboard_view,))
        keyboard_thread.start()  # Run the keyboard view in a separate thread
    
    if len(hw_man.connected_screens) > 1:
        screen_view = GameView(game_vm)
        view_man_vm.add_view(screen_view)
    
