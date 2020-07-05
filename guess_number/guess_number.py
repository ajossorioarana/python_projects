from random import randint


def game(first_case, last_case, max_chances):
	# Assigns a value to be guessed, taken into account limits imported in the function.
	answer = randint(first_case, last_case + 1)
	chance_left = max_chances

	print('Number between {0} and {1} has been selected. \n'.format(str(first_case), str(last_case)))

	while chance_left > 0:
		guess = input('You have {0} chances left. Make a guess: '.format(str(chance_left)))

		# TO-DO: Verify that user input is valid

		if int(guess) == answer:
			guesses_taken = max_chances - chance_left + 1
			print('You won! You achieved the result in {0} guesses. \n'.format(str(guesses_taken)))
			break
		elif int(guess) > answer:
			print('The answer is lower than {0}. \n'.format(str(guess)))
			if chance_left == 1:
				defeat_msg(answer)
		else:
			print('The answer is higher than {0}. \n'.format(str(guess)))
			if chance_left == 1:
				defeat_msg(answer)

		chance_left -= 1

	print('Thanks for playing "Guess the Number"! \n')

def defeat_msg(answer):
	print('You lost, you run out of chances! The right answer was {0}.'.format(str(answer)))
	print()



# Start of main loop

# Defining variables
first_case = 1
last_case = 20
max_chances = 4

# Running the game
game(first_case, last_case, max_chances)

input('Press a key to exit.')