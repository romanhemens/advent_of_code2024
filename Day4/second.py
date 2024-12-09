from Day4.first import create_grid

file = open('input').read().splitlines()

def word_search(grid, start, middle, end):

    if grid[1][1] != middle:
        return False

    count = 0

    if (grid[0][0] == start and grid[2][2] == end) or (grid[2][2] == start and grid[0][0] == end):
        if (grid[2][0] == start and grid[0][2] == end) or (grid[2][0] == end and grid[0][2] == start):
            count += 1

    return count

def actual_search(grid, start, middle, end):
    m = len(grid)
    n = len(grid[0])
    total_count = 0

    for i in range(m):
        if i+3 <= m:
            for j in range(n):
                if j+3 <= n:
                    window = [grid[i][j:j+3], grid[i+1][j:j+3], grid[i+2][j:j+3]]
                    total_count += word_search(window, start, middle, end)

    return total_count

count = actual_search(create_grid(file), 'M', 'A', 'S')
print('X-MAS count:', count)

