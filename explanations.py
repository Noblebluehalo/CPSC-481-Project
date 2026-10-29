import copy
from ai_agent import AI_PIECE, PLAYER_PIECE

def explain_move(game, col):
    """
    Evaluates the chosen column to explain simple tactical reasons.
    Returns a string explanation.
    """
    #Check immediate win
    temp_game = copy.deepcopy(game)
    temp_game.drop_piece(col, AI_PIECE)
    if temp_game.check_win(AI_PIECE):
        return "This move complete four in a row for an immediate win."

    #Check immediate block
    temp_game_block = copy.deepcopy(game)
    temp_game_block.drop_piece(col, PLAYER_PIECE)
    if temp_game_block.check_win(PLAYER_PIECE):
        return "This move blocks the opponent's immediate winning threat."

    #genral strategic explanation
    return "This move maximizes potential future alignments or controls the center of the board."