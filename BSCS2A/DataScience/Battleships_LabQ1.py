import random


def the_board(size, player_position, enemy_attack, player_miss):
    board = []

    for i in range(size):
        board.append(["0"] * size)

    board[player_position[0]][player_position[1]] = "P"

    for attack in enemy_attack:
        row = attack[0]
        col = attack[1]

        if board[row][col] == "0":
            board[row][col] = "E"

    for miss in player_miss:
        row = miss[0]
        col = miss[1]

        if board[row][col] == "0":
            board[row][col] = "X"

    return board


def print_board(board):
    size = len(board)

    print("  ", end="")

    for i in range(size):
        print(i + 1, end=" ")

    print()

    for i in range(size):
        letter = chr(65 + i)

        print(letter, end=" ")

        for space in board[i]:
            print(space, end=" ")

        print()


def get_position(prompt, size):
    while True:
        position = input(prompt)
        parts = position.split(",")

        if len(parts) != 2:
            print("Invalid format. Please enter as row,col (e.g., 3,5).")
            continue

        row = parts[0]
        col = parts[1]

        if not row.isnumeric() or not col.isnumeric():
            print("Invalid format. Please enter as row,col (e.g., 3,5).")
            continue

        row = int(row)
        col = int(col)

        if row >= 1 and row <= size and col >= 1 and col <= size:
            return (row - 1, col - 1)

        print("Coordinates must be between 1 and " + str(size) + ". Try again.")


def main():
    print("Welcome to Battlecats! Meow!")
    print("You are Commander Meowsalot. Defeat Emperor Meowzer!")

    while True:
        size_input = input("Enter the size of the board, nya: ")

        if size_input.isnumeric():
            size = int(size_input)

            if size > 1:
                break
            else:
                print("Try again! Board size must be greater than 1.")
        else:
            print("Sorry! Please enter a valid integer!")

    player_pos = get_position(
        "Enter Commander's position (row,col): ", size
    )

    while True:
        enemy_row = random.randint(0, size - 1)
        enemy_col = random.randint(0, size - 1)

        enemy_pos = (enemy_row, enemy_col)

        if enemy_pos != player_pos:
            break

    enemy_hits = []
    player_misses = []

    board = the_board(size, player_pos, enemy_hits, player_misses)
    print_board(board)

    while True:
        print("\nHINT: Enter -1,-1 to reveal ENEMY!")

        guess = input("Guess enemy location (row,col): ")
        parts = guess.split(",")

        if len(parts) != 2:
            print("Invalid format. Use row,col (e.g., 4,7).")

            board = the_board(size, player_pos, enemy_hits, player_misses)
            print_board(board)

            continue

        row = parts[0]
        col = parts[1]

        if row == "-1" and col == "-1":
            r = -1
            c = -1

        elif row.isnumeric() and col.isnumeric():
            r = int(row)
            c = int(col)

        else:
            print("Invalid format. Use row,col (e.g., 4,7).")

            board = the_board(size, player_pos, enemy_hits, player_misses)
            print_board(board)

            continue

        if not ((1 <= r <= size) and (1 <= c <= size)) and (r, c) != (-1, -1):
            print("Coordinates must be between 1 and " + str(size) + ". Try again.")

            board = the_board(size, player_pos, enemy_hits, player_misses)
            print_board(board)

            continue

        if (r, c) == (-1, -1):
            print("Emperor Meowzer is at: (" + str(enemy_pos[0] + 1) + "," + str(enemy_pos[1] + 1) + ")")
            print("Commander Meowsalot revealed the enemy!")

            board = the_board(size, player_pos, enemy_hits, player_misses)
            print_board(board)

            continue

        elif (r - 1, c - 1) == enemy_pos:
            print("Commander Meowsalot found the enemy! You win!")

            board = the_board(size, player_pos, enemy_hits, player_misses)
            print_board(board)

            break

        elif (r - 1, c - 1) in player_misses:
            print("Commander Meowsalot already tried that spot! Choose a different location.")

            board = the_board(size, player_pos, enemy_hits, player_misses)
            print_board(board)

            continue

        else:
            print("Commander Meowsalot missed! Emperor's turn...")
            player_misses.append((r - 1, c - 1))

        enemy_row = random.randint(0, size - 1)
        enemy_col = random.randint(0, size - 1)

        enemy_guess = (enemy_row, enemy_col)

        enemy_hits.append(enemy_guess)

        print("Emperor Meowzer guesses: (" + str(enemy_guess[0] + 1) + "," + str(enemy_guess[1] + 1) + ")")

        if enemy_guess == player_pos:
            print("Emperor Meowzer found you! Game over.")

            board = the_board(size, player_pos, enemy_hits, player_misses)
            print_board(board)

            break

        else:
            print("Emperor Meowzer missed. Your turn again.")

        board = the_board(size, player_pos, enemy_hits, player_misses)
        print_board(board)


main()