def collatz(number):
	if number % 2 == 0:
		return (number // 2)
	else:
		return (3 * number + 1)


# START OF PROGRAM
print('### COLLATZ SEQUENCE ###')
print()
number = int(input('Select a natural number to show the Collatz sequence for it: '))

# Main loop
while number != 1:
	number = collatz(number)
	print(number)

input('Press any key to exit.')