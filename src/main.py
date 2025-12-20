# pylint: disable=no-member

import sys
import pygame
from game.minesweeper import Minesweeper
from ui.ui import draw_board, draw_helper, CELL_SIZE, BOARD_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT, WHITE

def main():
    """Initializes the Pygame environment and runs the main Minesweeper game loop.

    Handles game setup, event processing (mouse clicks, key presses), and rendering
    the game state to the screen.
    """

    pygame.init()
    font = pygame.font.Font(None, 24)
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Minesweeper")
    clock = pygame.time.Clock()
    game_board = Minesweeper()
    game_board.new_game()

    while True:
        # Click position is tracked by the set cell size
        # Clicks allow for revealing and flagging cells
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_board.new_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                if mouse_y < BOARD_SIZE * CELL_SIZE:
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
                        cell = game_board.board.grid[row][col]
                        if not cell.is_revealed:
                            game_board.toggle_flag(row, col)

        screen.fill(WHITE)
        draw_board(screen, game_board, font)
        draw_helper(screen, font)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
