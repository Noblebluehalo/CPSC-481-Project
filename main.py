import tkinter as tk
import math
from game_logic import ConnectFour
from ai_agent import minimax, AI_PIECE, PLAYER_PIECE
from explanations import explain_move

SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)
BLUE = "#0000FF"
BLACK = "#000000"
RED = "#FF0000"
YELLOW = "#FFFF00"

class ConnectFourGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four AI")
        self.game = ConnectFour()
        
        self.difficulty = tk.IntVar(value=3)
        self.starting_player = tk.IntVar(value=PLAYER_PIECE) 
        
        self.setup_ui()
        self.restart()

    def setup_ui(self):
        controls = tk.Frame(self.root)
        controls.pack(pady=5)
        
        tk.Label(controls, text="Difficulty (Depth):").pack(side=tk.LEFT)
        tk.Scale(controls, from_=1, to=6, variable=self.difficulty, orient=tk.HORIZONTAL).pack(side=tk.LEFT, padx=10)
        
        # NEW: Toggle for Who Moves First
        tk.Label(controls, text="Starts:").pack(side=tk.LEFT)
        tk.Radiobutton(controls, text="Human", variable=self.starting_player, value=PLAYER_PIECE).pack(side=tk.LEFT)
        tk.Radiobutton(controls, text="AI", variable=self.starting_player, value=AI_PIECE).pack(side=tk.LEFT)
        
        tk.Button(controls, text="Restart", command=self.restart).pack(side=tk.LEFT, padx=10)
        
        self.info_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.info_label.pack(pady=5)

        self.canvas = tk.Canvas(self.root, width=self.game.columns*SQUARESIZE, height=(self.game.rows+1)*SQUARESIZE)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.handle_click)

    def draw_board(self):
        self.canvas.delete("all")
        for c in range(self.game.columns):
            for r in range(self.game.rows):
                x0 = c * SQUARESIZE
                y0 = (r + 1) * SQUARESIZE
                x1 = x0 + SQUARESIZE
                y1 = y0 + SQUARESIZE
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=BLUE)
                
                piece = self.game.board[r][c]
                color = BLACK
                if piece == PLAYER_PIECE:
                    color = RED
                elif piece == AI_PIECE:
                    color = YELLOW
                    
                cx = x0 + SQUARESIZE/2
                cy = y0 + SQUARESIZE/2
                self.canvas.create_oval(cx-RADIUS, cy-RADIUS, cx+RADIUS, cy+RADIUS, fill=color)

    def handle_click(self, event):
        if self.game.is_terminal_node() or self.game.current_turn != PLAYER_PIECE:
            return

        col = int(math.floor(event.x / SQUARESIZE))
        
        if self.game.is_valid_location(col):
            self.game.drop_piece(col, PLAYER_PIECE)
            self.draw_board()
            
            if self.game.check_win(PLAYER_PIECE):
                self.info_label.config(text="Player Wins!")
                return
                
            self.game.current_turn = AI_PIECE
            self.info_label.config(text="AI is thinking...")
            self.root.update()
            self.ai_move()

    def ai_move(self):
        # NEW: Unpacks nodes_examined
        col, _, nodes = minimax(self.game, self.difficulty.get(), -math.inf, math.inf, True)
        if col is not None:
            explanation = explain_move(self.game, col)
            self.game.drop_piece(col, AI_PIECE)
            self.draw_board()
            
            if self.game.check_win(AI_PIECE):
                self.info_label.config(text=f"AI Wins! {explanation} (Nodes checked: {nodes})")
            else:
                self.game.current_turn = PLAYER_PIECE
                self.info_label.config(text=f"Your Turn. AI says: {explanation} (Nodes checked: {nodes})")

    def restart(self):
        self.game = ConnectFour()
        self.game.current_turn = self.starting_player.get()
        self.draw_board()
        
        if self.game.current_turn == AI_PIECE:
            self.info_label.config(text="AI is thinking...")
            self.root.update()
            self.ai_move()
        else:
            self.info_label.config(text="Your Turn (Red)")

if __name__ == "__main__":
    root = tk.Tk()
    gui = ConnectFourGUI(root)
    root.mainloop()