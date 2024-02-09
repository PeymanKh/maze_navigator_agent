# Maze Navigator Agent
***Solving Problems by Searching*** is a fundamental concept in the field of Artificial Intelligence that  involves finding a sequence of actions or steps that leads from an initial state to a goal state. This approach is widely used in various domains such as robotics, game playing, pathfinding, and automated planning. In this project, I developed a maze generator that creates a unique maze on each run, along with an agent that finds its way from the starting point to the target using both informed and uninformed search algorithms.


![Image of a person in the middle of a maze](https://github.com/PeymanKh/Maze-solver-Agent/assets/118134658/0b002b9d-99ea-462e-990e-399989c062b8)

## Table of Contents
- [1. Rational Agent](#agent)
- [2. Environment](#environment)
- [3. Search Problem](#search)
- [4. Search Algorithms](#algorithms)




<a name="agent"></a>
## 1. Rational Agent 
Different people approach AI with different goals in mind. Here the main question is do you want to model humans or try to achieve the optimal results? 
According to what we call the standard model, AI is concerned mainly with rational agent which takes the best possible action in a situation. A rational agent is any entity that can perceive its environment through sensors and acts upon that environment using actuators. The key characteristic of a rational agent is its ability to make decisions or choose actions that maximize its chances of achieving a certain goal or set of goals. Rationality, in this context, means that given a set of perceptions and a knowledge base, the agent will perform an action that is expected to bring about the best outcome according to a specific performance measure. This measure can vary depending on the agent's objectives, such as maximizing utility, minimizing cost, or achieving a particular state.
Rational agents can be simple or complex, ranging from automated thermostats to sophisticated robotic systems. They can operate in a variety of environments and are designed to optimize their performance based on the principles of rationality, which involve selecting the best available option considering the given information and any constraints.

<a name="environment"></a>
## 2. Environment
The entire universe could be considered as the environment, but practically speaking, it's only the part of the universe around the agent that can influence or be influenced by what the agent's actions. Environments can be physical, like a robot navigating a room, or virtual, like a software agent operating within a computer system. They can also vary in terms of their properties such as being predictable or unpredictable. The complexity of an agent's behavior and its decision-making process are often directly related to the complexity of its environment. Understanding the environment is crucial for designing an agent that can effectively achieve its goals within that context.


<a name="search"></a>
## 3. Search Problem
A search problem can be defined formally as follows:
1. State Space: A set of all possible states of the problem.
2. Initial State: The starting point of the problem, where the search begins.
3. Goal state(s): The state or states that represent a solution to the problem.
4. Actions: The actions available to the agent. Given a state "s", ACTIONS(s) returns a finite set of actions that can be executed in "s".
5. Transition Model: Describes what each action does. RESULT(s, a) returns the state that results from doing action "a" in state "s".
6. Search Algorithm: The method used to explore the state space. It systematically checks states, expanding them to discover new states until the goal is reached.


<a name="algorithms"></a>
## 3. Search Algorithms
A search algorithm takes a search problem as input and returns either a solution, or indication of failure. In this project, I utilized search tree over the state space graph. Each node in this tree represents a cell in the maze, and the connections between nodes (edges) represent the possible moves. The root of the tree represents the problem's initial state.

![(1, 1)](https://github.com/PeymanKh/Maze_Navigator_Agent/assets/118134658/98fbb387-0ca7-466d-96ca-6ff5ccabbf20)


