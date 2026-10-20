'''P6. Guessing menu (while loop and input validation)
Choose a fixed secret number in the program. Keep asking the player to guess until they are correct or enter 0 to quit.
Give higher/lower hints, count attempts, and reject guesses outside 1-100.'''

secret = 50
attempts = 0

while True:
    guess = int(input("Guess a number (1-100) or enter 0 to quit: "))

    if guess == 0:
        print("You quit the game.")
        break

    if guess < 1 or guess > 100:
        print("Invalid guess! Enter a number from 1 to 100.")
        continue

    attempts = attempts + 1

    if guess < secret:
        print("Higher!")
    elif guess > secret:
        print("Lower!")
    else:
        print("Correct! You guessed the number.")
        print("Attempts:", attempts)
        break