
def generate_board(input):
    f = open('boards/board-1-'+input+'.txt', 'r')
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
    y_val = -1
    for y in map_array:
        y_val += 1
        x_val = -1
        for x in y:
            x_val += 1
            if (x_val == l[0]) and (y_val == l[1]):
                return map_array[y_val][x_val]

def success(board, x):
    solution_board = board
    for item in x.state:
        solution_board[item[1]][item[0]] = 'o'
    f = open('last_solution.txt', 'w')
    for line in solution_board:
        print(''.join(line) + '\n')
        f.write(''.join(line) + '\n')
    f.close()
    print('last_solution.tx is available in directory')