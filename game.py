"""A number-guessing game."""

# Put your code here
from random import randint

print("Welcome to my number guessing game!")
name = input("What's your name? ")

number = randint(1, 100)
print("I'm thinking of a number between 1 and 100. Can you guess it?")
print(number)