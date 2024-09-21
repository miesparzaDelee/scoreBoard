from PyQt5.QtWidgets import QApplication 
from model.game_model import GameModel 
from viewmodel.game_viewmodel import GameViewModel 
from view.game_view import GameView 
 
if __name__ == '__main__': 
    app = QApplication([]) 
    model = GameModel() 
    viewmodel = GameViewModel(model) 
    view = GameView(viewmodel) 
    view.show() 
    app.exec_() 
