import sys, random

# Initializes variables of game results
wins = 0
draws = 0
losses = 0

print('ROCK, PAPERS, SCISSORS')

while True: 	# Main game loop
	print()
	print('{0} wins, {1} draws, {2} losses.'.format(wins, draws, losses))
	while True:	
		print('Select your move: (r)ock, (p)aper, (s)cissors. Or press (q) to exit game.')
		player_move = input() 	# TO-DO: Disable CAPS
		print()

		if player_move == 'q':
			sys.exit()	# Exits game if 'q' selected
		elif player_move == 'r' or player_move == 'p' or player_move == 's':
			break	# Until player selects one of the options, the loop continues
		print('Please, select one of the options: (r), (p), (s) or (q).')

	# Prints player mover
	if player_move == 'r':
		print('ROCK vs...')
	elif player_move == 'p':
		print('PAPER vs...')
	elif player_move == 's':
		print('SCISSORS vs...')

	# AI turn
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

