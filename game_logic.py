class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.current_turn = 1 # 1 for Player, 2 for AI

    def drop_piece(self, col, piece):
        for r in range(self.rows-1, -1, -1):
            if self.board[r][col] == 0:
                self.board[r][col] = piece
                return r
        return -1

    def is_valid_location(self, col):
        return self.board[0][col] == 0

    def get_valid_locations(self):
        return [col for col in range(self.columns) if self.is_valid_location(col)]

    def check_win(self, piece):
        # Horizontal
        for c in range(self.columns-3):
            for r in range(self.rows):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    return True
        # Vertical
        for c in range(self.columns):
            for r in range(self.rows-3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    return True
        # Positive Diagonal
        for c in range(self.columns-3):
            for r in range(self.rows-3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    return True
        # Negative Diagonal
        for c in range(self.columns-3):
            for r in range(3, self.rows):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True
        return False

    def is_terminal_node(self):
        return self.check_win(1) or self.check_win(2) or len(self.get_valid_locations()) == 0