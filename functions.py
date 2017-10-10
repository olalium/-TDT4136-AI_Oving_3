import board_manipulation as b_m
from search_node import search_node

def manhattan_distance(start, end):
    sx, sy = start
    ex, ey = end
    return abs(ex - sx) + abs(ey - sy)

def generate_all_successors(board, node):
    new_nodes = {}

    temp_location = list(node.location)
    temp_location[1] += 1
    if b_m.get_map_value(board, temp_location) is '.' or b_m.get_map_value(board, temp_location) is 'B':
        temp_location = (temp_location[0], temp_location[1])
        new_node = search_node(G= node.g + 1, Parent=node)
        new_node.location = temp_location
        x = new_node.parent
        while x != None:
            new_node.state.append(x.location)
            x = x.parent
        new_nodes[temp_location] = new_node

    temp_location = list(node.location)
    temp_location[0] += 1

    if b_m.get_map_value(board, temp_location) is '.' or b_m.get_map_value(board, temp_location) is 'B':
        temp_location = (temp_location[0],temp_location[1])
        new_node = search_node(G= node.g + 1, Parent=node)
        new_node.location = temp_location
        x = new_node.parent
        while x != None:
            new_node.state.append(x.location)
            x = x.parent
        new_nodes[temp_location] = new_node

    temp_location = list(node.location)
    temp_location[1] -= 1
    if b_m.get_map_value(board, temp_location) is '.' or b_m.get_map_value(board, temp_location) is 'B':
        temp_location = (temp_location[0], temp_location[1])
        new_node = search_node(G= node.g + 1, Parent=node)
        new_node.location = temp_location
        x = new_node.parent
        while x != None:
            new_node.state.append(x.location)
            x = x.parent
        new_nodes[temp_location] = new_node

    temp_location = list(node.location)
    temp_location[0] -= 1
    if b_m.get_map_value(board, temp_location) is '.' or b_m.get_map_value(board, temp_location) is 'B':
        temp_location = (temp_location[0], temp_location[1])
        new_node = search_node(G= node.g + 1, Parent=node)
        new_node.location = temp_location
        x = new_node.parent
        while x != None:
            new_node.state.append(x.location)
            x = x.parent
        new_nodes[temp_location] = new_node

    return new_nodes

def attach_and_eval(child, parent, goal_location):
    child.parent = parent
    child.g = parent.g + 1
    child.h = manhattan_distance(child.location, goal_location)
    child.f = int(child.g) + int(child.h)
    return

def propagate_path_improvements(parent):
    for kid in parent.children:
        if (parent.g) + 1 < kid.g:
            kid.parent = parent
            kid.g = parent.g + 1
            kid.f = kid.g + kid.h
    return