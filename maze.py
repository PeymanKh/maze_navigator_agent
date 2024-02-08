"""
This module implements a maze generator and solver using tkinter for visualization. The maze is generated using a
modified depth-first search algorithm. Each cell in the maze can have walls to its right, left, up, or down. The solver
aims to find a path from the start to the end of the maze using various algorithms though the agent module.
"""

import tkinter as tk  # For GUI creation.
import random  # For random selections, necessary in maze generation.


class Maze:
    """
        A class representing a maze with cells that can be navigated through by removing walls between them.

        Attributes:
            - rows (int): The number of rows in the maze.
            - cols (int): The number of columns in the maze.
            - maze_map (dict): A dictionary mapping cell coordinates to a dictionary of walls ('R', 'U', 'D', 'L') and
                              their statuses (True if removed).
            - states (list): A list to keep track of the cells visited during maze generation for backtracking.

        Methods:
            - create_maze(): Generates the maze by removing walls between cells using a depth-first search algorithm.
            - _continues_straight_path(cell1, cell2): Checks if moving from cell1 to cell2 continues a straight path.
            - _blocked_neighbours(cell): Finds all neighbouring cells of a given cell that have all walls intact.
            - _remove_wall_in_between(cell1, cell2): Removes the wall between two adjacent cells.
            - _draw_maze(): Creates a tkinter window and draws the maze.
            - valid_actions(cell): Returns a list of valid actions for a given cell.
            - result_of_action(cell, action): Returns the cell resulting from taking an action from a given cell.
            - heuristic(cell, goal): Calculates the Manhattan distance from a cell to the goal.
            - run(): Generates the maze and displays it using tkinter.
    """
    def __init__(self, rows=30, cols=30) -> None:
        """
            Initializes the Maze with a specified number of rows and columns.

            Args:
                - rows (int): The number of rows in the maze (default is 30).
                - cols (int): The number of columns in the maze (default is 30).
        """
        self.rows = rows
        self.cols = cols
        self.maze_map = {(x, y): {'R': False, 'U': False, 'D': False, 'L': False} for x in range(1, rows + 1)
                         for y in range(1, cols + 1)}
        self.states = []

    def create_maze(self) -> None:
        """
            Generates the maze layout by randomly removing walls between cells to create a path, using
            a depth-first search.
        """
        stack = [(1, 1)]   # Start with a stack containing the initial cell.

        # Loop until the stack is empty.
        while stack:
            cell = stack[-1]  # Get the current cell (top of the stack).
            if cell not in self.states:  # If the cell hasn't been visited,
                self.states.append(cell)  # mark it as visited.

            # Find all unvisited neighbours of the current cell.
            neighbors = self._blocked_neighbours(cell)

            if not neighbors:  # If there are no unvisited neighbours,
                stack.pop()  # backtrack by popping the stack.
                continue

            # Loop to choose a neighbour randomly and remove the wall between it and the current cell.
            while neighbors:
                next_cell = random.choice(neighbors)

                # Avoid straight paths for complexity.
                if not self._continues_straight_path(cell, next_cell):
                    self._remove_wall_in_between(cell, next_cell)  # Remove the wall between cells.
                    stack.append(next_cell)   # Add the new cell to the stack (moving forward).
                    break
                else:
                    neighbors.remove(next_cell)  # Remove the neighbour and try another.

            # If no valid neighbours were found, backtrack.
            if not neighbors:
                stack.pop()

    def _continues_straight_path(self, cell1, cell2) -> bool:
        """
            Determines if moving from cell1 to cell2 would continue a straight path from the last state.

            Args:
                - cell1 (tuple): The current cell coordinates.
                - cell2 (tuple): The next cell coordinates.

            Returns:
                - bool: True if moving to cell2 continues a straight path from the last cell, False otherwise.
        """

        # If no cells have been visited yet, can't continue a straight path.
        if not self.states:
            return False

        last_cell = self.states[-1]  # Get the last visited cell.

        # Calculate the direction moved to reach the current cell.
        direction = (cell1[0] - last_cell[0], cell1[1] - last_cell[1])

        # Calculate the direction to move to the next cell.
        next_direction = (cell2[0] - cell1[0], cell2[1] - cell1[1])

        # Return True if the direction to the next cell is the same as the last move (straight path).
        return direction == next_direction

    def _blocked_neighbours(self, cell) -> list:
        """
            Finds all neighbouring cells of the given cell that have all walls intact.

            Args:
                - cell (tuple): The cell coordinates.

            Returns:
                - list: A list of coordinates of all blocked neighbours.
        """
        directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}
        neighbors = []

        # Check each direction for valid, unvisited neighbours.
        for direction, (dx, dy) in directions.items():
            nx, ny = cell[0] + dx, cell[1] + dy  # Calculate neighbour coordinates.

            # If the neighbour is within bounds and all walls are intact,
            if 1 <= nx <= self.rows and 1 <= ny <= self.cols and not any(self.maze_map[(nx, ny)].values()):
                # add it to the list of neighbours.
                neighbors.append((nx, ny))

        # Return the list of valid, unvisited neighbours.
        return neighbors

    def _remove_wall_in_between(self, cell1, cell2):
        """
            Removes the wall between two adjacent cells.

            Args:
                - cell1 (tuple): The coordinates of the first cell.
                - cell2 (tuple): The coordinates of the second cell.
        """
        x1, y1 = cell1
        x2, y2 = cell2

        # Determine the orientation of the cells and remove the appropriate walls.
        if x1 == x2:
            if y1 < y2:
                self.maze_map[cell1]['D'] = True
                self.maze_map[cell2]['U'] = True
            else:
                self.maze_map[cell1]['U'] = True
                self.maze_map[cell2]['D'] = True
        elif y1 == y2:
            if x1 < x2:
                self.maze_map[cell1]['R'] = True
                self.maze_map[cell2]['L'] = True
            else:
                self.maze_map[cell1]['L'] = True
                self.maze_map[cell2]['R'] = True

    def _draw_maze(self):
        """
            Creates a tkinter window and draws the current maze layout.

            Returns:
                - tkinter.Tk: The tkinter root window for the maze.
        """
        root = tk.Tk()  # Create the main window.
        root.title("Maze-Solver")  # Set the window title.

        # Create a canvas for drawing the maze, with appropriate dimensions and background color.
        canvas = tk.Canvas(root, width=self.cols*20, height=self.rows*20, bg='white')

        # Add the canvas to the window.
        canvas.pack()

        # Loop through each cell in the maze and draw its walls.
        for x in range(1, self.rows+1):
            for y in range(1, self.cols+1):
                cell = (x, y)
                x1, y1 = (x - 1) * 20, (y - 1) * 20
                if not self.maze_map[cell]['R']:
                    canvas.create_line(x1 + 20, y1, x1 + 20, y1 + 20, fill='black')
                if not self.maze_map[cell]['L']:
                    canvas.create_line(x1, y1, x1, y1 + 20, fill='black')
                if not self.maze_map[cell]['U']:
                    canvas.create_line(x1, y1, x1 + 20, y1, fill='black')
                if not self.maze_map[cell]['D']:
                    canvas.create_line(x1, y1 + 20, x1 + 20, y1 + 20, fill='black')

        return root

    def valid_actions(self, cell) -> list:
        """
            Determines the valid actions that can be taken from a given cell, based on the walls
            that have been removed.

            Args:
                - cell (tuple): The coordinates of the cell.

            Returns:
                - list: A list of actions ['R', 'L', 'U', 'D'] that are valid to take from the given cell.
        """
        valid_actions = []

        # Loops through each wall in the current cell to check if it's removed (open).
        for action, is_open in self.maze_map[cell].items():

            # If the wall is removed, the direction is added as a valid action.
            if is_open:
                valid_actions.append(action)

        # Returns the list of valid actions from the current cell.
        return valid_actions

    @staticmethod
    def result_of_action(cell, action) -> tuple:
        """
            Determines the resulting cell from taking a specified action from a given cell.

            Args:
                - cell (tuple): The coordinates of the current cell.
                - action (str): The action to take ('R', 'L', 'U', 'D').

            Returns:
                - tuple: The coordinates of the cell resulting from the action.
        """
        # Defines the movement vector for each action.
        directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}

        # Gets the delta x and delta y for the action.
        dx, dy = directions[action]

        # Calculates and returns the new cell coordinates after the action.
        return cell[0] + dx, cell[1] + dy

    @staticmethod
    def heuristic(cell, goal) -> int:
        """
            Calculate the Manhattan distance from a given cell to the goal.
            This heuristic is appropriate for a grid where you can move in four directions.

            Args:
                - cell (tuple): The current cell coordinates.
                - goal (tuple): The goal cell coordinates.

            Returns:
                - int: The Manhattan distance from the current cell to the goal.
        """

        # The Manhattan distance is the sum of the absolute differences in the x and y coordinates.
        return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

    def run(self) -> None:
        """
        Generates the maze and displays it using tkinter. This is the main method to start
        the maze generation and visualization process.
        """
        self.create_maze()  # Calls the method to generate the maze.
        root = self._draw_maze()  # Draws the maze on a tkinter canvas and gets the root window.
        root.mainloop()  # Enters the tkinter main event loop to display the window and interact with the user.
