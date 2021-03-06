"""A number-guessing game."""

# Put your code here
from random import randint

def round(name, mini, maxi, guesses):
    number = randint(mini, maxi)
    print(f"\nOk, {name}, I'm thinking of a number between {mini} and {maxi}. You have {guesses} guesses. Can you guess my number?")
    count = 0

    while count < guesses:
        guess = generateGuess(mini, maxi)
        count += 1
        if evaluateGuess(number, guess):
            print (f"You guessed my number in {count} tries, {name}!")
            return count

    print(f"Oh no! You're out of guesses. My number was {number}. Better luck next time.\n")
    return 10000
        
def generateGuess(mini, maxi):
    while True:
        guess = input("What's my number? ")
        try:
            guess = int(guess)
        except ValueError:
            print("Please guess an integer.")
            continue
        if guess < mini or guess > maxi:
            print("Your guess is out of range. Pick a number between 1 and 100, please.")
            continue
        break
    return guess

def evaluateGuess(number, guess):
    if guess == number:
        return True
    elif guess < number:
        print ("Too low.")
    else:
        print ("Too high.")
    return False

def setParameters():
    print("")
    while True:
        mini = input("What would you like the bottom of the range to be? ")
        try:
            mini = int(mini)
        except ValueError:
            print ("Please choose an integer.")
            continue
        break

    while True:
        maxi = input("What would you like the top of the range to be? ")
        try:
            maxi = int(maxi)
        except ValueError:
            print ("Please choose an integer.")
            continue
        if maxi <= mini:
            print("The top of your range needs to be higher than the bottom.")
            continue
        break

    while True:
        guesses = input("How many guesses would you like? ")
        try:
            guesses = int(guesses)
        except ValueError:
            print ("Please choose an integer.")
            continue
        if guesses <= 0:
            print ("Please choose a positive integer.")
            continue
        break

    return [mini, maxi, guesses]

def computerTurn(mini, maxi, guesses):
    print(f"\nMy turn! Think of a number between {mini} and {maxi} for me to guess in {guesses} guesses.")
    input("Hit enter when you've got your number. ")
    print("")

    count = 0

    while count < guesses:
        guess = int((mini+maxi)/2)
        count += 1

        while True:
            feedback = input(f"Is your number {guess}? [a] Yes, [b] Too high, [c] Too low. ")
            if feedback == 'a':
                print(f"Hooray! I got your number in {count} guesses.")
                return count
            elif feedback == 'b':
                maxi = guess - 1
                break
            elif feedback == 'c':
                mini = guess + 1
                break
            else:
                print ("Sorry, I didn't get that. Please type either a, b, or c?")

    print ("Aw shucks. I ran out of guesses.\n")
    return 10000

def playAgain():
    while True:
        again = input("Would you like to keep playing? [y/n] ")
        if again == "n":
            return False
        elif again == "y":
            return True
        else:
            print("Please respond with 'y' or 'n' only.")

def main():
    print("\nWelcome to my number guessing game!")
    name = input("What's your name? ")
    param = setParameters()

    userBest = 10000
    computerBest = 10000

    while True:
        score = round(name, param[0], param[1], param[2])
        if score < userBest:
            userBest = score

        if userBest != 10000:
            print(f"\nYour best score is {userBest}.")

        score = computerTurn(param[0], param[1], param[2])
        if score < computerBest:
            computerBest = score

        if computerBest != 10000:
            print(f"\nMy best score is {computerBest}.")

        if not playAgain():
            print("Goodbye!\n")
            return

main()


