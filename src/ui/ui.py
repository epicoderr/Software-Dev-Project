import pygame

# Most of these values I just asked AI what would be good
CELL_SIZE = 40  
BOARD_SIZE = 16 
HELPER_HEIGHT = 40
WINDOW_WIDTH = BOARD_SIZE * CELL_SIZE
WINDOW_HEIGHT = BOARD_SIZE * CELL_SIZE + HELPER_HEIGHT

WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def draw_board(screen, game_board, font):
    """Renders the current state of the Minesweeper board onto the Pygame screen.

    It iterates through every cell, determining its appearance based on its
    'isRevealed', 'isMine', 'isFlagged', and 'neighborCount' status.

    Args:
        screen: The Pygame surface to draw the board onto.
        game_board: The instance of the Minesweeper game containing the board state.
        font: The font object used for rendering neighbor counts, and helper.
    """
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            cell = game_board.board.grid[r][c]
            x = c * CELL_SIZE
            y = r * CELL_SIZE

            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            
            # The drawings were made with AI help
            if cell.is_revealed:
                pygame.draw.rect(screen, LIGHT_GRAY, rect)
                pygame.draw.rect(screen, DARK_GRAY, rect, 1) 

                if cell.is_mine:
                    pygame.draw.circle(screen, RED, rect.center, CELL_SIZE // 3)
                elif cell.neighbor_count > 0:
                    text_surface = font.render(str(cell.neighbor_count), True, BLUE)
                    text_rect = text_surface.get_rect(center=rect.center)
                    screen.blit(text_surface, text_rect)
            else:
                pygame.draw.rect(screen, DARK_GRAY, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)

                if cell.is_flagged:
                    pygame.draw.line(screen, RED, (x + CELL_SIZE // 4, y + CELL_SIZE // 4), (x + CELL_SIZE // 4, y + 3 * CELL_SIZE // 4), 3)
                    pygame.draw.polygon(screen, RED, [(x + CELL_SIZE // 4, y + CELL_SIZE // 4), (x + 3 * CELL_SIZE // 4, y + CELL_SIZE // 2), (x + CELL_SIZE // 4, y + 3 * CELL_SIZE // 4)])
            # AI help ends here

def draw_helper(screen, game_board, font):
    """Renders the controls of minesweeper for the user as text

    Args:
        screen: The Pygame surface to draw the text onto.
        game_board: The instance of the Minesweeper game containing the board state.
        font: The font object used for rendering neighbor counts and helper.
    """
    rect = pygame.Rect(0, BOARD_SIZE * CELL_SIZE, WINDOW_WIDTH, HELPER_HEIGHT)
    pygame.draw.rect(screen, LIGHT_GRAY, rect)
    pygame.draw.rect(screen, DARK_GRAY, rect, 2)

    flags_left = game_board.mines - game_board.flags

    text = f"Flags: {flags_left}    Left Click = Reveal    Right Click = Flag    R = Restart"
    text_surface = font.render(text, True, BLACK)

    text_rect = text_surface.get_rect(
        center=rect.center
    )
    screen.blit(text_surface, text_rect)
