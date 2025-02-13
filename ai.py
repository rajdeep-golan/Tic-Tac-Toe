import random
from utils import get_empty_cells, save_move

def ai_move(board):
    """AI makes a random move."""
    empty_cells = get_empty_cells(board)
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"
        save_move("O", row * 3 + col + 1)
