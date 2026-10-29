import math 
import copy

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

def score_postion(game, piece):
    score = 0
    board = game.board
    #center column preference
    center_array = [board[r][game.columns//2] for r in range(game.rows)]
    center_count = center_array.count(piece)
    score += center_count * 3

    #Horizontal
    for r in range(game.rows):
        row_array = board[r]
        for c in range(game.columns-3):
            window = row_array[c:c+4]
            score += evaluate_window(window, piece)

