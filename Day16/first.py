import heapq

def load_input(filepath:str) -> list:
    map = []
    with open(filepath) as file:
        for line in file:
            strs = [char for char in line.strip()]
            map.append(strs)

    return map


def find_cheapest_path(map: list) -> int:
    rows, cols = len(map), len(map[0])
    start = (rows - 2, 1)
    end = (1, cols - 2)

    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    pq = []
    for dx, dy in directions:
        initial_cost = 0 if (dx, dy) == (0, 1) else 1000
        heapq.heappush(pq, (initial_cost, start[0], start[1], dx, dy))

    visited = {}

    while pq:
        cost, x, y, dx, dy = heapq.heappop(pq)

        if (x, y, dx, dy) in visited and visited[(x, y, dx, dy)] <= cost:
            continue
        visited[(x, y, dx, dy)] = cost

        if (x, y) == end:
            return cost

        for ndx, ndy in directions:
            nx, ny = x + ndx, y + ndy
            if map[nx][ny] != '#':
                new_cost = cost + (1 if (ndx, ndy) == (dx, dy) else 1001)
                if (nx, ny, ndx, ndy) not in visited or new_cost < visited[(nx, ny, ndx, ndy)]:
                    heapq.heappush(pq, (new_cost, nx, ny, ndx, ndy))

    return float('inf')


if __name__ == "__main__":
    map = load_input('test')
    sol = find_cheapest_path(map)
    print(f'Part1: {sol}')