
def load_input(filepath: str) -> (list, list):
    warehouse = []
    moves = []
    movement = False
    row = 0
    with open(filepath) as file:
        for line in file:
            if line.strip():
                strs = []
                col = 0
                for char in line.strip():
                    if char == '@':
                        robot = [row, col]
                    strs.append(char)
                    col += 1

                if not movement:
                    warehouse.append(strs)
                else:
                    moves += strs
            else:
                movement = True
            row += 1
    return warehouse, moves, robot

def predict_next_move(robot: [int, int], warehouse: list, move = str) -> (int, int, list):

    pos_moves = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
    dir = pos_moves[move]
    next_pos = [robot[0] + dir[0], robot[1] + dir[1]]

    if warehouse[next_pos[0]][next_pos[1]] == '#':
        return robot, warehouse

    elif warehouse[next_pos[0]][next_pos[1]] == 'O':
        def pushing_boxes(next_pos, warehouse, dir):
            new_pos = [next_pos[0] + dir[0], next_pos[1] + dir[1]]
            if warehouse[new_pos[0]][new_pos[1]] == '#':
                return warehouse
            elif warehouse[new_pos[0]][new_pos[1]] == '.':
                warehouse[new_pos[0]][new_pos[1]] = 'O'
                warehouse[next_pos[0]][next_pos[1]] = '.'
                return warehouse
            else:
                warehouse = pushing_boxes(new_pos, warehouse, dir)
                if warehouse[new_pos[0]][new_pos[1]] == '.':
                    warehouse[new_pos[0]][new_pos[1]] = 'O'
                    warehouse[next_pos[0]][next_pos[1]] = '.'
            return warehouse
        warehouse = pushing_boxes(next_pos, warehouse, dir)

        if warehouse[next_pos[0]][next_pos[1]] == '.':
            warehouse[robot[0]][robot[1]] = '.'
            warehouse[next_pos[0]][next_pos[1]] = '@'
            return next_pos, warehouse
        return robot, warehouse
    elif warehouse[next_pos[0]][next_pos[1]] == '.':
        warehouse[robot[0]][robot[1]] = '.'
        warehouse[next_pos[0]][next_pos[1]] = '@'
        return next_pos, warehouse

def solve(warehouse: list, moves = list, robot = list) -> int:
    m = len(warehouse)
    n = len(warehouse[0])
    for move in moves:
        robot, warehouse = predict_next_move(robot, warehouse, move)

    gps_sum = 0
    for i in range(m):
        for j in range(n):
            if warehouse[i][j] == 'O':
                gps = 100*i + j
                gps_sum += gps

    return gps_sum

if __name__ == '__main__':
    warehouse, moves, robot = load_input('input')
    gps_sum = solve(warehouse, moves, robot)
    print(f'Part 1: {gps_sum}')



