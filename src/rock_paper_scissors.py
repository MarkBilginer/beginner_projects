from random import choice


def app() -> None:
	"""
	Application entry point.
	:return: None
	"""
	print("|=== Rock, Paper, Scissors Game ==|")
	game_status = int()
	is_exit = int()
	while is_exit != 1:
		play(game_status)
		is_exit = game_over()


def play(game_status: int) -> None:
	player_move = input(
		"Enter 'r' for Rock, 'p' for Paper and 's' for scissors: ")
	comp_move = choice(['r', 'p', 's'])
	game_status = is_win(player_move, comp_move)

	if game_status == 0:
		print(f"It's a tie! Player: {player_move}. Comp: {comp_move}")
	elif game_status == 1:
		print(f"Player wins! Player: {player_move}. Comp: {comp_move}")
	elif game_status == 2:
		print(f"Comp wins! Player: {player_move}. Comp: {comp_move}")


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


def game_over() -> int:
	is_game_over = input("Continue? Yes: 'y' or No: 'n' ")
	if is_game_over == 'n':
		return 1
	elif is_game_over == 'y':
		return 0
	else:
		print("Wrong input. Try again.")


if __name__ == "__main__":
	app()
	print("Exiting...")
