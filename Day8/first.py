from itertools import combinations

file = open('input').read().splitlines()
test = open('test').read().splitlines()

def create_grid(file):
    grid = []
    for line in file:
        grid.append(list(line))

    return grid

def find_frequencies(grid):
    m = len(grid)
    n = len(grid[0])

    antenna_dict = {}

    for i in range(m):
        for j in range(n):
            if grid[i][j] != '.':
                if grid[i][j] not in antenna_dict:
                    antenna_dict[grid[i][j]] = [(i, j)]
                else:
                    antenna_dict[grid[i][j]].append((i, j))

    return antenna_dict

def find_unique_antinodes(antennas, grid):
    m = len(grid)
    n = len(grid[0])
    unique_antinodes = set()

    for ant in antennas:

        pairs = combinations(antennas[ant], 2)
        for pair in pairs:

            dist_x =  pair[1][0] - pair[0][0]
            dist_y =  pair[1][1] - pair[0][1]

            pos_antidode1 = (pair[0][0] - dist_x, pair[0][1] - dist_y)
            pos_antidode2 = (pair[1][0] + dist_x, pair[1][1] + dist_y)

            if pos_antidode1 not in unique_antinodes and 0 <= pos_antidode1[0] < m and 0 <= pos_antidode1[1] < n:
                unique_antinodes.add(pos_antidode1)
            if pos_antidode2 not in unique_antinodes and 0 <= pos_antidode2[0] < m and 0 <= pos_antidode2[1] < n:
                unique_antinodes.add(pos_antidode2)

    return unique_antinodes

def calculate(file):
    grid = create_grid(file)
    antenna_dict = find_frequencies(grid)
    unique_antinodes = find_unique_antinodes(antenna_dict, grid)

    return len(unique_antinodes)

print('Answer - Part 1:', calculate(file))