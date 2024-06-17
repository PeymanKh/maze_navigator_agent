"""
This module provides a graphical user interface for visualizing and interacting with a maze.

It leverages the tkinter library to create a window where users can generate mazes, choose a solving algorithm,
and visually follow the algorithm's progress towards solving the maze.

Author: Peyman Kh
Date: 07/Feb/2024
"""
# Import libraries
import tkinter as tk
from maze import Maze
from agent import Agent
import time


class MazeUI:
    """A class to create and manage the maze solving GUI."""

    def __init__(self, rows=30, cols=30) -> None:
        """
        Initializes the MazeUI class with default or specified rows and columns, sets up the GUI components.

        Parameters:
            - rows (int): The number of rows in the maze (Defaults to 30).
            - cols (int): The number of columns in the maze (Defaults to 30).

        Attributes:
            - agent (Agent): An instance of the Agent class for solving the maze.
            - root (tk.Tk): The main window of the application.
            - rows (int): Number of rows in the maze.
            - cols (int): Number of columns in the maze.
            - canvas (tk.Canvas): Canvas widget for drawing the maze.
            - maze (Maze): An instance of the Maze class representing the maze.
            - initial_state (tuple): The starting point in the maze.
            - goal_state (tuple): The goal or end point in the maze.
            - generate_button (tk.Button): Button to generate a new maze.
            - solve_button (tk.Button): Button to solve the current maze.
            - algorithm (tk.StringVar): A tkinter variable holding the selected algorithm's name.
            - algorithm_menu (tk.OptionMenu): Dropdown menu for selecting the solving algorithm.
        """
        self.agent = None
        self.root = tk.Tk()
        self.root.title("Maze Solver")
        self.rows = rows
        self.cols = cols
        self.canvas = tk.Canvas(self.root, width=cols * 20, height=rows * 20, bg='white')
        self.canvas.pack()
        self.maze = Maze(rows, cols)
        self.initial_state = (1, 1)
        self.goal_state = (rows, cols)
        self.generate_button = tk.Button(self.root, text="Generate Maze", command=self.generate_and_draw_maze)
        self.generate_button.pack()
        self.solve_button = tk.Button(self.root, text="Solve Maze", command=self.solve_maze)
        self.solve_button.pack()
        self.algorithm = tk.StringVar(self.root)
        self.algorithm.set("DFS")  # default value
        self.algorithm_menu = tk.OptionMenu(self.root, self.algorithm, "DFS", "BFS", "A*")
        self.algorithm_menu.pack()

    def draw_maze(self):
        """
        Draws the maze on the canvas, including all walls and the initial and goal states.

        Returns:
            - None
        """
        self.canvas.delete("all")  # Clear the existing maze
        for x in range(1, self.maze.rows + 1):
            for y in range(1, self.maze.cols + 1):
                cell = (x, y)
                x1, y1 = (x - 1) * 20, (y - 1) * 20
                # Draw cell background
                self.canvas.create_rectangle(x1, y1, x1 + 20, y1 + 20, fill='white', outline="")
                # Draw walls
                if not self.maze.maze_map[cell]['R']:
                    self.canvas.create_line(x1 + 20, y1, x1 + 20, y1 + 20, fill='black', width=2)
                if not self.maze.maze_map[cell]['L']:
                    self.canvas.create_line(x1, y1, x1, y1 + 20, fill='black', width=2)
                if not self.maze.maze_map[cell]['U']:
                    self.canvas.create_line(x1, y1, x1 + 20, y1, fill='black', width=2)
                if not self.maze.maze_map[cell]['D']:
                    self.canvas.create_line(x1, y1 + 20, x1 + 20, y1 + 20, fill='black', width=2)
        # Drawing initial and goal states
        self.draw_state(self.initial_state, "green")
        self.draw_state(self.goal_state, "red")

    def draw_state(self, state, color):
        """
        Draws a single state (cell) in the maze with a specified color.

        Parameters:
            - state (tuple): The state (cell) to draw, represented as (row, column).
            - color (str): The color to use for the state (cell).

        Returns:
            - None
        """
        x, y = state
        x1, y1 = (x - 1) * 20, (y - 1) * 20
        self.canvas.create_rectangle(x1 + 2, y1 + 2, x1 + 18, y1 + 18, fill=color, outline="")

    def generate_and_draw_maze(self):
        """Generates a new maze and draws it on the canvas."""
        self.maze = Maze(self.rows, self.cols)
        self.maze.create_maze()
        self.draw_maze()

    def solve_maze(self):
        """Solves the maze using the selected algorithm and visualizes the solution path."""
        self.draw_maze()  # Clear any previous paths or highlights
        self.agent = Agent(self.maze)
        chosen_algorithm = self.algorithm.get()

        if chosen_algorithm == "DFS":
            solution_path = self.agent.dfs(self.initial_state, self.goal_state, self.update_gui_with_current_state)
        elif chosen_algorithm == "BFS":
            solution_path = self.agent.bfs(self.initial_state, self.goal_state, self.update_gui_with_current_state)
        elif chosen_algorithm == "A*":
            solution_path = self.agent.a_star(self.initial_state, self.goal_state, self.update_gui_with_current_state)

        self.redraw_final_path(solution_path)

    def update_gui_with_current_state(self, current_state):
        """
        Updates the GUI to reflect the current state during the solving process, with a delay for visualization.

        Parameters:
            - current_state (tuple): The current state (cell) being processed by the solving algorithm.
        """
        # Check if the current state is not the initial or goal state before coloring it blue
        if current_state != self.initial_state and current_state != self.goal_state:
            self.draw_state(current_state, "#0884cc")  # Light blue for the search process
        else:
            self.draw_state(current_state, "green")  # Keep initial and goal states green

        self.root.update()
        time.sleep(0.1)

    def redraw_final_path(self, solution_path):
        """
        Redraws the solution path on the maze after the maze has been solved.

        Parameters:
            - solution_path (list): The path from the initial to the goal state as a list of states (cells).
        """
        if solution_path is None:
            return

        for state in solution_path:
            self.draw_state(state, "red")
            self.root.update()
            time.sleep(0.05)

    def run(self):
        """Starts the tkinter main event loop to run the application."""
        self.root.mainloop()
