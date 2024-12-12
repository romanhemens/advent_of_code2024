from typing import List, Tuple
from collections import deque

def load_input(file_path: str) -> List[List[str]]:
    with open(file_path) as f:
        map = []
        for line in f:
            strs = [char for char in line.strip()]
            map.append(strs)

        return map

def calculate_area_and_region(map: List[List[str]], row: int, col: int, m: int, n: int) -> Tuple[int, int, set]:

    region = set()
    region.add((row, col))

    path = deque([(row, col)])
    parameter = 0

    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while path:
        x, y = path.popleft()

        for dx, dy in dir:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n:
                if map[nx][ny] == map[x][y]:
                    if (nx, ny) not in region:
                        path.append((nx, ny))
                        region.add((nx, ny))

                else:
                    parameter += 1
            else:
                parameter += 1


    return len(region), parameter, region


def solve(map: List[List[str]]) -> int:
    m = len(map)
    n = len(map[0])
    regions = set()
    price = 0
    for i in range(m):
        for j in range(n):
            if (i, j) not in regions:
                area, parameter, region = calculate_area_and_region(map, i, j, m, n)
                regions.update(region)
                price += area*parameter

    return price

if __name__ == '__main__':

    input = load_input('input')
    price = solve(input)
    print(f'Part 1: {price}')