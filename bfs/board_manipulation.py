
# generates board to a map_ array on format: [['.','.']['.','.']]
def generate_board(input):

    f = open('../boards/board-'+input+'.txt', 'r')
    map_array = []

    for line in f:

        map_array.append(list(line.strip()))

    f.close()

    return map_array

# locates a certain unique-in-map_array-value and returns x & y values
def locate(map_array, node):

    y_val = -1

    for y in map_array:

        y_val += 1
        x_val = -1

        for x in y:

            x_val += 1

            if x is node:

                return x_val, y_val

# returns the value in map array location 'l'
def get_map_value(map_array, l):

    x_val = l[0]
    y_val = l[1]

    return map_array[y_val][x_val]

# returns the original map_array board with different values representing opened, closed and optimal solution nodes
def success(board, x, open_d, closed):

    solution_board = board
    x.state.pop()

    for item in open_d.values():
        if get_map_value(board, item.location) != 'A' and get_map_value(board, item.location) != 'B':
            solution_board[item.location[1]][item.location[0]] = 'X'

    for item in closed.values():
        if get_map_value(board, item.location) != 'A' and get_map_value(board, item.location) != 'B':
            solution_board[item.location[1]][item.location[0]] = '-'

    for item in x.state:

        solution_board[item[1]][item[0]] = '+'

    f = open('last_solution.txt', 'w')

    for line in solution_board:

        print(''.join(line) + '\n')
        f.write(''.join(line) + '\n')

    f.close()

    print('last_solution.txt is available in directory, "+" = path , "-" = closed and "X" = open')

# calculates the g value of a node on a map_array, values from list in task
def calculate_g(map_array, new_node):

    map_value = get_map_value(map_array, new_node.location)

    if map_value == "w":
        value = 100
    elif map_value == "m":
        value = 50
    elif map_value == "f":
        value = 10
    elif map_value == "g":
        value = 5
    elif map_value == "r":
        value = 1
    else:
        value = 1
    return value

