# CPSC-481-Project
To build a Connect Four game where a human plays against an AI opponent.

# Connect Four AI

## Team Members
* **Joshua Zamora:** Automated performance experiments, statistical analysis, and documentation[cite: 1].
* **Arturo Sanchez:** Minimax search, alpha-beta pruning, and heuristic evaluation function[cite: 1].
* **Filiberto Oceguera-Huizar:** Game rules, board representation, and graphical interface[cite: 1].
* **Timothy Huang:** Tactical board checks and move explanation features[cite: 1].

## Problem Statement
The goal of this project is to build a Connect Four game where a human plays against an AI opponent[cite: 1]. The project explores how game search algorithms choose moves and how search depth affects playing strength and decision time[cite: 1]. 

## Approach
* **Programming Language & Libraries:** Python, utilizing Tkinter for the graphical interface[cite: 1].
* **Algorithms:** Depth-limited minimax with alpha-beta pruning to evaluate possible moves and skip irrelevant branches[cite: 1].
* **Evaluation Function:** A heuristic function scores board positions at the depth limit based on potential lines of four, opponent threats, and center column control[cite: 1]. Explicit scores are assigned for terminal wins, losses, and draws[cite: 1].
* **Datasets:** No external training datasets are used; the AI relies entirely on search algorithms and the manually designed evaluation function[cite: 1].

## Description of the Software
The software is a desktop application consisting of several interconnected components[cite: 1]:
* **Front-End / GUI:** Lets the user select a difficulty level, choose who moves first, restart the game, and displays the current turn and game results (win/draw)[cite: 1].
* **AI Engine:** Processes the current board state using minimax and alpha-beta pruning to determine the optimal next move based on the selected difficulty (search depth)[cite: 1].
* **Explanation Module ("Why this move?"):** Uses tactical board checks to identify and display simple tactical reasons for a move, such as completing four in a row or blocking an opponent's win[cite: 1]. 

## Layout of the Code
* `main.py`: Entry point that initializes the Tkinter graphical interface and routes user inputs to the game logic.
* `game_logic.py`: Manages the 6x7 board state, validates legal moves, and checks for terminal game states (wins/draws).
* `ai_agent.py`: Contains the depth-limited minimax algorithm, alpha-beta pruning logic, and the heuristic scoring function.
* `explanations.py`: Handles the board checks to generate the "Why this move?" tactical insights[cite: 2].
* `performance_tests.py`: Scripts to automate gameplay between the AI and a random opponent to gather performance data[cite: 2].

## Evaluation Metrics
Performance is quantified through automated testing[cite: 1, 2]:
* **Win/Loss/Draw Rates:** The AI plays at least 100 games per difficulty level against a random legal-move opponent, with starting positions split evenly[cite: 1].
* **Efficiency:** Plain minimax and alpha-beta pruning are compared on identical test positions at the same depth[cite: 1]. Metrics recorded include decision time and the number of positions examined (excluding animation time)[cite: 1].
* **Tactical Accuracy:** Specific tests check for immediate wins, required blocks, and full columns[cite: 1].

## Conclusion and Future Work
*(To be populated at the end of Week 8 after final bugs are fixed and testing is complete[cite: 1]. Summarize main lessons learned and ideas for improvement[cite: 2].)*

## References
*(To be populated. Will list any course materials, tutorials, or papers used to study the algorithms[cite: 1, 2].)*

---

## Source Code Submission Instructions

### System Requirements
* **OS:** Windows, macOS, or Linux[cite: 2].
* **Language:** Python 3.x[cite: 2].
* **Libraries:** `tkinter` (included in standard Python library)[cite: 1, 2]. 

### Installation Instructions
1. Download and extract the project `.zip` file, or clone the repository[cite: 2].
2. Open a terminal or command prompt and navigate to the root folder of the project[cite: 2].
3. Ensure Python 3.x is installed on your system by running:
   ```bash
   python --version
