from collections import defaultdict
import heapq

def load_input(filepath:str) -> list:
    map = []
    with open(filepath) as file:
        for line in file:
            strs = [char for char in line.strip()]
            map.append(strs)

    return map


def find_best_paths(map: list) -> list:
    rows, cols = len(map), len(map[0])
    start = (rows - 2, 1)
    end = (1, cols - 2)

    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    pq = []
    for dx, dy in directions:
        initial_cost = 0 if (dx, dy) == (0, 1) else 1000
        heapq.heappush(pq, (initial_cost, start[0], start[1], dx, dy, [start]))

    visited = defaultdict(lambda: float('inf'))

    best_paths = []
    best_cost = float('inf')

    while pq:
        cost, x, y, dx, dy, path = heapq.heappop(pq)

        if (x, y) == end:
            if cost < best_cost:
                best_cost = cost
                best_paths = [path]
            elif cost == best_cost:
                best_paths.append(path)
            continue

        if cost > visited[(x, y, dx, dy)]:
            continue

        visited[(x, y, dx, dy)] = cost

        for ndx, ndy in directions:
            nx, ny = x + ndx, y + ndy
            if map[nx][ny] != '#':
                new_cost = cost + (1 if (ndx, ndy) == (dx, dy) else 1000)
                heapq.heappush(pq, (new_cost, nx, ny, ndx, ndy, path + [(nx, ny)]))

    return best_paths


def count_tiles_in_best_paths(best_paths: list) -> int:
    marked = set()
    for path in best_paths:
        marked.update(path)

    return len(marked)


if __name__ == "__main__":
    map = load_input('input')
    best_paths = find_best_paths(map)
    sol = count_tiles_in_best_paths(best_paths)
    print(f'Part 2: {sol}')