# CPSC-481-Project
To build a Connect Four game where a human plays against an AI opponent.

# Connect Four AI

## Team Members
* **Joshua Zamora:** Automated performance experiments, statistical analysis, and documentation.
* **Arturo Sanchez:** Minimax search, alpha-beta pruning, and heuristic evaluation function.
* **Filiberto Oceguera-Huizar:** Game rules, board representation, and graphical interface.
* **Timothy Huang:** Tactical board checks and move explanation features.

## Problem Statement
The goal of this project is to build a Connect Four game where a human plays against an AI opponent. The project explores how game search algorithms choose moves and how search depth affects playing strength and decision time.

## Approach
* **Programming Language & Libraries:** Python, utilizing Tkinter for the graphical interface.
* **Algorithms:** Depth-limited minimax with alpha-beta pruning to evaluate possible moves and skip irrelevant branches.
* **Evaluation Function:** A heuristic function scores board positions at the depth limit based on potential lines of four, opponent threats, and center column control. Explicit scores are assigned for terminal wins, losses, and draws.
* **Datasets:** No external training datasets are used; the AI relies entirely on search algorithms and the manually designed evaluation function.

## Description of the Software
The software is a desktop application consisting of several interconnected components:
* **Front-End / GUI:** Lets the user select a difficulty level, choose who moves first, restart the game, and displays the current turn and game results (win/draw).
* **AI Engine:** Processes the current board state using minimax and alpha-beta pruning to determine the optimal next move based on the selected difficulty (search depth).
* **Explanation Module ("Why this move?"):** Uses tactical board checks to identify and display simple tactical reasons for a move, such as completing four in a row or blocking an opponent's win.

## Layout of the Code
* `main.py`: Entry point that initializes the Tkinter graphical interface and routes user inputs to the game logic.
* `game_logic.py`: Manages the 6x7 board state, validates legal moves, and checks for terminal game states (wins/draws).
* `ai_agent.py`: Contains the depth-limited minimax algorithm, alpha-beta pruning logic, and the heuristic scoring function.
* `explanations.py`: Handles the board checks to generate the "Why this move?" tactical insights.
* `performance_tests.py`: Scripts to automate gameplay between the AI and a random opponent to gather performance data.

## Evaluation Metrics
Performance is quantified through automated testing:
* **Win/Loss/Draw Rates:** The AI plays at least 100 games per difficulty level against a random legal-move opponent, with starting positions split evenly.
* **Efficiency:** Plain minimax and alpha-beta pruning are compared on identical test positions at the same depth. Metrics recorded include decision time and the number of positions examined (excluding animation time).
* **Tactical Accuracy:** Specific tests check for immediate wins, required blocks, and full columns.

## Conclusion and Future Work
*(To be populated at the end of Week 8 after final bugs are fixed and testing is complete. Summarize main lessons learned and ideas for improvement.)*

## References
*(To be populated. Will list any course materials, tutorials, or papers used to study the algorithms.)*

---

## Source Code Submission Instructions

### System Requirements
* **OS:** Windows, macOS, or Linux.
* **Language:** Python 3.x.
* **Libraries:** `tkinter` (included in standard Python library).

### Installation Instructions
1. Download and extract the project `.zip` file, or clone the repository.
2. Open a terminal or command prompt and navigate to the root folder of the project.
3. Ensure Python 3.x is installed on your system by running:

```bash
python --version
```
