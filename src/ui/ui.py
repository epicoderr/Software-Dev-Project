import pygame

CELL_SIZE = 30  
BOARD_SIZE = 16 
WINDOW_WIDTH = BOARD_SIZE * CELL_SIZE
WINDOW_HEIGHT = BOARD_SIZE * CELL_SIZE

WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def draw_board(screen, game_board, font):
    # Basically just helps create the board for the player
    # Might use assets later but this is sufficient for now
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            cell = game_board.board[r][c]
            x = c * CELL_SIZE
            y = r * CELL_SIZE

            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            
            # the drawings were made with ai help
            if cell["isRevealed"]:
                pygame.draw.rect(screen, LIGHT_GRAY, rect)
                pygame.draw.rect(screen, DARK_GRAY, rect, 1) 

                if cell["isMine"]:
                    pygame.draw.circle(screen, RED, rect.center, CELL_SIZE // 3)
                elif cell["neighborCount"] > 0:
                    text_surface = font.render(str(cell["neighborCount"]), True, BLUE)
                    text_rect = text_surface.get_rect(center=rect.center)
                    screen.blit(text_surface, text_rect)
            else:
                pygame.draw.rect(screen, DARK_GRAY, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)

                if cell["isFlagged"]:
                    pygame.draw.line(screen, RED, (x + CELL_SIZE // 4, y + CELL_SIZE // 4), (x + CELL_SIZE // 4, y + 3 * CELL_SIZE // 4), 3)
                    pygame.draw.polygon(screen, RED, [(x + CELL_SIZE // 4, y + CELL_SIZE // 4), (x + 3 * CELL_SIZE // 4, y + CELL_SIZE // 2), (x + CELL_SIZE // 4, y + 3 * CELL_SIZE // 4)])