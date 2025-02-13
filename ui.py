import pygame
import sys

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (0, 0, 0)
FONT = pygame.font.Font(None, 100)

def draw_board(screen, board):
    """Draws the game board and marks."""
    screen.fill(WHITE)

    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * 200), (600, i * 200), 5)
        pygame.draw.line(screen, LINE_COLOR, (i * 200, 0), (i * 200, 600), 5)

    for row in range(3):
        for col in range(3):
            if board[row][col] != " ":
                text_surface = FONT.render(board[row][col], True, BLACK)
                screen.blit(text_surface, (col * 200 + 50, row * 200 + 30))

    pygame.display.update()

def show_result_screen(screen, message, game):
    """Displays the result screen and buttons for play again/exit."""
    screen.fill(WHITE)
    font = pygame.font.Font(None, 50)
    text = font.render(message, True, BLACK)
    screen.blit(text, (150, 250))

    play_again_button = pygame.Rect(100, 350, 210, 50)
    exit_button = pygame.Rect(350, 350, 150, 50)

    pygame.draw.rect(screen, BLACK, play_again_button, border_radius=10)
    pygame.draw.rect(screen, BLACK, exit_button, border_radius=10)

    screen.blit(font.render("Play Again", True, WHITE), (120, 360))
    screen.blit(font.render("Exit", True, WHITE), (380, 360))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.collidepoint(event.pos):
                    game.reset_game()
                    return
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
