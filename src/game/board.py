import random
from game.cell import Cell

class Board:
    """A class to represent the Board for minesweeper.

    Attributes:
        mine_count: The total number of mines on the board.
        size: The dimension of the square board (e.g., size=16 means 16x16 board).
        grid: The 2D list representing the game board cells.
    """

    def __init__(self, size, mine_count):
        """Initializes a new Minesweeper game instance.

        Args:
            size: The dimension of the square board. Defaults to 16 (medium difficulty basis).
        """
        self.mine_count = mine_count
        self.size = size
        self.grid = [
            [Cell() for _ in range(size)]
            for _ in range(size)
        ]

    def create_puzzle(self, r, c):
        """Generates and places mines randomly on the board, ensuring the first-clicked cell
        and its neighbors are safe.

        Args:
            r: The row of the first clicked cell.
            c: The column of the first clicked cell.
        """

        # AI was used for help in the creation of the safe first click
        forbidden = set()
        forbidden.add((r, c))

        for nr, nc in self.neighbors(r, c):
            forbidden.add((nr, nc))

        available = [
        (r, c)
        for r in range(self.size)
        for c in range(self.size)
        if (r, c) not in forbidden
        ]
        # AI help ends here

        positions = random.sample(available, self.mine_count)
        for row, col in positions:
            self.grid[row][col].is_mine = True

    def number_cells(self):
        """Iterates over the board and computes the mine neighbor count for every
        cell that is not a mine, by calling check_mines on every non-mine cell."""
        for i in range(self.size):
            for j in range(self.size):
                if not self.grid[i][j].is_mine:
                    self.check_mines(i, j)

    def check_mines(self, r, c):
        """Computes how many mines are nearby for a non-mine cell at (r, c) 
        and sets its neighborCount.

        Args:
            r: The row of the cell.
            c: The column of the cell.
        """
        count = 0
        for nr, nc in self.neighbors(r, c):
            if self.grid[nr][nc].is_mine:
                count += 1
        self.grid[r][c].neighbor_count = count

    def in_bounds(self, r, c):
        return 0 <= r < self.size and 0 <= c < self.size
    
    def neighbors(self, r, c):
        directions = [
        (-1,  0),
        ( 1,  0),
        ( 0, -1),
        ( 0,  1),
        (-1, -1),
        (-1,  1),
        ( 1, -1),
        ( 1,  1),
        ]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if self.in_bounds(nr, nc):
                yield nr, nc
