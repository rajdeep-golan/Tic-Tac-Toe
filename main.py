import pygame

#Initialising the game
pygame.init()

import sys
import random
from ui import draw_board, show_result_screen
from ai import ai_move
from utils import save_move, check_winner, get_empty_cells


class TicTacToeGame:
    """Handles the Tic-Tac-Toe game logic."""
    
    def __init__(self):
        self.WIDTH, self.HEIGHT = 600, 600
        self.CELL_SIZE = self.WIDTH // 3
        self.players = ["X", "O"]
        self.current_player = random.choice(self.players)
        self.against_ai = False
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.running = True
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Tic-Tac-Toe")

    def reset_game(self):
        """Resets the game board and variables."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = random.choice(self.players)
        self.running = True

    def handle_click(self, x, y):
        """Processes user clicks for making moves."""
        row, col = y // self.CELL_SIZE, x // self.CELL_SIZE

        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            save_move(self.current_player, row * 3 + col + 1)

            winner = check_winner(self.board)
            if winner:
                show_result_screen(self.screen, f"Player {winner} Wins!", self)
                return

            if not get_empty_cells(self.board):
                show_result_screen(self.screen, "It's a Draw!", self)
                return

            self.current_player = "O" if self.current_player == "X" else "X"

            if self.against_ai and self.current_player == "O":
                ai_move(self.board)
                winner = check_winner(self.board)
                if winner:
                    show_result_screen(self.screen, f"Player {winner} Wins!", self)
                    return
                self.current_player = "X"

    def run(self):
        """Main game loop."""
        print("Welcome to Tic-Tac-Toe!")
        print("When Pygame window opens, click on a cell to make a move.")
        self.against_ai = input("Play against AI? (yes/no): ").strip().lower() == "yes"

        while True:
            draw_board(self.screen, self.board)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and self.running:
                    self.handle_click(event.pos[0], event.pos[1])

if __name__ == "__main__":
    game = TicTacToeGame()
    game.run()
