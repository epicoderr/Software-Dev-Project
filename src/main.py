from game.minesweeper import Minesweeper

def main():
    # Initializes the game, so creates the board then 40 mines
    game_board = Minesweeper()
    game_board.create_board()
    game_board.create_puzzle()
    game_board.number_cells()

    print("Welcome to Minesweeper!")
    game_board.display()

    while True:
        # Player chooses what action to take
        print("\nCommands:")
        print("1: Reveal Cell")
        print("2: Flag Cell")
        print("3: New game")
        print("4: Exit")

        choice = input("Enter your choice: ").strip()

        # Choices 1 and 2 were implemented with the help of AI
        # This is only a temporary solution for testing purposes
        if choice == "1":
            while True:
                try:
                    pos = input("Enter cell to reveal (row, column): ")
                    row, column = map(int, pos.split(","))
                    game_board.reveal_cell(row, column)
                    game_board.display()
                    if game_board.board[row][column]["isMine"]:
                        print("The game is over")
                    break

                except ValueError:
                    print("Invalid input. Please enter two numbers like: 3,4")
                except IndexError:
                    print("That cell is outside the board. Try again.")

        elif choice == "2":
            while True:
                try:
                    pos = input("Enter cell to reveal (row, column): ")
                    row, column = map(int, pos.split(","))
                    game_board.add_flag(row, column)
                    game_board.display()
                    break

                except ValueError:
                    print("Invalid input. Please enter two numbers like: 3,4")
                except IndexError:
                    print("That cell is outside the board. Try again.")

        elif choice == "3":
            game_board.new_game()
            game_board.display()

        elif choice == "4":
            print("Exiting game....")
            break
        else:
            print("Invalid command. Please try again.")
            continue


if __name__ == "__main__":
    main()
