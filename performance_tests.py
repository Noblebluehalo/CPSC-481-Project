import time
import random
import math
import copy
from game_logic import ConnectFour
from ai_agent import minimax, plain_minimax, AI_PIECE, PLAYER_PIECE

def test_pruning_efficiency(depth=4):
    """Compares Plain Minimax and Alpha-Beta Pruning on identical test positions."""
    print(f"\n--- Pruning Comparison (Depth {depth}) ---")
    game = ConnectFour()
    
    # Populate a random mid-game board to give algorithms something to evaluate
    for _ in range(8):
        valid = game.get_valid_locations()
        game.drop_piece(random.choice(valid), random.choice([PLAYER_PIECE, AI_PIECE]))

    # Test Plain Minimax
    game_copy_1 = copy.deepcopy(game)
    start_time_plain = time.time()
    col_plain, score_plain, nodes_plain = plain_minimax(game_copy_1, depth, True)
    time_plain = time.time() - start_time_plain

    # Test Alpha-Beta
    game_copy_2 = copy.deepcopy(game)
    start_time_ab = time.time()
    col_ab, score_ab, nodes_ab = minimax(game_copy_2, depth, -math.inf, math.inf, True)
    time_ab = time.time() - start_time_ab

    print(f"Plain Minimax: Score = {score_plain}, Nodes = {nodes_plain}, Time = {time_plain:.4f}s")
    print(f"Alpha-Beta:    Score = {score_ab}, Nodes = {nodes_ab}, Time = {time_ab:.4f}s")
    
    if score_plain == score_ab:
        print("Success: Both algorithms returned the same minimax score.")
    else:
        print("Error: Algorithms returned different scores!")

def run_performance_metrics(games=100, depth=3):
    """Runs automated games splitting starting positions evenly."""
    print(f"\n--- 100 Game Simulation (Depth {depth}) ---")
    wins, losses, draws = 0, 0, 0
    total_ai_time = 0
    total_nodes = 0
    moves_made = 0

    for i in range(games):
        game = ConnectFour()
        # Evenly split starting positions
        turn = AI_PIECE if i % 2 == 0 else PLAYER_PIECE 
        
        while not game.is_terminal_node():
            if turn == PLAYER_PIECE:
                valid = game.get_valid_locations()
                if valid:
                    game.drop_piece(random.choice(valid), PLAYER_PIECE)
                turn = AI_PIECE
            else:
                start_time = time.time()
                col, _, nodes = minimax(game, depth, -math.inf, math.inf, True)
                total_ai_time += (time.time() - start_time)
                total_nodes += nodes
                moves_made += 1
                if col is not None:
                    game.drop_piece(col, AI_PIECE)
                turn = PLAYER_PIECE

        if game.check_win(AI_PIECE):
            wins += 1
        elif game.check_win(PLAYER_PIECE):
            losses += 1
        else:
            draws += 1
            
        if (i+1) % 25 == 0:
            print(f"Completed {i+1}/{games} games...")

    print("\nFinal Results:")
    print(f"AI Wins: {wins} | Losses: {losses} | Draws: {draws}")
    print(f"Avg AI Decision Time: {total_ai_time / max(1, moves_made):.4f} seconds per move")
    print(f"Avg Nodes Expanded: {total_nodes / max(1, moves_made):.1f} per move")

if __name__ == "__main__":
    test_pruning_efficiency(depth=4)
    run_performance_metrics(games=100, depth=3)