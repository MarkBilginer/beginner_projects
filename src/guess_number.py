
from random import randint

print("Welcome to the boring guess the number game!")

guess = int(input("Your guess: "))

number = randint(0, 10)

if guess == number:
	print("You guessed the computer generated number correctly!")
else:
	print("You failed!")