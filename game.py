"""A number-guessing game."""

# Put your code here
from random import randint

def round(name):
    number = randint(1, 100)
    print(f"\nOk, {name}, I'm thinking of a number between 1 and 100. Can you guess it?")

    count = 0

    while True:
        guess = input("What's my number? ")
        try:
            guess = int(guess)
        except ValueError:
            print("Please guess an integer.")
            continue
        if guess < 1 or guess > 100:
            print("Your guess is out of range. Pick a number between 1 and 100, please.")
            continue
        count += 1
        if guess == number:
            print (f"You guessed my number in {count} tries, {name}!\n")
            return count
        elif guess < number:
            print ("Too low.")
        else:
            print ("Too high.")

def playAgain():
    while True:
        again = input("Would you like to play again? [y/n] ")
        if again == "n":
            return False
        elif again == "y":
            return True
        else:
            print("Please respond with 'y' or 'n' only.")


def main():
    print("\nWelcome to my number guessing game!")
    name = input("What's your name? ")

    best = 10000

    while True:
        score = round(name)
        if score < best:
            best = score

        print(f"Your best score is {best}.")
        if not playAgain():
            print("Goodbye!\n")
            return


main()