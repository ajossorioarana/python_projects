# START OF PROGRAM

print('### Input Validation ###')
print()

while True: # Loops until user enters valid input
	age = input('Please enter your age: ')
	print()
	try:
		int(age)
		break
	except ValueError:
		print('Please, enter a valid number.')

input('Press any key to exit.')