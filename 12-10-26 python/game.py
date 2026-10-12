# give in input for the Tic Tac Toe  game in two players
# function are not allow
# def in this not allow in this game

board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

player = "X"
count = 0

while count < 9:
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])

    print("\nPlayer", player, "turn")

    choice = input("Enter position (1-9): ")

    if choice not in "123456789" or len(choice) != 1:
        print("Invalid input! Enter a number from 1 to 9.")
        continue

    position = int(choice) - 1

    if board[position] == "X" or board[position] == "O":
        print("Position already taken! Try again.")
        continue

    board[position] = player
    count = count + 1

    if (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6]):

        print("\n")
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("--+---+--")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("--+---+--")
        print(board[6] + " | " + board[7] + " | " + board[8])

        print("\nPlayer", player, "wins!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"

if count == 9 and not (
    board[0] == board[1] == board[2] or
    board[3] == board[4] == board[5] or
    board[6] == board[7] == board[8] or
    board[0] == board[3] == board[6] or
    board[1] == board[4] == board[7] or
    board[2] == board[5] == board[8] or
    board[0] == board[4] == board[8] or
    board[2] == board[4] == board[6]
):
    print("\nGame Draw!")