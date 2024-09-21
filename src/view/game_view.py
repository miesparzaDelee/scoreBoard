from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap

class GameView(QWidget):
    def __init__(self, viewmodel):
        super().__init__()
        self.viewmodel = viewmodel
        
        # Team 1 UI Elements
        self.team1_logo = QLabel()
        self.team1_name = QLabel(self.viewmodel.get_team1_name())
        self.team1_description = QLabel(self.viewmodel.get_team1_description())
        self.team1_score = QLabel(self.viewmodel.get_team1_score())

        # Load team 1 logo if available
        team1_logo_path = self.viewmodel.get_team1_logo()
        if team1_logo_path:
            self.team1_logo.setPixmap(QPixmap(team1_logo_path))

        # Team 2 UI Elements
        self.team2_logo = QLabel()
        self.team2_name = QLabel(self.viewmodel.get_team2_name())
        self.team2_description = QLabel(self.viewmodel.get_team2_description())
        self.team2_score = QLabel(self.viewmodel.get_team2_score())

        # Load team 2 logo if available
        team2_logo_path = self.viewmodel.get_team2_logo()
        if team2_logo_path:
            self.team2_logo.setPixmap(QPixmap(team2_logo_path))

        # Buttons to update score
        self.team1_button = QPushButton('Add Point to Team 1')
        self.team2_button = QPushButton('Add Point to Team 2')
        
        self.team1_button.clicked.connect(self.update_team1_score)
        self.team2_button.clicked.connect(self.update_team2_score)

        # Layout for Team 1
        team1_layout = QVBoxLayout()
        team1_layout.addWidget(self.team1_logo)
        team1_layout.addWidget(self.team1_name)
        team1_layout.addWidget(self.team1_description)
        team1_layout.addWidget(self.team1_score)
        team1_layout.addWidget(self.team1_button)

        # Layout for Team 2
        team2_layout = QVBoxLayout()
        team2_layout.addWidget(self.team2_logo)
        team2_layout.addWidget(self.team2_name)
        team2_layout.addWidget(self.team2_description)
        team2_layout.addWidget(self.team2_score)
        team2_layout.addWidget(self.team2_button)

        # Main layout with both teams side by side
        main_layout = QHBoxLayout()
        main_layout.addLayout(team1_layout)
        main_layout.addLayout(team2_layout)

        self.setLayout(main_layout)

    def update_team1_score(self):
        self.viewmodel.update_team_score(1)
        self.team1_score.setText(self.viewmodel.get_team1_score())

    def update_team2_score(self):
        self.viewmodel.update_team_score(2)
        self.team2_score.setText(self.viewmodel.get_team2_score())
