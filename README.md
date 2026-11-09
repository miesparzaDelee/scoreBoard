
# Sports Scoreboard

A cross-platform sports scoreboard application for Windows and Raspberry Pi, built using Python and PyQt5. This application follows a Model-View-ViewModel (MVVM) architecture to separate business logic from the user interface, allowing for clean code organization and scalability.

## Features

- **Cross-platform**: Runs on both Windows and Raspberry Pi.
- **MVVM Architecture**: Ensures separation of concerns between the UI and business logic.
- **Keyboard control**: Initially designed for keyboard input with future plans for remote control (Bluetooth/Wi-Fi) and custom physical scoreboard integration.

## Requirements

- **Python** 3.6 or higher
- **PyQt5** 5.15.4 or higher
- **pytest** for running unit tests

## Installation

### 1. Clone the Repository

First, clone the GitHub repository to your local machine:

```bash
git clone https://github.com/yourusername/sports-scoreboard.git
cd sports-scoreboard
```

### 2. Create and Activate a Virtual Environment

It is recommended to create a virtual environment to manage the project dependencies.

- On **Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

- On **Linux/Raspberry Pi**:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

Once the virtual environment is activated, install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This will install:

- **PyQt5**: For the user interface.
- **pytest**: For running unit tests.

## Running the Application from Terminal

After the dependencies are installed, you can run the application using the following command:

```bash
python src/main.py
```

This will launch the sports scoreboard interface.

## Running Unit Tests from Terminal

To run unit tests for the business logic, make sure you are in the root directory of the project and then run:

```bash
pytest
```

This will run all the tests located in the `tests/` directory.

## Project Structure

The project follows a clear separation of concerns using the MVVM architecture. Here's an overview of the directory structure:

```plaintext
sports-scoreboard/
├── README.md             # Project overview and setup instructions
├── requirements.txt      # Project dependencies
├── .gitignore            # Git ignore file
├── src/                  # Source code for the application
│   ├── model/            # Model layer (business logic)
│   ├── vm/        # ViewModel layer (connects model and view)
│   ├── view/             # View layer (UI components)
│   └── main.py           # Application entry point
└── tests/                # Unit tests for the application
```

- **Model Layer** (`src/model/`): Handles the core game logic (teams, scores, etc.).
- **ViewModel Layer** (`src/vm/`): Connects the data between the Model and View.
- **View Layer** (`src/view/`): Defines the user interface with PyQt5.
- **Main Entry Point** (`src/main.py`): The entry point for running the application.
- **Unit Tests** (`tests/`): Unit tests for the model and logic.

## VSCODE Development Environment Setup

This project uses VSCode to manage and run different components of the application, such as running the main app, running individual files for testing or usage examples, and running unit tests. Below is a guide to help you run and debug the code effectively.

### Running or Debugging the Application

To run or debug the full application:

1. Open the **Run and Debug** tab on the left side panel in VSCode (shortcut: `Ctrl+Shift+D`).
2. Select the configuration labeled **"Run Scoreboard Program"** from the dropdown.
3. Click the **green play button** or hit `F5` to run the app.

This will launch the entire application and execute the code from the `src/main.py` file.

### Running a Single File with the Run File Button

VSCode also allows you to quickly run or debug individual files using the **Run Python File** button:

1. Open the Python file you want to run, for example, `game_viewmodel.py`.
2. Click the **Run Python File** button in the top right corner of the editor or use the shortcut `Ctrl+F5`.

This will run the file directly in the integrated terminal. If the file includes a `__main__` section (e.g., usage example code), that section will be executed.

#### Important Notes

- Ensure your Python environment is correctly set up in VSCode.
- The `PYTHONPATH` is dynamically set in the code to include the `src` folder for module imports. This is essential when running individual files.

### Running Unit Tests

To run unit tests:

1. Open the **Testing** tab in VSCode (shortcut: `Ctrl+Shift+T`).
2. Click **Run Tests** to execute all available unit tests in the project.
3. You can also run or debug individual tests by clicking on the test cases listed in the **Testing** tab.

The tests are configured to automatically discover and run the test files from the `tests` directory.


# Programming Paradigm and Feature Addition Guidelines

This project follows the **Model-View-ViewModel (MVVM)** architectural pattern, which separates the application logic (business rules) from the user interface (UI) layer. This structure ensures clean separation of concerns and makes the application easier to maintain, scale, and test.

## Key Components

### 1. **Model**

- The model contains the **business logic** and represents the state of the application.
- It holds core data (e.g., team scores, game time, periods) and implements logic to manipulate that data (e.g., incrementing a score, changing periods).
- Models are fully **unit tested** to ensure the correctness of business rules and data manipulation.

### 2. **ViewModel**

- The ViewModel acts as an **intermediary** between the Model and the View.
- It exposes **properties** and **commands** for the View to bind to, making the ViewModel responsible for providing the UI with data (from the Model) and handling user input (via commands).
- The ViewModel does not directly reference UI components; instead, it manages application state and logic in a way that can be consumed by the View.
- `__main__` blocks are used in ViewModels to provide examples of usage and demonstrate their behavior without requiring a UI.

### 3. **View**

- The View is the **UI layer** and is responsible for rendering data and responding to user actions.
- It binds to the ViewModel to display data and execute commands (e.g., displaying a score, allowing the user to change the game period).
- The View does not contain business logic; it focuses purely on user interaction.

---

## How to Add New Features

The following steps outline how to add new features to the project following the MVVM pattern. The focus is on ensuring clean separation of concerns, comprehensive testing for the model, and clear examples for the ViewModel.

### 1. **Update the Model**

- **Add new data or logic** to the model class that represents the core of the feature.
  - Example: If you’re adding game periods, add properties like `current_period` and `total_periods` to the `GameModel`.
- Add methods to the model to manipulate the feature's data.
  - Example: `next_period()` in `GameModel` to advance the game to the next period.
- **Write unit tests** to cover the new feature in the model. The tests should verify that the model behaves as expected, especially for edge cases.

   ```python
   import unittest
   from model.game_model import GameModel

   class TestGameModel(unittest.TestCase):
       def test_next_period(self):
           game = GameModel()
           self.assertEqual(game.current_period, 1)
           game.next_period()
           self.assertEqual(game.current_period, 2)

       def test_no_periods_after_max(self):
           game = GameModel()
           for _ in range(5):  # More than total periods
               game.next_period()
           self.assertEqual(game.current_period, game.total_periods)

   if __name__ == '__main__':
       unittest.main()
   ```

### 2. **Update the ViewModel**

- **Expose the feature** from the model via properties or commands in the ViewModel.
  - Example: Add a `current_period` property in the `GameViewModel` that returns the current period from the `GameModel`.
- Add commands to manipulate the model from the ViewModel.
  - Example: Add a `next_period()` command to the `GameViewModel` that calls the corresponding method in the `GameModel`.
- Include a `__main__` block that shows how the ViewModel interacts with the model. This serves as an example or informal test for the ViewModel logic.

   ```python
   if __name__ == "__main__":
       game_model = GameModel()
       game_vm = GameViewModel(game_model)

       print(f"Initial period: {game_vm.current_period}")
       game_vm.next_period()
       print(f"After next period: {game_vm.current_period}")
   ```

### 3. **Update the View**

- **Add UI elements** to display and interact with the new feature in the view.
  - Example: Add a `QLabel` to display the current period and a `QPushButton` to allow the user to switch to the next period.
- **Bind the ViewModel** properties and commands to the UI components, ensuring the ViewModel handles all the logic and the View is purely for interaction.
- Manually test the View by running the application and verifying that the UI updates correctly when interacting with the new feature.

   ```python
   from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton

   class GameView(QWidget):
       def __init__(self, vm: GameViewModel):
           super().__init__()
           self.vm = vm

           # Period Display and Button
           self.period_label = QLabel(f"Period: {self.vm.current_period} of {self.vm.total_periods}")
           self.next_period_button = QPushButton('Next Period')
           self.next_period_button.clicked.connect(self.vm.next_period)

           # Layout
           layout = QVBoxLayout()
           layout.addWidget(self.period_label)
           layout.addWidget(self.next_period_button)
           self.setLayout(layout)

           # Subscribe to period change
           self.vm.add_property_changed_listener("current_period", self.update_period_display)

       def update_period_display(self):
           """Update the displayed period when it changes."""
           self.period_label.setText(f"Period: {self.vm.current_period} of {self.vm.total_periods}")
   ```

### 4. **Testing and Iteration**

- **Run unit tests** for the model to ensure the business logic is correct.
- Test the ViewModel with the `__main__` block to ensure that it interacts with the model properly.
- **Manually test the view** by running the application to check how the UI interacts with the new feature.
- Iterate as needed to refine the feature.

---

### Conclusion

The MVVM pattern ensures that features are added in a modular way, with clear separation between the business logic (Model), the interaction logic (ViewModel), and the UI (View). The model is fully unit tested, and `__main__` blocks in the ViewModel provide usage examples to demonstrate how the logic works. This approach enables scalability and maintainability, making the application robust and adaptable to future changes.
