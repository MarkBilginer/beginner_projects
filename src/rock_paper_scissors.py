from random import choice


def app() -> None:
	"""
	Application entry point.
	:return: None
	"""
	print("|=== Rock, Paper, Scissors Game ==|")
	game_status = int()
	is_exit = int()
	highscore = [0, 0]

	while is_exit != 1:
		game_status = play_round()
		update_highscore(game_status, highscore)
		is_exit = game_over()
	print_highscore(highscore)


def play_round() -> int:
	"""
	Executes one round of the game.
	:return: result of the round 0 for tie, 1 for player win or 2 for
	computer win
	"""
	player_move = input(
		"Enter 'r' for Rock, 'p' for Paper and 's' for scissors: ")
	comp_move = choice(['r', 'p', 's'])
	game_status = is_win(player_move, comp_move)

	if game_status == 0:
		print(f"It's a tie! Player: {player_move}. Comp: {comp_move}")
		return 0
	elif game_status == 1:
		print(f"Player wins! Player: {player_move}. Comp: {comp_move}")
		return 1
	elif game_status == 2:
		print(f"Comp wins! Player: {player_move}. Comp: {comp_move}")
		return 2


def is_win(player_move: str, comp_move: str) -> int:
	"""
	Checks game result.

	logic for win:
	paper beats rock.
	rock beats scissors.
	scissors beats paper.
	if both moves are equal game is a tie.

	:param player_move: player move in length one lowercase string
	:param comp_move: computer move in length one lowercase string
	:return: 1 if player won, 2 if computer won, 0 if it is a tie
	"""

	if player_move == comp_move:
		return 0
	elif player_move == 'p' and comp_move == 'r':
		return 1
	elif player_move == 'r' and comp_move == 's':
		return 1
	elif player_move == 's' and comp_move == 'p':
		return 1
	else:
		return 2


def update_highscore(game_status: int, highscore: list) -> None:
	"""
	Updates the highscore value for both players after each round.
	:param game_status: variable containing integer who won the game
	:param highscore: list containing the highscore
	:return:
	"""
	if game_status == 1:
		highscore[0] += 1
	elif game_status == 2:
		highscore[1] += 1


def print_highscore(highscore: list) -> None:
	"""
	Prints the highscore saved in a list.
	:param highscore: list with index 0 for player 1 and index 1 for comp
	:return: None
	"""
	print("|== Highscore: ==|")
	print(f"Player 1: {highscore[0]}")
	print(f"Player 2: {highscore[1]}")


def game_over() -> int:
	"""
	Gets input from user whether s_he wants to continue playing or not.
	:return: 1 for game is over, 0 for game is not over
	"""
	is_game_over = input("Continue? Yes: 'y' or No: 'n': ")
	if is_game_over == 'n':
		return 1
	elif is_game_over == 'y':
		return 0
	else:
		print("Wrong input. Try again.")


if __name__ == "__main__":
	app()
	print("Exiting...")
