import random

class Minesweeper:
    def __init__(self, size=16):
        # Some initial values for the game, I am using the medium difficulty as the basis for now
        self.mines = 40
        self.revealed = 0
        self.board = []
        self.size = size
        self.game_over = False

    def new_game(self):
        # Initializes a new game
        self.board = []
        self.create_board()
        self.create_puzzle()
        self.number_cells()

    def create_board(self):
        # Creates the board by giving four properties to each cell
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

    def create_puzzle(self):
        # Generates 40 mines to start the game
        positions = random.sample(
            [(r, c) for r in range(self.size) for c in range(self.size)],
            self.mines
        )

        for r, c in positions:
            self.board[r][c]["isMine"] = True

    def reveal_cell(self, r, c):
        # Reveals the tile and then all other tiles with no mine neighbors
        # First reveal will have to be safe, will implement later
        rows = len(self.board)
        cols = len(self.board[0])
        if not (0 <= r < rows and 0 <= c < cols):
            return

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
        if self.board[r][c]["isFlagged"]:
            self.board[r][c]["isFlagged"] = False
        else:
            self.board[r][c]["isFlagged"] = True

    def number_cells(self):
        # Computes how many mines are nearby for each non-mine cell
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if not self.board[i][j]["isMine"]:
                    self.check_mines(i, j)

    def check_mines(self, r, c):
        # Computes how many mines are nearby for a cell, so checks all adjacent positions
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
