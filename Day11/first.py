from typing import List


def load_input(file_path: str) -> List[int]:
    with open(file_path, 'r') as f:
        return list(map(int, f.read().split(' ')))


def rules(stone: int) -> List[int]:
    n = len(str(stone))
    if stone == 0:
        return [1]
    elif n % 2 == 0:
        left = int(str(stone)[0:n // 2])
        right = int(str(stone)[n // 2:])
        return [left, right]
    else:
        return [stone * 2024]


def solve(input: List[int], blinking: int) -> int:

    for _ in range(blinking):
        arrangement = []
        for stone in input:
            results = rules(stone)
            for res in results:
                arrangement.append(res)

        input = arrangement

    return len(input)


if __name__ == '__main__':
    input = load_input('input')
    part1= solve(input, 25)
    print(f'Part 1: {part1}')