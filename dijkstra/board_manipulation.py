from PIL import Image
from numpy import uint8
from numpy import zeros
import copy

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

    old_board = copy.deepcopy(board)

    solution_board = board

    x.state.pop() # removes node from path so A and B show on map

    for item in open_d.values():
        if get_map_value(board, item.location) != 'A' and get_map_value(board, item.location) != 'B':
            solution_board[item.location[1]][item.location[0]] = 'X'

    for item in closed.values():
        if get_map_value(board, item.location) != 'A' and get_map_value(board, item.location) != 'B':
            solution_board[item.location[1]][item.location[0]] = '-'

    for item in x.state:

        solution_board[item[1]][item[0]] = '+'

    success_image(old_board, solution_board)

    f = open('last_solution.txt', 'w')

    for line in solution_board:

        print(''.join(line) + '\n')
        f.write(''.join(line) + '\n')

    f.close()

    print('last_solution.txt is available in directory, "+" = path , "-" = closed and "X" = open'
          '\nfinal_solution.png is available in directory, purple = closed, light blue = open, red = path')

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

#creates image using PIL of solution board, pretty complicated and ugly, but does the trick
def success_image(board, solution_board):

    #task1 = 20x7
    #task2 = 40x10

    cons = 20

    legen_d = {'.':[255, 255, 255], '#':[10,10,10], 'w':[0,0,200],
               'm':[128,128,128],'f':[0,128,0],'g':[0,200,0],
               'r':[153,50,0], 'A':[255,0,0], 'B':[255,0,0]}

    solution_d = {'+':[255,0,0],'-':[128,0,255],'X':[0,255,255]}

    height_board = len(board)
    width_board = len(board[0])

    width_pic = width_board*cons
    height_pic = height_board*cons

    pic_array = zeros((height_pic, width_pic, 3), dtype=uint8)

    y_val = -1
    for y in solution_board:
        y_val += 1
        x_val = -1
        for x in y:
            x_val += 1
            if x in legen_d.keys():
                rgb_val = legen_d[x]
                i_val = x_val*cons
                for i in range(i_val+1, i_val+cons-1):
                    j_val = y_val * cons
                    for j in range(j_val+1, j_val+cons-1):
                        pic_array[j][i] = rgb_val
            elif x in solution_d.keys():
                rgb_val = legen_d[board[y_val][x_val]]
                i_val = x_val * cons
                for i in range(i_val + 1, i_val + cons - 1):
                    j_val = y_val * cons
                    for j in range(j_val + 1, j_val + cons - 1):
                        pic_array[j][i] = rgb_val
                rgb_val = solution_d[x]
                i_val = x_val * cons
                for i in range(i_val + 5, i_val + 10):
                    j_val = y_val * cons
                    for j in range(j_val + 5, j_val + 10):
                        pic_array[j][i] = rgb_val


    img = Image.fromarray(pic_array, 'RGB')
    img.show()
    img.save('final_solution.png')