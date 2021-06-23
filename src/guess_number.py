from random import randint


def guess(x: int) -> None:
	"""Simple Game where the user guesses a pseudo-randomly generated
	number. The integer x initializes the guessing range.
	"""
	number = randint(1, x)
	user_input = 0
	while user_input != number:
		user_input = int(input(f"Your guess between 1 and {x}: "))
		if user_input < number:
			print("Number too low. Try again...")
		elif user_input > number:
			print("Number too high. Try again...")
	else:
		print(f"You have guessed the random number correctly: {number}!")

def fill_list(x: int, generic_list: list) -> None:
	"""Fills the list, generic_list, sequentially with integers in the
	range 1...x.
	"""
	for i in range(1, x + 1):
		generic_list.append(i)


def no_repeat_random(x: int, filled_list: list) -> int:
	"""Randomly identifies index of parameter filled_list. Pops the
	chosen element from the list. This way the pseudo-randomly chosen
	element will not be repeated.
	"""
	length = len(filled_list)
	if length != 0:
		index = randint(0, length - 1)
		result = filled_list.pop(index)
		return result
	return 0


def computer_guess(x: int) -> None:
	"""Simple Game where the computer guesses a user provided number.
	The integer x initializes the guessing range.
	"""
	guess_list = list()
	user_input = int(input(f"Specify the number the computer should guess: "))
	fill_list(x, guess_list)
	guess = 0
	while guess != user_input:
		guess = no_repeat_random(x, guess_list)
		print(f"The computer guesses: {guess}")
	else:
		print(f"The computer guesses the number correctly: {guess}")


if __name__ == "__main__":
	print("Welcome to the boring guess the number game!")
	# guess(10)
	computer_guess(10)
	print("Exiting...")
