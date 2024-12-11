from typing import Dict, List
from collections import Counter


def load_input(file_path: str) -> Dict[int, int]:
    with open(file_path, 'r') as f:
        stones = list(map(int, f.read().split(' ')))
        return dict(Counter(stones))


def rules(stone: int) -> List[int]:
    n = len(str(stone))
    if stone == 0:
        return [1]
    elif n % 2 == 0:
        left = int(str(stone)[:n // 2])
        right = int(str(stone)[n // 2:])
        return [left, right]
    else:
        return [stone * 2024]


def solve(input_freq: Dict[int, int], blinking: int) -> int:
    cache = {}

    for _ in range(blinking):
        next_freq = {}
        for stone, count in input_freq.items():
            if stone in cache:
                results = cache[stone]
            else:
                results = rules(stone)
                cache[stone] = results

            for result in results:
                if result in next_freq:
                    next_freq[result] += count
                else:
                    next_freq[result] = count

        input_freq = next_freq

    return sum(input_freq.values())


if __name__ == '__main__':
    input_freq = load_input('input')
    part2 = solve(input_freq, 75)
    print(f'Part 2: {part2}')

