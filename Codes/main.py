"""
This module serves as the entry point for the maze solver application.

It initializes the main application class, MainApp, which in turn creates and manages the MazeUI for interacting with
the maze. The application allows users to generate mazes of specified sizes, choose a solving algorithm, and visualize
the algorithm's solution path through the maze.

Author: Peyman Kh
Date: 09/Feb/2024
"""

from ui import MazeUI


class MainApp:
    """
    The main application class responsible for initializing and running the maze solver GUI.

    Parameters:
        - maze_ui (MazeUI): An instance of the MazeUI class for managing the maze solver GUI.
    """
    def __init__(self, rows=20, cols=20):
        """
        Initializes the MainApp with a MazeUI instance.

        Parameters:
            - rows (int): The number of rows for the maze. Defaults to 20.
            - cols (int): The number of columns for the maze. Defaults to 20.
        """
        self.maze_ui = MazeUI(rows, cols)   # Create the maze UI with specified dimensions.

    def run(self):
        """Starts the maze solver application."""
        self.maze_ui.run()


if __name__ == "__main__":
    n1 = int(input('Enter the number of maze rows: '))  # User input for the number of maze rows.
    n2 = int(input('Enter the number of maze columns: '))  # User input for the number of maze columns.
    app = MainApp(n1, n2)  # Create an instance of the MainApp.
    app.run()  # Run the application.
