
file = open('input').read().splitlines()

test = open('test').read().splitlines()

def create_map(file):
    map = []
    row = 0
    for line in file:
        if '^' in line:
            for i in range(len(line)):
                if line[i] == '^':
                    start_row = row
                    start_col =  i
        map.append(list(line))
        row += 1
    return map, start_row, start_col

def patrol_route(file):
    map, start_row, start_col = create_map(file)
    m = len(map)
    n = len(map[0])
    map[start_row][start_col] = 'X'
    curRow, curCol = start_row, start_col
    dir = 0
    x = [-1, 0, 1,  0]
    y = [ 0, 1, 0, -1]

    distinct_pos = 1

    while True:
        next_row, next_col = curRow + x[dir], curCol + y[dir]

        if not (0 <= next_row < m and 0 <= next_col < n):
            break

        if map[next_row][next_col] == '#':
            dir = (dir + 1) % 4
        else:
            if map[next_row][next_col] == '.':
                map[next_row][next_col] = 'X'
                distinct_pos += 1

            curRow, curCol = next_row, next_col

    return distinct_pos


print('Answer - Part 1:', patrol_route(file))




