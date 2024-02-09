# Maze Navigator Agent
***Solving Problems by Searching*** is a fundamental concept in the field of Artificial Intelligence that  involves finding a sequence of actions or steps that leads from an initial state to a goal state. This approach is widely used in various domains such as robotics, game playing, pathfinding, and automated planning. In this project, I developed a maze generator that creates a unique maze on each run, along with an agent that finds its way from the starting point to the target using both informed and uninformed search algorithms.

![Image of a person in the middle of a maze](https://github.com/PeymanKh/Maze-solver-Agent/assets/118134658/0b002b9d-99ea-462e-990e-399989c062b8)

## Table of Contents
- [1. Rational Agent](#agent)
- [2. Environment](#environment)
- [3. Search Problem](#search)
- [4. Search Algorithms](#algorithms)
- [5. Modules Overview](#algorithms)
- [6. How to Run The App](#app)
- [7. Reference](#credits)




<a name="agent"></a>
## 1. Rational Agent 
Different people approach AI with different goals in mind. Here, the main question is: do you want to model humans or try to achieve optimal results? According to what we call the standard model, AI is concerned mainly with rational agents, which take the best possible action in a given situation. A rational agent is any entity that can perceive its environment through sensors and act upon that environment using actuators. The key characteristic of a rational agent is its ability to make decisions or choose actions that maximize its chances of achieving a certain goal or set of goals. Rationality, in this context, means that given a set of perceptions and a knowledge base, the agent will perform an action that is expected to bring about the best outcome according to a specific performance measure. This measure can vary depending on the agent's objectives, such as maximizing utility, minimizing cost, or achieving a particular state. Rational agents can be simple or complex, ranging from automated thermostats to sophisticated robotic systems.

<a name="environment"></a>
## 2. Environment
The entire universe could be considered as the environment, but practically speaking, it's only the part of the universe around the agent that can influence or be influenced by the agent's actions. Environments can be physical, like a robot navigating a room, or virtual, like a software agent operating within a computer system. They can also vary in terms of their properties, such as being predictable or unpredictable. The complexity of an agent's behavior and its decision-making process are often directly related to the complexity of its environment. Understanding the environment is crucial for designing an agent that can effectively achieve its goals within that context.

<a name="search"></a>
## 3. Search Problem
A search problem can be defined formally as follows:

1. State Space: A set of all possible states of the problem.
2. Initial State: The starting point of the problem, where the search begins.
3. Goal State(s): The state or states that represent a solution to the problem.
4. Actions: The actions available to the agent. Given a state "s", ACTIONS(s) returns a finite set of actions that can be executed in "s".
5. Transition Model: Describes what each action does. RESULT(s, a) returns the state that results from performing action "a" in state "s".
6. Search Algorithm: The method used to explore the state space. It systematically checks states, expanding them to discover new states until the goal is reached.


<a name="algorithms"></a>
## 4. Search Algorithms

A search algorithm takes a search problem as input and returns either a solution or an indication of failure. In this project, I utilized a search tree over the state space graph. Each node in this tree represents a cell in the maze, and the connections between nodes (edges) represent the possible moves. The root of the tree represents the problem's initial state.

![(1, 1)](https://github.com/PeymanKh/Maze_Navigator_Agent/assets/118134658/98fbb387-0ca7-466d-96ca-6ff5ccabbf20)


Throughout the project's development, two distinct search strategies were applied to systematically expand from the current state towards discovering new states until the goal was achieved. The first strategy, Uninformed Search (also known as blind search), relies on the absence of additional information about the state space beyond the current state. This strategy encompasses two primary algorithms:


1. Breadth-First Search (BFS): BFS operates by exploring the state space horizontally, processing all states at a certain depth before proceeding to states at the next level of depth. This methodical approach ensures that the shortest path, in terms of the number of steps taken, is identified. This characteristic of BFS makes it particularly useful in scenarios where the path length to the goal is of primary concern, as it guarantees the discovery of the shortest path if one exists.

2. Depth-First Search (DFS): In contrast, DFS delves deep into the state space, prioritizing the exploration of as far along each branch as possible before resorting to backtracking. This approach is known for its memory efficiency, as it does not require storing all expanded nodes at a given depth, unlike BFS. However, the trade-off is that DFS does not inherently guarantee finding the shortest path to the goal. Its tendency to explore deep into the state space without regard for proximity to the goal can lead to finding a solution that, while valid, may not be optimal in terms of path length.


> DFS is favored for its lower memory usage, as it does not require storing all sibling nodes at each level to navigate a path, making it ideal for problems with deep solution paths or vast state spaces. In contrast, BFS excels in situations where finding the shortest path is paramount due to its systematic level-by-level exploration, albeit at a higher memory cost. The selection between DFS and BFS hinges on the application's specific needs: BFS is the go-to for scenarios where the shortest path is essential, while DFS is better suited for cases with unknown solution depths or extensive search spaces.


![DFS & BFS](https://github.com/PeymanKh/Maze_Navigator_Agent/assets/118134658/3dee7b5e-9ade-49e7-8643-e24a9a7a480a)

The second strategy is Informed Search, also known as heuristic search. Within this approach, the agent utilizes additional knowledge about the state space to efficiently find the solution. Unlike uninformed search strategies that explore the search space without any direction, informed strategies use heuristics to guide the search process towards the goal more quickly. The A* (A_star) algorithm represents a significant advancement in informed search strategies by leveraging heuristic functions to efficiently navigate towards the goal state. Unlike uninformed search methods that indiscriminately explore the search space, A* incorporates additional information through two key cost functions:

- g(n):  This function calculates the cost of the path from the start node to the current node n. It ensures that the path taken to reach n is accounted for in the decision-making process, providing a basis for understanding the accrued cost of the journey thus far.
- h(n): The heuristic function estimates the cost from node n to the closest goal node. It's here that A* differentiates itself by integrating domain-specific knowledge to make educated guesses about the remaining path cost. This heuristic is crucial for guiding the search more directly towards the goal, significantly improving search efficiency by avoiding less promising paths.
- f(n) = g(n) + h(n): f(n) represents the total estimated cost of the cheapest solution passing through node n. A* uses this function to prioritize which nodes to explore next, favoring those with the lowest f(n) values. This prioritization ensures that A* systematically focuses on paths that are more likely to lead to the goal efficiently,


My heuristic in this project is the Manhattan distance for calculating the distance between two points \((x_1, y_1)\) and \((x_2, y_2)\)in a grid-based path, which is calculated as:

**$$
d = |x_2 - x_1| + |y_2 - y_1|
$$**

where:

- \(d\) is the Manhattan distance,
- \((x_1, y_1)\) are the coordinates of the first point,
- \((x_2, y_2)\) are the coordinates of the second point.

This formula computes the sum of the absolute differences of their Cartesian coordinates. It's an effective heuristic for grid-based mazes where movement is restricted to orthogonal directions (right, left, up, and down) because it accurately reflects the minimum number of steps required to move from one point to another without considering any potential obstacles that might be present.

> The effectiveness of A* depend on the heuristic function h(n). an accurate h(n) can dramatically reduce the search space, allowing A* to find the optimal path more quickly than uninformed search algorithms. However, the choice of h(n) s crucial; an overly optimistic heuristic can lead to inefficient searches, while a pessimistic one may not provide sufficient guidance to improve upon uninformed strategies. The beauty of A* lies in its flexibility and the balance it strikes between exploring unvisited nodes and extending paths from known nodes, making it highly effective for a wide range of problems where the goal is to find the most cost-effective path.

<a name="module"></a>
## 5. Modules Overview
###  5.1. maze module
The core functionality of this module lies in its ability to generate random mazes by leveraging a modified depth-first search (DFS) algorithm, popular for its simplicity and capacity to craft complex mazes. It can also solve mazes using a variety of algorithms that are integrated from the agent module. The Maze class encapsulates the logic for maze generation, including methods for creating the maze, identifying valid actions within it, and drawing the maze using tkinter for visualization. Additionally, it employs heuristic functions to facilitate the solving process.
###  5.2. agent module
The Agent module introduces the Agent class, specifically engineered to navigate through mazes. It stands out by utilizing a variety of search algorithms, including Depth-First Search (DFS), Breadth-First Search (BFS), and A* Search, each designed to find a path from an initial state to a goal state within the maze. The Agent class is intricately linked with the Maze instance, which provides the layout of the maze and the mechanics for movement, such as identifying valid actions and determining the outcomes of those actions. Importantly, this module utilizes callback functions within its search algorithms for real-time updates to the GUI, enhancing the user interface experience. Through the integration of essential data structures like Queue and MinHeap, the Agent class efficiently executes search algorithms, making it a cornerstone for interactive maze navigation and solution visualization.
###  5.3. dataStructure module
The Data Structure module is fundamental to supporting algorithmic operations. The Queue class adheres to the First In, First Out (FIFO) principle, facilitating operations like enqueueing to add elements to the queue's end and dequeueing to remove elements from the front, essential for breadth-first search processes. On the other hand, the MinHeap class implements a min-heap structure, optimizing priority queue operations with efficient minimum value retrieval. This is crucial for algorithms like A* search, where priority is given to paths with lower costs. Through these implementations, the module ensures that search algorithms can be executed efficiently, with quick access to and manipulation of data as required by the algorithms' logic.
###  5.4. ui module
The UI module harnesses the tkinter library to offer a graphical user interface that allows users to engage directly with the maze-solving process. It empowers users to generate mazes, select a solving algorithm from options like Depth-First Search (DFS), Breadth-First Search (BFS), and A* Search, and visually track the algorithm's progress in real-time as it works to find a solution. The MazeUI class, central to this module, sets up the main application window, incorporates a canvas for maze drawing, and integrates buttons for maze generation and solving.
### 5.5. main module
This module is where everything begins for the maze solver application. It introduces a class called MainApp that gets everything ready for users to interact with the maze. When MainApp starts, it sets up a visual interface for the maze, where users can create mazes, pick how they want to solve them, and see the solution unfold step by step.


<a name="app"></a>
## 6. How to Run The App
Ensure you have Python 3 installed on your computer. You should download five modules and save them in a single folder. Any integrated development environment (IDE) can be used to run the codes, and you can view the application by executing the main.py code.


<a name="credits"></a>
## 7. Reference
Russell, S., & Norvig, P. (1995). ***Artificial Intelligence: A Modern Approach***.
