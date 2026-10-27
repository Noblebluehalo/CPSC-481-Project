class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = [['0 ' for _ in range(self.columns)] for _ in range(self.rows)]
        self.current_turn = 1 


        def drop_piece(self, col, piece):
            for r in range(self.rows - 1, -1, -1):
                if self.board[r][col] == '0 ':
                    self.board[r][col] = piece
                    return r 
                return -1  # Column is full
