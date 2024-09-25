
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

## Running the Application

After the dependencies are installed, you can run the application using the following command:

```bash
python src/main.py
```

This will launch the sports scoreboard interface.

## Running Unit Tests

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
│   ├── viewmodel/        # ViewModel layer (connects model and view)
│   ├── view/             # View layer (UI components)
│   └── main.py           # Application entry point
└── tests/                # Unit tests for the application
```

- **Model Layer** (`src/model/`): Handles the core game logic (teams, scores, etc.).
- **ViewModel Layer** (`src/viewmodel/`): Connects the data between the Model and View.
- **View Layer** (`src/view/`): Defines the user interface with PyQt5.
- **Main Entry Point** (`src/main.py`): The entry point for running the application.
- **Unit Tests** (`tests/`): Unit tests for the model and logic.

## Development Environment Setup

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

#### Important Notes:
- Ensure your Python environment is correctly set up in VSCode.
- The `PYTHONPATH` is dynamically set in the code to include the `src` folder for module imports. This is essential when running individual files.

### Running Unit Tests
To run unit tests:

1. Open the **Testing** tab in VSCode (shortcut: `Ctrl+Shift+T`).
2. Click **Run Tests** to execute all available unit tests in the project.
3. You can also run or debug individual tests by clicking on the test cases listed in the **Testing** tab.

The tests are configured to automatically discover and run the test files from the `tests` directory.

