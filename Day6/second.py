from Day6.first import create_map

file = open('input').read().splitlines()

test = open('test').read().splitlines()

def check_patrol_for_loop(map, start_row, start_col):
    m = len(map)
    n = len(map[0])
    dir = 0
    x = [-1, 0, 1, 0]
    y = [0, 1, 0, -1]

    curRow, curCol = start_row, start_col
    visited = set()

    while True:

        state = (curRow, curCol, dir)
        if state in visited:
            return True
        visited.add(state)

        next_row, next_col = curRow + x[dir], curCol + y[dir]
        if not (0 <= next_row < m and 0 <= next_col < n):
            return False

        if map[next_row][next_col] == '#':
            dir = (dir + 1) % 4
        else:
            curRow, curCol = next_row, next_col

def find_obstructions_pos(file):
    map, start_row, start_col = create_map(file)
    m = len(map)
    n = len(map[0])
    possible_pos = []

    for row in range(m):
        for col in range(n):
            if map[row][col] != '.' or (row == start_row and col == start_col):
                continue

            map[row][col] = '#'

            if check_patrol_for_loop(map, start_row, start_col):
                possible_pos.append((row, col))

            map[row][col] = '.'

    return len(possible_pos)


print('Answer - Part 2: ', find_obstructions_pos(file))