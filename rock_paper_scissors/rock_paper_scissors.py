import sys, random


def game_select():
	while True:	
		print('Select type of game:')
		print('Player vs AI ..... [1]')
		print('AI vs AI ......... [2]')
		print('Exit ............. [q]')
		menu_choice = input() 	# TO-DO: Disable CAPS

		if menu_choice == 'q':
			sys.exit()	# Exits game if 'q' selected
		elif menu_choice == '1' or menu_choice == '2':
			break	# Until player selects one of the options, the loop continues
		print('Please, select one of the options: (1), (2), or (q).')

	if menu_choice == '1':
		main_vs_ai()
	elif menu_choice == '2':
		main_ai_vs_ai() 


def main_vs_ai():
	# Initializes variables of game results
	wins = 0
	draws = 0
	losses = 0

	while True:
		print()
		print('{0} wins, {1} draws, {2} losses.'.format(wins, draws, losses))

		player_results = player_turn(wins, draws, losses)
		ai_results = ai_turn()
	
		wins, draws, losses = turn_eval(player_results, ai_results, wins, draws, losses)	


def main_ai_vs_ai():
	# Initializes variables of game results
	wins = 0
	draws = 0
	losses = 0

	total_rolls = int(input('Number of rolls: ')) 	# TO-DO: Exception handling for integer

	for i in range(total_rolls):
		print()
		print('{0} wins, {1} draws, {2} losses.'.format(wins, draws, losses))

		ai_results_p1 = ai_turn()
		ai_results_p2 = ai_turn()
	
		wins, draws, losses = turn_eval(ai_results_p1, ai_results_p2, wins, draws, losses)

	input('Press any key to exit')

def player_turn(wins, draws, losses):
	while True:	
		print('Select your move: (r)ock, (p)aper, (s)cissors. Or press (q) to exit game.')
		player_move = input() 	# TO-DO: Disable CAPS
		print()

		if player_move == 'q':
			sys.exit()	# Exits game if 'q' selected
		elif player_move == 'r' or player_move == 'p' or player_move == 's':
			break	# Until player selects one of the options, the loop continues
		print('Please, select one of the options: (r), (p), (s) or (q).')

	# Prints player move
	if player_move == 'r':
		print('ROCK vs...')
	elif player_move == 'p':
		print('PAPER vs...')
	elif player_move == 's':
		print('SCISSORS vs...')

	return player_move


def ai_turn():
	ai_num = random.randint(1, 3)
	if ai_num == 1:
		ai_move = 'r'
		print('ROCK!')
	elif ai_num == 2:
		ai_move = 'p'
		print('PAPER!')
	elif ai_num == 3:
		ai_move = 's'
		print('SCISSORS!')

	return ai_move


def turn_eval(player_move, ai_move, wins, draws, losses):
	# Comparison and results
	if player_move == ai_move:
		draws += 1
		print('It\'s a draw!')
	elif player_move == 'r':
		if ai_move == 'p':
			losses += 1
			print('You lose!')
		elif ai_move == 's':
			print('You win!')
			wins += 1
	elif player_move == 'p':
		if ai_move == 's':
			losses += 1
			print('You lose!')
		elif ai_move == 'r':
			print('You win!')
			wins += 1
	elif player_move == 's':
		if ai_move == 'r':
			losses += 1
			print('You lose!')
		elif ai_move == 'p':
			print('You win!')
			wins += 1

	return wins, draws , losses


print('ROCK, PAPERS, SCISSORS')
print('')
game_select()