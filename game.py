"""A number-guessing game."""

# Put your code here
from random import randint

print("Welcome to my number guessing game!")
name = input("What's your name? ")

number = randint(1, 100)
print(f"Ok, {name}, I'm thinking of a number between 1 and 100. Can you guess it?")

count = 0

while True:
    guess = int(input("What's my number? "))
    count += 1
    if guess == number:
        print (f"You guessed my number in {count} tries, {name}!")
        break
    elif guess < number:
        print ("Too low.")
    else:
        print ("Too high.")