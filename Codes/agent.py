"""
This module defines the Agent class responsible for navigating through mazes.

The Agent class utilizes different search algorithms to find a path from a given initial state to a goal state within
the maze. It supports Depth-First Search (DFS), Breadth-First Search (BFS), and A* Search algorithms. Each method is
designed to interact with a Maze instance, which provides the maze's layout and the mechanics for moving within it,
such as identifying valid actions and the result of those actions.
Callback functions are used within search algorithms for real-time GUI updates, which can be useful for UI.
"""

from dataStructure import Queue, MinHeap  # Import necessary data structures for the search algorithms.


class Agent:
    """
        Represents an agent navigating through a maze.

        Attributes:
            - maze (Maze): An instance of a Maze class that this agent will navigate.
    """
    def __init__(self, maze) -> None:
        """
            - Initializes the Agent with a maze to solve.

            - Args:
                - maze (Maze): The maze instance that the agent will navigate.
        """
        self.maze = maze

    def dfs(self, current_state, goal_state, callback, visited=None) -> list or None:
        """
            Performs Depth-First Search (DFS) from the current state to the goal state.

            Args:
                - current_state (tuple): The current state of the agent in the maze.
                - goal_state (tuple): The goal state that the agent aims to reach.
                - callback (function): A function to call for updating the GUI.
                - visited (set, optional): A set of already visited states. Defaults to None.

            Returns:
                - list: The path from the current state to the goal state as a list of states,
                or None if no path is found.
        """

        # Initialize visited set in the first call.
        if visited is None:
            visited = set()

        # Return path if goal state is reached.
        if current_state == goal_state:
            return [current_state]

        visited.add(current_state)  # Add current state to the visited.
        callback(current_state)  # Update GUI

        # Iterate through valid actions of the current state.
        for action in self.maze.valid_actions(current_state):
            next_state = self.maze.result_of_action(current_state, action)

            # Continue search from next state if not visited.
            if next_state not in visited:
                path = self.dfs(next_state, goal_state, callback, visited)

                # Return path including current state if path is found.
                if path:
                    return [current_state] + path

        return None  # Return None if no path is found.

    def bfs(self, initial_state, goal_state, callback) -> list or None:
        """
            Performs Breadth-First Search (BFS) from the initial state to the goal state.

            Args:
                - initial_state (tuple): The initial state of the agent in the maze.
                - goal_state (tuple): The goal state that the agent aims to reach.
                - callback (function): A function to call for updating the GUI.

            Returns:
                - list: The path from the initial state to the goal state as a list of states,
                or None if no path is found.
        """
        visited = set()
        queue = Queue()

        # Enqueue the initial state with an empty path.
        queue.enqueue((initial_state, []))

        while not queue.is_empty():
            current_state, path = queue.dequeue()  # Dequeue the next state to visit.
            if current_state in visited:
                continue  # Skip if state has already been visited.

            visited.add(current_state)  # Add current state to the visited.
            callback(current_state)  # Update GUI

            # Return path if goal state is reached.
            if current_state == goal_state:
                return path + [current_state]

            # Explore all valid actions from the current state and enqueue new states to visit.
            for action in self.maze.valid_actions(current_state):
                next_state = self.maze.result_of_action(current_state, action)
                if next_state not in visited:
                    queue.enqueue((next_state, path + [current_state]))

        return None  # Return None if no path is found.

    def a_star(self, initial_state, goal_state, callback) -> list or None:
        """
            Performs A* Search from the initial state to the goal state.

            Args:
                - initial_state (tuple): The initial state of the agent in the maze.
                - goal_state (tuple): The goal state that the agent aims to reach.
                - callback (function): A function to call for updating the GUI.

        Returns:
            list: The path from the initial state to the goal state as a list of states,
            or None if no path is found.
        """

        # Use a MinHeap for efficient retrieval of the lowest cost state.
        priority_queue = MinHeap()
        visited = set()

        # Initialize with the initial state. The heap stores tuples of (f-score, g-score, state, path).
        priority_queue.push((0 + self.maze.heuristic(initial_state, goal_state), 0, initial_state, [initial_state]))

        # Distance from start to the current node.
        g_score = {initial_state: 0}

        # Continue until there are no more states to explore.
        while not priority_queue.is_empty():
            f_score, g_score_current, current, path = priority_queue.pop()  # Pop state with the lowest f-score.

            # Skip if state has already been visited.
            if current in visited:
                continue

            visited.add(current)  # Add current state to the visited.
            callback(current)  # Update GUI

            # Return path if goal state is reached.
            if current == goal_state:
                return path

            for action in self.maze.valid_actions(current):
                next_cell = self.maze.result_of_action(current, action)
                tentative_g_score = g_score_current + 1

                if next_cell not in g_score or tentative_g_score < g_score[next_cell]:
                    # Update g_score for next_cell if it's a better path.
                    g_score[next_cell] = tentative_g_score

                    # Calculate f_score.
                    f_score_next = tentative_g_score + self.maze.heuristic(next_cell, goal_state)

                    # Append next_cell to the current path.
                    new_path = path + [next_cell]

                    # Add to the priority queue.
                    priority_queue.push((f_score_next, tentative_g_score, next_cell, new_path))

        return None  # Return None if no path to the goal state is found.
