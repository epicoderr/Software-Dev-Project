from game.board import Board

class Minesweeper:
    """A class to represent the Minesweeper game logic.

    Attributes:
        mines: The total number of mines on the board.
        revealed: The count of non-mine cells revealed so far (currently unused in provided code).
        board: The Board class which represents the game board cells.
        size: The dimension of the square board (e.g., size=16 means 16x16 board).
        game_over: Flag indicating if the game has ended.
        first_click: Flag indicating if the first move of the game is yet to be made.
    """

    def __init__(self, size=16, mines=40):
        """Initializes a new Minesweeper game instance.

        Args:
            size: The dimension of the square board. Defaults to 16 (medium difficulty basis).
        """
        self.mines = mines
        self.size = size
        self.board = None
        self.revealed = 0
        self.flags = 0
        self.game_over = False
        self.first_click = True

        self.new_game()

    def new_game(self):
        """Initializes a new game board and resets the first_click flag."""
        self.board = Board(self.size, self.mines)
        self.revealed = 0
        self.flags = 0
        self.game_over = False
        self.first_click = True

    def reveal_cell(self, r, c):
        """Reveals a cell on board and recursively reveals adjacent zero-neighbor cells

        Args:
            r: The row of the first clicked cell.
            c: The column of the first clicked cell.
        """
        if not (0 <= r < self.size and 0 <= c < self.size):
            return

        if self.first_click:
            self.board.create_puzzle(r, c)
            self.board.number_cells()
            self.first_click = False

        cell = self.board.grid[r][c]

        if cell.is_revealed or cell.is_flagged:
            return

        if cell.is_mine:
            cell.is_revealed = True
            self.game_over = True
            return

        cell.is_revealed = True

        self.revealed += 1
        safe_cells = (self.size * self.size) - self.mines
        if self.revealed == safe_cells:
            print("All safe cells revealed!")

        if cell.neighbor_count > 0:
            return

        for nr, nc in self.board.neighbors(r, c):
            self.reveal_cell(nr, nc)

    def toggle_flag(self, r, c):
        """Toggles the 'isFlagged' status of a cell at (r, c).

        Args:
            r: The row of the cell.
            c: The column of the cell.
        """
        if self.first_click:
            return

        if not (0 <= r < self.size and 0 <= c < self.size):
            return

        if self.board.grid[r][c].is_flagged:
            self.board.grid[r][c].is_flagged = False
            self.flags -= 1
        else:
            if self.flags >= self.mines:
                return
            self.board.grid[r][c].is_flagged = True
            self.flags += 1
