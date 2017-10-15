import board_manipulation as b_m
from search_node import search_node

# manhattan distance is distance between two points on a grid based on strictly horizontal and/or vertical path
def manhattan_distance(start, end):

    sx, sy = start
    ex, ey = end

    return abs(ex - sx) + abs(ey - sy)

# generates and returns all children nodes of the node if it does not collide with a wall
def generate_all_successors(board, node):

    new_nodes = {}
    cell_categories = ["w", "m", "f", "g", "r", ".", "B"]

    temp_location = list(node.location)

    if temp_location[1] < (len(board)-1): # checks if this is edge of map

        temp_location[1] += 1   # y value +1 (goes up)

        m_v = b_m.get_map_value(board, temp_location)

        if m_v in cell_categories: #checks if map value is not a wall

            #creates a node
            temp_location = (temp_location[0], temp_location[1])
            new_node = search_node(G= node.g , Parent=node)
            new_node.g += b_m.calculate_g(board, new_node)
            new_node.location = temp_location
            x = new_node.parent

            #creates the nodes "state", what path it takes from start node
            while x != None:

                new_node.state.append(x.location)
                x = x.parent

            new_nodes[temp_location] = new_node

    #repeats previous actions on left, right, down movement

    temp_location = list(node.location)

    if temp_location[0] < (len(board[0])-1):

        temp_location[0] += 1

        m_v = b_m.get_map_value(board, temp_location)

        if m_v in cell_categories:

            temp_location = (temp_location[0],temp_location[1])
            new_node = search_node(G= node.g, Parent=node)
            new_node.g += b_m.calculate_g(board, new_node)
            new_node.location = temp_location
            x = new_node.parent

            while x != None:

                new_node.state.append(x.location)
                x = x.parent

            new_nodes[temp_location] = new_node

    temp_location = list(node.location)

    if temp_location[1]> 0:

        temp_location[1] -= 1

        m_v = b_m.get_map_value(board, temp_location)

        if m_v in cell_categories:

            temp_location = (temp_location[0], temp_location[1])
            new_node = search_node(G= node.g, Parent=node)
            new_node.g += b_m.calculate_g(board, new_node)
            new_node.location = temp_location
            x = new_node.parent

            while x != None:

                new_node.state.append(x.location)
                x = x.parent

            new_nodes[temp_location] = new_node

    temp_location = list(node.location)

    if temp_location[0] > 0:

        temp_location[0] -= 1

        m_v = b_m.get_map_value(board, temp_location)

        if m_v in cell_categories:

            temp_location = (temp_location[0], temp_location[1])
            new_node = search_node(G= node.g, Parent=node)
            new_node.g += b_m.calculate_g(board, new_node)
            new_node.location = temp_location
            x = new_node.parent

            while x != None:

                new_node.state.append(x.location)
                x = x.parent

            new_nodes[temp_location] = new_node

    return new_nodes

# attaches child to a node that is now considered its best parent so far
def attach_and_eval(map_array, child, parent, goal_location):

    child.parent = parent
    child.g = parent.g + b_m.calculate_g(map_array, child)
    child.h = manhattan_distance(child.location, goal_location)
    child.f = int(child.g) + int(child.h)

# recurses through the children of a parent and other descendants if the new parent.g value makes the path better
def propagate_path_improvements(map_array, parent):

    for kid in parent.children:

        if ((parent.g) + b_m.calculate_g(map_array, kid)) < kid.g:

            kid.parent = parent
            kid.g = parent.g + b_m.calculate_g(map_array, kid)
            kid.f = kid.g + kid.h