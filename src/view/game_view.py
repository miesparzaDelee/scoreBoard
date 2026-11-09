from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QInputDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from game_viewmodel import GameViewModel

class GameView(QWidget):
    def __init__(self, vm: GameViewModel):
        self.app = QApplication([])
        super().__init__()
        self.vm = vm
        
        # Team 1 UI Elements
        self.team1_logo = QLabel()
        self.team1_name = QLabel(self.vm._game_model.team1.name)  # Directly use the model
        self.team1_description = QLabel(self.vm._game_model.team1.description)
        self.team1_score = QLabel(str(self.vm.team1_score))  # Bind to viewmodel property

        # Load team 1 logo if available
        team1_logo_path = self.vm._game_model.team1.image_logo
        if team1_logo_path:
            self.team1_logo.setPixmap(QPixmap(team1_logo_path))

        # Team 2 UI Elements
        self.team2_logo = QLabel()
        self.team2_name = QLabel(self.vm._game_model.team2.name)
        self.team2_description = QLabel(self.vm._game_model.team2.description)
        self.team2_score = QLabel(str(self.vm.team2_score))  # Bind to viewmodel property

        # Load team 2 logo if available
        team2_logo_path = self.vm._game_model.team2.image_logo
        if team2_logo_path:
            self.team2_logo.setPixmap(QPixmap(team2_logo_path))

        # Buttons to update score
        self.team1_button = QPushButton('Add Point')
        self.team2_button = QPushButton('Add Point')
        
        self.team1_button.clicked.connect(self.vm.increment_team1_score)  # Use viewmodel command
        self.team2_button.clicked.connect(self.vm.increment_team2_score)  # Use viewmodel command

        # Click on team names to change them
        self.team1_name.mousePressEvent = self.change_team1_name
        self.team2_name.mousePressEvent = self.change_team2_name

        # Add Clock UI Elements
        self.clock_display = QLabel(str(self.vm.current_clock_time))  # Clock display
        self.clock_display.mousePressEvent = self.set_clock_time  # Set time when clicked

        self.start_pause_button = QPushButton('Start')  # Button to start/pause clock
        self.start_pause_button.clicked.connect(self.toggle_clock)

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

        # Layout for Clock and Buttons
        clock_layout = QVBoxLayout()
        clock_layout.addWidget(self.clock_display)
        clock_layout.addWidget(self.start_pause_button)

        # Main layout with both teams side by side and the clock below
        main_layout = QHBoxLayout()
        main_layout.addLayout(team1_layout)
        main_layout.addLayout(team2_layout)
        main_layout.addLayout(clock_layout)

        self.setLayout(main_layout)

        # Subscribe to score changes
        self.vm.add_property_changed_listener("team1_score", self.update_team1_score)
        self.vm.add_property_changed_listener("team2_score", self.update_team2_score)
        self.vm.add_property_changed_listener("team1_name", self.update_team1_name)
        self.vm.add_property_changed_listener("team2_name", self.update_team2_name)
        self.vm.add_property_changed_listener("current_clock_time", self.update_clock_display)
        self.vm.add_property_changed_listener("is_clock_running", self.update_start_pause_button)

    def update_team1_score(self):
        """Update the displayed score for Team 1 when the property changes."""
        self.team1_score.setText(str(self.vm.team1_score))

    def update_team2_score(self):
        """Update the displayed score for Team 2 when the property changes."""
        self.team2_score.setText(str(self.vm.team2_score))

    def update_team1_name(self):
        """Update the displayed name for Team 1 when the property changes."""
        self.team1_name.setText(self.vm.team1_name)

    def update_team2_name(self):
        """Update the displayed name for Team 2 when the property changes."""
        self.team2_name.setText(self.vm.team2_name)

    def update_clock_display(self):
        """Update the clock display with the current time."""
        self.clock_display.setText(f"Time: {self.vm.current_clock_time:.2f}")

    def update_start_pause_button(self):
        """Update the start/pause button text based on the clock state."""
        if self.vm.is_clock_running:
            self.start_pause_button.setText('Pause')
        else:
            self.start_pause_button.setText('Start')

    def set_clock_time(self, event):
        """
        Prompt for a new clock time and update interval when the clock is clicked, but only if the clock is stopped.
        The default update interval is set to 1 second.
        """
        if not self.vm.is_clock_running:
            # Prompt for the clock time
            new_time, ok_time = QInputDialog.getDouble(self, 'Set Clock Time', 'Enter time in minutes:')
            if ok_time:
                # Prompt for the update time, defaulting to 1 second
                update_time, ok_update = QInputDialog.getDouble(self, 'Set Update Interval', 'Enter update interval (seconds):', 1.0)
                if ok_update:
                    # Add the clock and set the update interval
                    self.vm.add_clock(new_time, 'up')  # Assuming 'up' direction for simplicity
                    self.vm.set_update_time_interval(update_time)

    def toggle_clock(self):
        """Start or pause the clock when the button is clicked."""
        self.vm.toggle_clock()

    def change_team1_name(self, event):
        """Prompt for a new name for Team 1 when clicked."""
        new_name, ok = QInputDialog.getText(self, 'Change Team 1 Name', 'Enter new name:')
        if ok:
            self.vm.team1_name = new_name

    def change_team2_name(self, event):
        """Prompt for a new name for Team 2 when clicked."""
        new_name, ok = QInputDialog.getText(self, 'Change Team 2 Name', 'Enter new name:')
        if ok:
            self.vm.team2_name = new_name
    
    # Implement AbstractView methods
    def display(self):
        """Display the game view."""
        self.show()
        self.app.exec_()

    def close(self):
        """Close the game view."""
        super().close()

    def get_type(self):
        """Return the type of the view as a string."""
        return "PC Screen"
