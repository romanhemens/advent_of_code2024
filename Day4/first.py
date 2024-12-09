
file = open('input').read().splitlines()

def create_grid(file):
    word_search = []
    for line in file:
        word_search.append(list(line))

    return word_search

def word_search(grid, row, col, word):
    m = len(grid)
    n = len(grid[0])

    if grid[row][col] != word[0]:
        return False

    lenword = len(word)

    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1,  0,  1,-1, 1,-1, 0, 1]

    count = 0

    for dir in range(8):
        currentRow, currentCol = row + x[dir], col + y[dir]
        k = 1

        while k < lenword:

            if currentRow < 0 or currentRow >= m or currentCol < 0 or currentCol >= n:
                break

            if grid[currentRow][currentCol] != word[k]:
                break

            currentRow += x[dir]
            currentCol += y[dir]
            k += 1

        if k == lenword:
            count += 1

    return count

def actual_search(grid, word):
    m = len(grid)
    n = len(grid[0])

    total_count = 0

    for i in range(m):
        for j in range(n):
            total_count += word_search(grid, i, j, word)

    return total_count

ans = actual_search(create_grid(file), "XMAS")
print('XMAS occurences:', ans)

