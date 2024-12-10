from collections import deque
from typing import List

def load_input(file_path: str) -> List[List[int]]:
    with open(file_path) as f:
        map = []
        for line in f:
            nums = [int(char) for char in line.strip()]
            map.append(nums)

        return map


def trailhead_rating(map: List[List[int]], trailhead:(int, int)) -> int:
    rows = len(map)
    cols = len(map[0])
    path = deque([trailhead])

    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    count = 0

    while path:
        (row, col) = path.popleft()

        if map[row][col] == 9:
            count += 1
            continue

        for next_row, next_col in dir:
            next_row, next_col = row + next_row, col + next_col

            if 0 <= next_row < rows and 0 <= next_col < cols:
                if map[next_row][next_col] == map[row][col] + 1:
                    path.append((next_row, next_col))

    return count

def solve(file_path: str) -> int:
    map = load_input(file_path)

    m = len(map)
    n = len(map[0])

    sum_rating = 0

    for i in range(m):
        for j in range(n):
            if map[i][j] == 0:
                score = trailhead_rating(map, (i, j))
                sum_rating += score

    return sum_rating

if __name__ == '__main__':
    sum_rating = solve('input')
    print(F"Part 2: {sum_rating}")