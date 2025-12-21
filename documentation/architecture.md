# Architecture Document

## Overview

This document describes the structure and logic of a Minesweeper game implemented in Python using Pygame. The game follows a modular architecture separating game logic from the user interface.

## Structure

The project consists of four main components:

Game Logic (Minesweeper): Handles cell revealing, toggling flags and game rules.

Board: Handles creation of the board, placement of mines

Cells (Cell): Represent individual squares on the board, storing mine status, neighbor counts, and flag/reveal states.

User Interface (UI): Handles rendering the board using Pygame and user interactions (left-click for reveal, right-click for flag).

## Game Logic
### Board Initialization

New Game: Resets the board.

Board Creation: Populates the board with cells.

Mine Placement: Randomly assigns mines to cells while ensuring the first clicked cell is safe.

Neighbor Count: Computes the number of adjacent mines for each non-mine cell.

### Gameplay Mechanics

Reveal Cell:

If a mine is revealed → game over.

If neighbor mine count is higher than zero, reveal only the cell.

If neighbor mine count is equal to zero, recursively reveal adjacent cells.

Toggle Flag: Marks or unmarks a cell as a suspected mine.

## Class Diagram
```mermaid
classDiagram

    class Minesweeper {
        new_game()
        create_board()
        reveal_cell(r, c)
        add_flag(r, c)
        display()
    }

    class Board {
        create_puzzle()
        number_cells()
        check_mines()
        neighbors(r, c)
        in_bounds(r, c)
    }

    class Cell {
        bool isMine
        int neighborCount
        bool isFlagged
        bool isRevealed
    }
    
    Minesweeper "1" *-- "1" Board : owns
    Board "1" *-- "*" Cell : contains

```
## Sequence Diagram
```mermaid
sequenceDiagram
    participant Main
    participant Game as Minesweeper 
    participant Board
    participant UI
    participant Cell

%% --- Game Initialization ---
    Main->>Game: __init__(size, mines)
    Main->>Game: new_game()
    activate Game
    Game->>Board: __init__(size, mine_count)
    Board->>Cell: create all Cell instances
    Game->>Board:: create_puzzle()
    Game->>Board:: number_cells()
    deactivate Game
    Main->>UI: pygame.init()
    Main->>UI: draw_board(screen, game_board, font)

    %% --- Player Clicks (Left/Reveal) ---
    Main->>Game: reveal_cell(r, c)
    activate Game
    Game->>Board: access cell at (r, c)
    Board->>Cell: check is_revealed, is_flagged
    alt Hit Mine
    Game->>Game: cell.is_mine = True
        Game->>Game: cell.is_revealed = True
        Game-->>Main: Return (Game Over)
    else Safe Reveal (Neighbor Count > 0)
        Game->>Game: cell.is_revealed = True
        Game-->>Main: Return
    else Safe Reveal (Neighbor Count = 0)
        Game->>Game: cell.is_revealed = True
        loop for dr, dc in directions
            Game->>Game: reveal_cell(nr, nc)
        end
        Game-->>Main: Return
    end
    deactivate Game
    Main->>UI: draw_board()

    %% --- Player Clicks (Right/Flag) ---
    Main->>Game: toggle_flag(r, c)
    activate Game
    Game->>Board: access cell at (r, c)
    Cell->>Cell: toggle is_flagged
    deactivate Game
    Main->>UI: draw_board()

```



