from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton 
 
class GameView(QWidget): 
    def __init__(self, viewmodel): 
        super().__init__() 
        self.viewmodel = viewmodel 
 
        self.team1_label = QLabel(self.viewmodel.get_team1_name()) 
        self.team1_score = QLabel(self.viewmodel.get_team1_score()) 
        self.team2_label = QLabel(self.viewmodel.get_team2_name()) 
        self.team2_score = QLabel(self.viewmodel.get_team2_score()) 
 
        self.team1_button = QPushButton('Add Point to Team 1') 
        self.team2_button = QPushButton('Add Point to Team 2') 
 
        self.team1_button.clicked.connect(self.update_team1_score) 
        self.team2_button.clicked.connect(self.update_team2_score) 
 
        layout = QVBoxLayout() 
        layout.addWidget(self.team1_label) 
        layout.addWidget(self.team1_score) 
        layout.addWidget(self.team1_button) 
        layout.addWidget(self.team2_label) 
        layout.addWidget(self.team2_score) 
        layout.addWidget(self.team2_button) 
        self.setLayout(layout) 
 
    def update_team1_score(self): 
        self.viewmodel.update_score(1) 
        self.team1_score.setText(self.viewmodel.get_team1_score()) 
 
    def update_team2_score(self): 
        self.viewmodel.update_score(2) 
        self.team2_score.setText(self.viewmodel.get_team2_score()) 
