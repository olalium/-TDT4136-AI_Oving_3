import board_manipulation as b_m
from functions import manhattan_distance as m_h
from functions import generate_all_successors as g_a_s
from functions import attach_and_eval as a_a_e
from functions import propagate_path_improvements as p_p_i
import operator
from search_node import search_node

def main():
    board = b_m.generate_board(input('board 1-4:'))
    goal_location = b_m.locate(board, 'B')

    closed = {}
    open_d = {}
    open_stack = []
    existing = {}

    n0 = search_node(G = 0, Parent = None)
    n0.location = b_m.locate(board, 'A')
    n0.h = m_h(n0.location, goal_location)
    n0.f = n0.h + n0.g

    existing[n0.location] = n0
    open_d[n0.location] = n0
    open_stack.append(n0.location)
    n0.status = 'open_d'
    solution = None
    depth = 0
    while (solution is None):
        if (len(open_d.values()) == 0):
            print('fail')
            return 'fail'
        x = open_d.pop(open_stack[-1:][0])
        open_stack.pop()
        closed[x.location] = x
        x.status = 'closed'

        if (m_h(x.location, goal_location)) == 0:
            print('success', depth, x.state)
            return b_m.success(board, x)
        depth += 1
        succssessors = g_a_s(board, x)

        for S in succssessors:
            if (S in existing.keys()):
                succssessors[S].status = 'closed'
            else:
                existing[S] = succssessors[S]

            x.children.append(succssessors[S])
            if succssessors[S].status is not 'open_d' and succssessors[S].status is not 'closed':
                a_a_e(succssessors[S], x, goal_location)
                open_d[S] = succssessors[S]
                open_stack.append(S)
                new_open = []
                for key in sorted(open_d.values(), key=operator.attrgetter('f'), reverse = True):
                    new_open.append(key.location)
                open_stack = new_open

            elif (x.g + 1) < succssessors[S].g:
                a_a_e(succssessors[S], x, goal_location)
                if S in closed:
                    p_p_i(succssessors[S])

if __name__ == '__main__':
    main()