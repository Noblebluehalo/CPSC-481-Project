import tkinter as tk
import math
import threading
from game_logic import ConnectFour
from ai_agent import minimax, AI_PIECE, PLAYER_PIECE
from explanations import explain_move

SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)
BLUE = "#0000FF"
BLACK = "#000000"
RED = "#FF0000"
YELLOW = "#FFFF00"
ANIMATION_SPEED = 25 # Lower is faster (milliseconds per frame)
ANIMATION_STEP = 20  # Pixels moved per frame

class ConnectFourGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four AI")
        self.game = ConnectFour()
        
        self.difficulty = tk.IntVar(value=3)
        self.starting_player = tk.IntVar(value=PLAYER_PIECE) 
        self.is_animating = False
        
        self.setup_ui()
        self.restart()

    def setup_ui(self):
        controls = tk.Frame(self.root)
        controls.pack(pady=5)
        
        tk.Label(controls, text="Difficulty (Depth):").pack(side=tk.LEFT)
        tk.Scale(controls, from_=1, to=6, variable=self.difficulty, orient=tk.HORIZONTAL).pack(side=tk.LEFT, padx=10)
        
        tk.Label(controls, text="Starts:").pack(side=tk.LEFT)
        tk.Radiobutton(controls, text="Human", variable=self.starting_player, value=PLAYER_PIECE).pack(side=tk.LEFT)
        tk.Radiobutton(controls, text="AI", variable=self.starting_player, value=AI_PIECE).pack(side=tk.LEFT)
        
        tk.Button(controls, text="Restart", command=self.restart).pack(side=tk.LEFT, padx=10)
        
        self.info_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.info_label.pack(pady=5)

        # Extra row at the top for the piece to appear before dropping
        self.canvas = tk.Canvas(self.root, width=self.game.columns*SQUARESIZE, height=(self.game.rows+1)*SQUARESIZE, bg=BLACK)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.handle_click)

    def draw_board(self):
        self.canvas.delete("board_element")
        for c in range(self.game.columns):
            for r in range(self.game.rows):
                x0 = c * SQUARESIZE
                y0 = (r + 1) * SQUARESIZE
                x1 = x0 + SQUARESIZE
                y1 = y0 + SQUARESIZE
                # Tagging these elements allows the animated piece to be drawn without wiping the canvas
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=BLUE, tags="board_element")
                
                piece = self.game.board[r][c]
                color = BLACK
                if piece == PLAYER_PIECE:
                    color = RED
                elif piece == AI_PIECE:
                    color = YELLOW
                    
                cx = x0 + SQUARESIZE/2
                cy = y0 + SQUARESIZE/2
                self.canvas.create_oval(cx-RADIUS, cy-RADIUS, cx+RADIUS, cy+RADIUS, fill=color, tags="board_element")

    def _get_open_row(self, col):
        for r in range(self.game.rows-1, -1, -1):
            if self.game.board[r][col] == 0:
                return r
        return -1

    def animate_piece(self, col, target_row, piece, callback):
        self.is_animating = True
        
        # Starting coordinates (top of the board, above the grid)
        cx = col * SQUARESIZE + SQUARESIZE / 2
        cy = SQUARESIZE / 2
        
        color = RED if piece == PLAYER_PIECE else YELLOW
        piece_id = self.canvas.create_oval(cx - RADIUS, cy - RADIUS, cx + RADIUS, cy + RADIUS, fill=color)
        
        target_y = (target_row + 1) * SQUARESIZE + SQUARESIZE / 2
        
        def move_down():
            coords = self.canvas.coords(piece_id)
            current_y = (coords[1] + coords[3]) / 2
            
            if current_y < target_y:
                self.canvas.move(piece_id, 0, ANIMATION_STEP)
                self.root.after(ANIMATION_SPEED, move_down)
            else:
                self.canvas.delete(piece_id)
                self.is_animating = False
                callback()
                
        move_down()

    def handle_click(self, event):
        # Ignore clicks if game is over, it's AI's turn, or an animation is currently running
        if self.game.is_terminal_node() or self.game.current_turn != PLAYER_PIECE or self.is_animating:
            return

        col = int(math.floor(event.x / SQUARESIZE))
        
        if self.game.is_valid_location(col):
            target_row = self._get_open_row(col)
            self.animate_piece(col, target_row, PLAYER_PIECE, lambda: self._post_player_move(col))

    def _post_player_move(self, col):
        self.game.drop_piece(col, PLAYER_PIECE)
        self.draw_board()
        
        if self.game.check_win(PLAYER_PIECE):
            self.info_label.config(text="Player Wins!")
            return
            
        self.game.current_turn = AI_PIECE
        self.info_label.config(text="AI is thinking...")
        self.ai_move()

    def ai_move(self):
        threading.Thread(target=self._ai_worker, daemon=True).start()

    def _ai_worker(self):
        col, _, nodes = minimax(self.game, self.difficulty.get(), -math.inf, math.inf, True)
        self.root.after(0, self._apply_ai_move, col, nodes)

    def _apply_ai_move(self, col, nodes):
        if col is not None:
            target_row = self._get_open_row(col)
            self.animate_piece(col, target_row, AI_PIECE, lambda: self._post_ai_move(col, nodes))

    def _post_ai_move(self, col, nodes):
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
        self.is_animating = False
        self.draw_board()
        
        if self.game.current_turn == AI_PIECE:
            self.info_label.config(text="AI is thinking...")
            self.ai_move()
        else:
            self.info_label.config(text="Your Turn (Red)")

if __name__ == "__main__":
    root = tk.Tk()
    gui = ConnectFourGUI(root)
    root.mainloop()