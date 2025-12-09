import random

class Minesweeper:
    """A class to represent the Minesweeper game logic.

    Attributes:
        mines: The total number of mines on the board.
        revealed: The count of non-mine cells revealed so far (currently unused in provided code).
        board: The 2D list representing the game board cells.
        size: The dimension of the square board (e.g., size=16 means 16x16 board).
        game_over: Flag indicating if the game has ended.
        first_click: Flag indicating if the first move of the game is yet to be made.
    """

    def __init__(self, size=16):
        """Initializes a new Minesweeper game instance.

        Args:
            size: The dimension of the square board. Defaults to 16 (medium difficulty basis).
        """
        self.mines = 40
        self.revealed = 0
        self.board = []
        self.size = size
        self.game_over = False
        self.first_click = True

    def new_game(self):
        """Initializes a new game board and resets the first_click flag."""
        self.board = []
        self.create_board()
        self.first_click = True

    def create_board(self):
        """Creates the initial, empty game board.

        Each cell is a dictionary with properties: "isMine", "neighborCount",
        "isFlagged", and "isRevealed".
        """
        for _ in range(self.size):
            row = []
            for _ in range(self.size):
                cell = {
                "isMine": False,
                "neighborCount": 0,
                "isFlagged": False,
                "isRevealed": False
                }
                row.append(cell)
            self.board.append(row)

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
            forbidden.add((nr, nc))

        available = [
        (r, c)
        for r in range(self.size)
        for c in range(self.size)
        if (r, c) not in forbidden
        ]
        # AI help ends here

        positions = random.sample(available, self.mines)
        for row, col in positions:
            self.board[row][col]["isMine"] = True

    def reveal_cell(self, r, c):
        """Reveals a cell on board and recursively reveals adjacent zero-neighbor cells

        Args:
            r: The row of the first clicked cell.
            c: The column of the first clicked cell.
        """

        rows = len(self.board)
        cols = len(self.board[0])
        if not (0 <= r < rows and 0 <= c < cols):
            return

        if self.first_click:
            self.create_puzzle(r, c)
            self.number_cells()
            self.first_click = False

        cell = self.board[r][c]

        if cell["isRevealed"] or cell["isFlagged"]:
            return

        if cell["isMine"]:
            cell["isRevealed"] = True
            self.game_over = True
            return

        cell["isRevealed"] = True

        if cell["neighborCount"] > 0:
            return


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
            self.reveal_cell(nr, nc)

    def toggle_flag(self, r, c):
        """Toggles the 'isFlagged' status of a cell at (r, c).

        Args:
            r: The row of the cell.
            c: The column of the cell.
        """
        if self.board[r][c]["isFlagged"]:
            self.board[r][c]["isFlagged"] = False
        else:
            self.board[r][c]["isFlagged"] = True

    def number_cells(self):
        """Iterates over the board and computes the mine neighbor count for every
        cell that is not a mine, by calling check_mines on every mine cell."""
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if not self.board[i][j]["isMine"]:
                    self.check_mines(i, j)

    def check_mines(self, r, c):
        """Computes how many mines are nearby for a non-mine cell at (r, c) 
        and sets its neighborCount.

        Args:
            r: The row of the cell.
            c: The column of the cell.
        """
        rows = len(self.board)
        cols = len(self.board[0])

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
        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if self.board[nr][nc]["isMine"]:
                    count += 1
        self.board[r][c]["neighborCount"] = count
