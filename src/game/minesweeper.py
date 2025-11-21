import random

class Minesweeper:
    def __init__(self, size=16):
        # Some initial values for the game, I am using the medium difficulty as the basis for now
        self.mines = 40
        self.revealed = 0
        self.board = []
        self.size = size

    def new_game(self):
        # Initializes a new game
        self.create_board()
        self.create_puzzle()
        self.number_cells()

    def create_board(self):
        # Creates the board by giving four properties to each cell
        # Size is based on self.size, might add difficulty levels later so this may be mutable
        for i in range(self.size):
            row = []
            for j in range(self.size):
                cell = {
                "isMine": False,
                "neighborCount": 0,
                "isFlagged": False,
                "isRevealed": False
                }
                row.append(cell)
            self.board.append(row)
    
    def create_puzzle(self):
        # Generates 40 mines, the first click will have to be safe so this will be tweaked later
        positions = random.sample(
            [(r, c) for r in range(self.size) for c in range(self.size)],
            self.mines
        )
        
        for r, c in positions:
            self.board[r][c]["isMine"] = True

    def reveal_cell(self, r, c):
        # Will need to implement sometimes revealing more tiles next to it
        self.board[r][c]["isRevealed"] = True
        if self.board[r][c]["isMine"] == True:
            self.game_over() #game is lost, will make that later
    
    def add_flag(self, r, c):
        self.board[r][c]["isFlagged"] = True

    def display(self):
        # Used ai for this, its just a text based display to test things out for now
        print("    " + " ".join(f"{i:2}" for i in range(self.size)))
        print("   " + "---" * self.size)

        for r in range(self.size):
            row_str = f"{r:2} |"
            for c in range(self.size):
                form = self.check_form(r, c)

                if form == "hidden":
                    row_str += " ? "
                elif form == "flag":
                    row_str += " F "
                elif form == "mine":
                    row_str += " * "
                else:
                    row_str += f" {form if form > 0 else ' '} "
            print(row_str)

    
    def number_cells(self):
        # Computes how many mines are nearby for each non-mine cell
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j]["isMine"] != True:
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
                if self.board[nr][nc] == "*":
                    count += 1
        self.board[r][c]["neighborCount"] = count
        
    def check_form(self, r, c):
        # Checks the properties of a cell in order to find the correct way to display it
        cell = self.board[r][c]
        if not cell["isRevealed"]:
            if cell["isFlagged"]:
                return "flagged"
            return "hidden"
        if cell["isMine"]:
            return "mine"
        
        return self.board[r][c]["neighborCount"]
    
    def game_over(self):
        return "the game is over!!!"
