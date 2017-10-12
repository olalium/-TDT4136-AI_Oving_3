
def generate_board(input):

    f = open('boards/board-'+input+'.txt', 'r')
    map_array = []

    for line in f:

        map_array.append(list(line.strip()))

    f.close()

    return map_array

def locate(map_array, node):

    y_val = -1

    for y in map_array:

        y_val += 1
        x_val = -1

        for x in y:

            x_val += 1

            if x is node:

                return x_val, y_val

def get_map_value(map_array, l):

    x_val = l[0]
    y_val = l[1]

    return map_array[y_val][x_val]

def success(board, x, open_d, closed):

    solution_board = board
    x.state.pop()

    for item in open_d.values():

        solution_board[item.location[1]][item.location[0]] = 'X'

    for item in closed.values():

        solution_board[item.location[1]][item.location[0]] = '-'

    for item in x.state:

        solution_board[item[1]][item[0]] = '+'

    f = open('last_solution.txt', 'w')

    for line in solution_board:

        print(''.join(line) + '\n')
        f.write(''.join(line) + '\n')

    f.close()

    print('last_solution.tx is available in directory')

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

