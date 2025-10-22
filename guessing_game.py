def guessing_game():
    # TODO create guessing game function
    # HINT: Target number should be 15
    # HINT: Return message should be "Congratulations! You guessed it!"
    # HINT: Use input("Enter your guess: ") for user input
    # HINT: Print "Too low! Try again." for low guesses
    # HINT: Print "Too high! Try again." for high guesses
    target = 15;
    answer = 0
    while answer != target:
        answer = int(input("Enter your guess: "))
        if answer == target:
            break
        elif answer > target:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
    return "Congratulations! You guessed it!"


    pass

if __name__ == "__main__":
    # create guessing game below this
    guessing_game()
