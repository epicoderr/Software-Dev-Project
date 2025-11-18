import random

#PLACEHOLDER VALUE MEANINGS FOR NOW
# 0 = UNREVEALED NON MINE
# 1 = REVEALED NON MINE, maybe I will make it based on how many mines are beside it
# 2 = MINE


class Minesweeper:
    def __init__(self, size=16):
        #Some initial values for the game, I am using the medium difficulty as the basis
        self.size = size
        self.board = [["0"]*size for _ in range(size)]
        self.mines = 40
        self.revealed = 0
    
    def create_puzzle(self):
        #generates 40 mines, the first click will have to be safe so this will be tweaked later
        positions = random.sample(
            [(r, c) for r in range(self.size) for c in range(self.size)],
            self.mines
        )
        
        for r, c in positions:
            self.board[r][c] = "2"
    
    def reveal_cell(self, r, c):
        #Will need to implement sometimes revealing more tiles next to it
        if self.board[r][c] == "2":
            self.game_over() #game is lost, will make that later
        self.board[r][c] = "1"
    
    def add_flag(self):
        return True
    
    def new_game(self):
        return True