from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap

class GameView(QWidget):
    def __init__(self, viewmodel):
        super().__init__()
        self.viewmodel = viewmodel
        
        # Team 1 UI Elements
        self.team1_logo = QLabel()
        self.team1_name = QLabel(self.viewmodel._game_model.team1.name)  # Directly use the model
        self.team1_description = QLabel(self.viewmodel._game_model.team1.description)
        self.team1_score = QLabel(str(self.viewmodel.team1_score))  # Bind to viewmodel property

        # Load team 1 logo if available
        team1_logo_path = self.viewmodel._game_model.team1.image_logo
        if team1_logo_path:
            self.team1_logo.setPixmap(QPixmap(team1_logo_path))

        # Team 2 UI Elements
        self.team2_logo = QLabel()
        self.team2_name = QLabel(self.viewmodel._game_model.team2.name)
        self.team2_description = QLabel(self.viewmodel._game_model.team2.description)
        self.team2_score = QLabel(str(self.viewmodel.team2_score))  # Bind to viewmodel property

        # Load team 2 logo if available
        team2_logo_path = self.viewmodel._game_model.team2.image_logo
        if team2_logo_path:
            self.team2_logo.setPixmap(QPixmap(team2_logo_path))

        # Buttons to update score
        self.team1_button = QPushButton('Add Point to Team 1')
        self.team2_button = QPushButton('Add Point to Team 2')
        
        self.team1_button.clicked.connect(self.viewmodel.increment_team1_score)  # Use viewmodel command
        self.team2_button.clicked.connect(self.viewmodel.increment_team2_score)  # Use viewmodel command

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

        # Subscribe to score changes
        self.viewmodel.add_property_changed_listener("team1_score", self.update_team1_score)
        self.viewmodel.add_property_changed_listener("team2_score", self.update_team2_score)

    def update_team1_score(self):
        """Update the displayed score for Team 1 when the property changes."""
        self.team1_score.setText(str(self.viewmodel.team1_score))

    def update_team2_score(self):
        """Update the displayed score for Team 2 when the property changes."""
        self.team2_score.setText(str(self.viewmodel.team2_score))
