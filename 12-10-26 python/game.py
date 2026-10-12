# give in input for the game in two players
# function are not allow
# def in this not allow in this game
# Tic Tac Toe and check the winner in the game and print the winner name in the game and also check the draw in the game and print the draw in the game and also check the invalid input in the game and print the invalid input in the game and also check the player turn in the game and print the player turn in the game and also check the player win in the game and print the player win in the game and also check the player lose in the game and print the player lose in the game and also check the player tie in the game and print the player tie in the game and also check the player quit in the game and print the player quit in the game and also check the player restart in the game and print the player restart in the game and also check the player exit in the game and print the player exit inthe game and also checkthe player help inthe game and printthe player help inthe game and also checkthe player about inthe game and printthe player about inthe game and also checkthe player settings inthe game and printthe player settings inthe game and also checkthe player sound inthe game and printthe player sound inthe game and also checkthe player music inthe game and printthe player music inthe game and also checkthe player graphics inthe game and printthe player graphics inthe game and also checkthe player controls inthe game and printthe player controls inthe game and also checkthe player difficulty inthe game and printthe player difficulty inthe game and also checkthe player level inthe game and printthe player level inthe game和也check_the_player_score_in_the_game_and_print_the_player_score_in_the_game_and_also_check_the_player_highscore_in_the_game_and_print_the_player_highscore_in_the_game_and_also_check_the_player_leaderboard_in_the_game_and_print_the_player_leaderboard_in_the_game_and_also_check_the_player_achievements_in_the_game_and_print_the_player_achievements_in_the_game_and_also_check_the_player_stats_in_the_game_and_print_the_player_stats_in_the_game_and_also_check_the_player_profile_in_the_game_and_print_the_player_profile_in_the_game_and_also_check_the_player_login_in-the-game-and-print-the-player-login-in-the-game-and-also-check-the-player-logout-in-the-game-and-print-the-player-logout-in-the-game-and-also-check-the-player-register-in-the-game-and-print-the-player-register-in-the-game-and-also-check-the-player-forgot-password-in-the-game-and-print-the-player-forgot-password-in-the-game-and-also-check-the-player-reset-password-in-the-game-and-print-the-player-reset-password-in-the-game-and-also-check-the-player-change-password-in-the-game-and-print-the-player-change-password-in-the-game-and-also-check-the-player-update-profile-in-the-game-and-print-the-player-update-profile-in-the-game

board = [" " for i in range(9)]

player1 = input("Enter Player 1 name: ")
player2 = input("Enter Player 2 name: ")

players = ["X", "O"]
names = [player1, player2]
scores = [0, 0]

print("\n===== TIC TAC TOE =====")
print("Player 1:", player1, "(X)")
print("Player 2:", player2, "(O)")

game = "yes"

while game == "yes":

    board = [" " for i in range(9)]
    turn = 0
    winner = ""

    while turn < 9 and winner == "":

        print("\n", board[0], "|", board[1], "|", board[2])
        print("---+---+---")
        print("", board[3], "|", board[4], "|", board[5])
        print("---+---+---")
        print("", board[6], "|", board[7], "|", board[8])

        print("\nPlayer turn:", names[turn % 2])
        print("Symbol:", players[turn % 2])
        print("Enter position 1-9")
        print("Type help, score, quit, restart, or exit")

        choice = input("Enter your choice: ").lower().strip()

        if choice == "help":
            print("Choose a position from 1 to 9.")
            print("Get three symbols in a row to win.")

        elif choice == "about":
            print("Tic Tac Toe is a two-player game.")

        elif choice == "score":
            print(player1, "score:", scores[0])
            print(player2, "score:", scores[1])

        elif choice == "settings":
            print("Settings: Two players, X and O.")

        elif choice == "sound":
            print("Sound setting is not available.")

        elif choice == "music":
            print("Music setting is not available.")

        elif choice == "graphics":
            print("Graphics setting is not available.")

        elif choice == "controls":
            print("Controls: Enter a number from 1 to 9.")

        elif choice == "difficulty":
            print("Difficulty: Normal.")

        elif choice == "level":
            print("Level: 1")

        elif choice == "highscore":
            print("High score:", max(scores))

        elif choice == "leaderboard":
            print("Leaderboard:")
            print(player1, scores[0])
            print(player2, scores[1])

        elif choice == "achievements":
            print("Achievements: Win your first game!")

        elif choice == "stats":
            print("Player statistics:")
            print(player1, scores[0])
            print(player2, scores[1])

        elif choice == "profile":
            print("Player 1:", player1)
            print("Player 2:", player2)

        elif choice == "login":
            print("Players are already entered.")

        elif choice == "logout":
            print("Logout is not available during the game.")

        elif choice == "register":
            print("Player registration is completed.")

        elif choice == "forgot password":
            print("Password recovery is not required.")

        elif choice == "reset password":
            print("Password reset is not available.")

        elif choice == "change password":
            print("Password change is not available.")

        elif choice == "update profile":
            player1 = input("Enter new Player 1 name: ")
            player2 = input("Enter new Player 2 name: ")
            names = [player1, player2]
            print("Profile updated successfully.")

        elif choice == "quit":
            print(names[turn % 2], "quit the game.")
            print(names[(turn + 1) % 2], "wins by quitting.")
            scores[(turn + 1) % 2] += 1
            winner = "quit"

        elif choice == "restart":
            print("Game restarted!")
            winner = "restart"

        elif choice == "exit":
            print("Game exited.")
            game = "no"
            winner = "exit"

        elif choice.isdigit() and int(choice) >= 1 and int(choice) <= 9:

            position = int(choice) - 1

            if board[position] == " ":
                board[position] = players[turn % 2]

                if (
                    board[0] == board[1] == board[2] != " " or
                    board[3] == board[4] == board[5] != " " or
                    board[6] == board[7] == board[8] != " " or
                    board[0] == board[3] == board[6] != " " or
                    board[1] == board[4] == board[7] != " " or
                    board[2] == board[5] == board[8] != " " or
                    board[0] == board[4] == board[8] != " " or
                    board[2] == board[4] == board[6] != " "
                ):
                    winner = names[turn % 2]
                    scores[turn % 2] += 1
                    print("\nCongratulations!", winner, "wins!")
                    print(names[(turn + 1) % 2], "loses!")

                turn += 1

            else:
                print("Invalid input! This position is already occupied.")

        else:
            print("Invalid input! Enter 1-9 or a valid command.")

    if game == "yes" and winner == "":
        print("\nIt's a draw! Both players tie.")

    print("\nFinal Board:")
    print(board[0], "|", board[1], "|", board[2])
    print("---+---+---")
    print(board[3], "|", board[4], "|", board[5])
    print("---+---+---")
    print(board[6], "|", board[7], "|", board[8])

    if game == "yes":
        print("\n===== SCOREBOARD =====")
        print(player1, ":", scores[0])
        print(player2, ":", scores[1])

        game = input("\nPlay again? (yes/no): ").lower().strip()

        if game == "yes":
            print("Starting a new game!")
        elif game != "no":
            print("Invalid choice. Game ended.")
            game = "no"

print("\nThanks for playing Tic Tac Toe!")
print("Final Score:")
print(player1, ":", scores[0])
print(player2, ":", scores[1])