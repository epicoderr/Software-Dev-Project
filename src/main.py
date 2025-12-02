# pylint: disable=no-member

import sys
import pygame
from game.minesweeper import Minesweeper
from ui.ui import draw_board, CELL_SIZE, BOARD_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT, WHITE

def main():
    # Initializes the game, so creates the board then 40 mines
    # Also sets up the window for the player
    pygame.init()
    font = pygame.font.Font(None, 24)
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Minesweeper")
    clock = pygame.time.Clock()
    game_board = Minesweeper()
    game_board.new_game()

    while True:
        # Gameplay functions for the user
        # Click position is tracked by the set cell size
        # Clicks allow for revealing and flagging cells
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                col = mouse_x // CELL_SIZE
                row = mouse_y // CELL_SIZE

                if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                    if event.button == 1:
                        game_board.reveal_cell(row, col)
                        if game_board.game_over:
                            print("game over!! you hit a mine")
                            pygame.quit()
                            sys.exit()

                    elif event.button == 3:
                        cell = game_board.board[row][col]
                        if not cell["isRevealed"]:
                            game_board.toggle_flag(row, col)

        screen.fill(WHITE)
        draw_board(screen, game_board, font)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
