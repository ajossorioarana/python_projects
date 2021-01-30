import copy, random, time

width = 60
height = 20

# Fills board with '#'
next_board = [['#' for y in range(height)] for x in range(width)]

# Loops through all cells and if randint = 0, erases '#'
for x in range(width):
    for y in range(height):
        alive = random.randint(0, 1)
        if alive is 0:
            next_board[x][y] = ' '

# Main program loop
while True:
    print('\n\n\n\n\n')
    current_board = copy.deepcopy(next_board) # Make a copy of previous board

    # Prints current board
    for y in range(height):
        for x in range(width):
            print(current_board[x][y], end='')
        print()

    # Calculates next board based on current coordinates
    for y in range(height):
        for x in range(width):
            # Get neighboring coordinates
            left_coordinates = (x - 1) % width
            right_coordinates = (x + 1) % width
            above_coordinates = (y - 1) % height
            below_coordinates = (y + 1) % height

            alive_neighbors = 0


            # Checks for living neighboors
            if current_board[left_coordinates][above_coordinates] == '#':
                alive_neighbors += 1
            if current_board[x][above_coordinates] == '#':
                alive_neighbors += 1
            if current_board[right_coordinates][above_coordinates] == '#':
                alive_neighbors += 1
            if current_board[left_coordinates][y] == '#':
                alive_neighbors += 1
            if current_board[right_coordinates][y] == '#':
                alive_neighbors += 1
            if current_board[left_coordinates][below_coordinates] == '#':
                alive_neighbors += 1
            if current_board[x][below_coordinates] == '#':
                alive_neighbors += 1
            if current_board[right_coordinates][below_coordinates] == '#':
                alive_neighbors += 1


            # Applies new configuration of dead-alive based on rules.
            if current_board[x][y] == '#' and (alive_neighbors == 2 or alive_neighbors == 3):
                next_board[x][y] = '#'
            elif current_board[x][y] == ' ' and alive_neighbors == 3:
                next_board[x][y] = '#'
            else:
                next_board[x][y] = ' '

    time.sleep(1) # Adds a 1 second pause for flickering