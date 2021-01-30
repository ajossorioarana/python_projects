import random

def roll(num_dice, max_roll):
	total_roll = 0
	for i in range(num_dice): # For total number of dice, roll and sum
		roll = random.randint(0, max_roll)
		total_roll += roll
	print('#'*30)
	print('You roll {0} d{1} and obtained a {2}.'.format(
		  str(num_dice), str(max_roll), str(total_roll)))


def input_validation(msg_input, msg_error):
	while True: # Loops until user enters valid input
		value = input(msg_input)
		print()
		try:
			int(value)
			break
		except ValueError:
			print(msg_error)

	return int(value)

num_dice_msg_input = 'Enter total number of dices to roll: '
max_roll_msg_input = 'Enter max value of dice: '
msg_error = 'Please, enter a valid number.'

# START OF PROGRAM #
print('### DICE SIMULATOR ###')
print()

num_dice = input_validation(num_dice_msg_input, msg_error)
max_roll = input_validation(max_roll_msg_input, msg_error)

roll(num_dice, max_roll)

input('Press any key to exit.')