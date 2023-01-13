# Guessing game.

# References:
# https://www.khanacademy.org/computing/computer-science/algorithms/intro-to-algorithms/a/a-guessing-game
# https://www.geeksforgeeks.org/round-function-python/


def get_guess(i):
    print(f"Enter 'h' if your number is higher than {i:.0f}. " +
          f"\nEnter 'l' if your number is lower than {i:.0f}. " +
          f"\nEnter 'e' if your number is equal to {i:.0f}. ")
    guess = input()
    return guess


def main():
    print("Guess any number between 0 and 100")
    array = []
    count = 0
    low = 0
    high = 100
    while True:
        guess = (low + high) / 2
        array.append(round(guess))
        response = get_guess(guess)
        count = count + 1
        if response == "h":
            low = guess
        elif response == "l":
            high = guess
        elif response == "e":
            print(f"Your number is {guess:.0f} at {count:.0f} guess.")
            break
    print("array of guesses made:")
    print(array)


main()