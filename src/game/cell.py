class Cell:
    """A class to represent a single cell on a board of minesweeper.

    Attributes:
        is_mine(bool): whether the cell is a mine
        is_revealed(bool): whether the cell is revealed
        is_flagged(bool): whether the cell is flagged
        neighbor_count(int): the amount of mines adjacent to the cell
    """

    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.neighbor_count = 0
