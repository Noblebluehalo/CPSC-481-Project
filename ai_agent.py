import math
import copy
import random

PLAYER_PIECE = 1
AI_PIECE = 2
EMPTY = 0

def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE if piece == AI_PIECE else AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score

def score_position(game, piece):
    score = 0
    board = game.board
    
    # Center column preference
    center_array = [board[r][game.columns//2] for r in range(game.rows)]
    center_count = center_array.count(piece)
    score += center_count * 3

    # Horizontal
    for r in range(game.rows):
        row_array = board[r]
        for c in range(game.columns-3):
            window = row_array[c:c+4]
            score += evaluate_window(window, piece)

    # Vertical
    for c in range(game.columns):
        col_array = [board[r][c] for r in range(game.rows)]
        for r in range(game.rows-3):
            window = col_array[r:r+4]
            score += evaluate_window(window, piece)

    # Positive Diagonal (NEW)
    for r in range(game.rows-3):
        for c in range(game.columns-3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Negative Diagonal (NEW)
    for r in range(game.rows-3):
        for c in range(game.columns-3):
            window = [board[r+3-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score

def plain_minimax(game, depth, maximizingPlayer):
    """Plain Minimax without pruning for performance comparison."""
    valid_locations = game.get_valid_locations()
    is_terminal = game.is_terminal_node()
    nodes_examined = 1 
    
    if depth == 0 or is_terminal:
        if is_terminal:
            if game.check_win(AI_PIECE):
                return (None, 100000000000000, nodes_examined)
            elif game.check_win(PLAYER_PIECE):
                return (None, -10000000000000, nodes_examined)
            else:
                return (None, 0, nodes_examined)
        else:
            return (None, score_position(game, AI_PIECE), nodes_examined)
            
    if maximizingPlayer:
        value = -math.inf
        best_col = random.choice(valid_locations) if valid_locations else None
        for col in valid_locations:
            b_copy = copy.deepcopy(game)
            b_copy.drop_piece(col, AI_PIECE)
            new_score = plain_minimax(b_copy, depth-1, False)
            nodes_examined += new_score[2]
            if new_score[1] > value:
                value = new_score[1]
                best_col = col
        return best_col, value, nodes_examined
    else:
        value = math.inf
        best_col = random.choice(valid_locations) if valid_locations else None
        for col in valid_locations:
            b_copy = copy.deepcopy(game)
            b_copy.drop_piece(col, PLAYER_PIECE)
            new_score = plain_minimax(b_copy, depth-1, True)
            nodes_examined += new_score[2]
            if new_score[1] < value:
                value = new_score[1]
                best_col = col
        return best_col, value, nodes_examined

def minimax(game, depth, alpha, beta, maximizingPlayer):
    """Minimax with Alpha-Beta Pruning."""
    valid_locations = game.get_valid_locations()
    is_terminal = game.is_terminal_node()
    nodes_examined = 1 
    
    if depth == 0 or is_terminal:
        if is_terminal:
            if game.check_win(AI_PIECE):
                return (None, 100000000000000, nodes_examined)
            elif game.check_win(PLAYER_PIECE):
                return (None, -10000000000000, nodes_examined)
            else:
                return (None, 0, nodes_examined)
        else:
            return (None, score_position(game, AI_PIECE), nodes_examined)
            
    if maximizingPlayer:
        value = -math.inf
        best_col = random.choice(valid_locations) if valid_locations else None
        for col in valid_locations:
            b_copy = copy.deepcopy(game)
            b_copy.drop_piece(col, AI_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, False)
            nodes_examined += new_score[2]
            if new_score[1] > value:
                value = new_score[1]
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value, nodes_examined
    else:
        value = math.inf
        best_col = random.choice(valid_locations) if valid_locations else None
        for col in valid_locations:
            b_copy = copy.deepcopy(game)
            b_copy.drop_piece(col, PLAYER_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, True)
            nodes_examined += new_score[2]
            if new_score[1] < value:
                value = new_score[1]
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value, nodes_examined