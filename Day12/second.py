from typing import List, Tuple
from collections import deque

def load_input(file_path: str) -> List[List[str]]:
    with open(file_path) as f:
        map = []
        for line in f:
            strs = [char for char in line.strip()]
            map.append(strs)

        return map

def calculate_area_and_sides(map: List[List[str]], row: int, col: int, m: int, n: int) -> Tuple[int, int, set]:
    region = set()
    region.add((row, col))

    path = deque([(row, col)])
    sides = set()
    side_count = 0
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]


    while path:
        x, y = path.popleft()

        for dx, dy in dir:

            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= m or ny < 0 or ny >= n or map[nx][ny] != map[x][y] :

                if not((dx, dy, x - 1, y) in sides or (dx, dy, x + 1, y) in sides or (dx, dy, x, y - 1) in sides or (dx, dy, x, y + 1) in sides):
                    side_count += 1
                if ((dx, dy, x - 1, y) in sides and (dx, dy, x + 1, y) in sides) or ((dx, dy, x, y - 1) in sides and (dx, dy, x, y + 1) in sides):
                    side_count -= 1

                sides.add((dx, dy, x, y))
                continue

            if (nx, ny) not in region:
                path.append((nx, ny))
                region.add((nx, ny))

    return len(region), side_count, region



def solve(map: List[List[str]]) -> int:
    m = len(map)
    n = len(map[0])
    regions = set()
    price = 0
    for i in range(m):
        for j in range(n):
            if (i, j) not in regions:
                pass
                area, sides, region = calculate_area_and_sides(map, i, j, m, n)
                regions.update(region)
                price += area*sides

    return price


if __name__ == '__main__':
    input = load_input('input')

    price = solve(input)
    print(f'Part 2: {price}')