
import re
from typing import List

def load_input(file_path: str) -> List[int]:
    with open(file_path) as f:
        return list(map(int, re.findall(r'\d', f.read())))

def calculate_checksum(disk: List[int]) -> int:
    return sum(pos * file_id for pos, file_id in enumerate(disk) if file_id != -1)

def compact_disk_with_files(disk_map: List[int]) -> int:
    files = {}
    free_spaces = []
    position = 0

    for i, length in enumerate(disk_map):
        if i % 2 == 0:
            files[i // 2] = (position, length)
        else:
            free_spaces.append((position, length))
        position += length

    for file_id, (file_pos, file_size) in reversed(files.items()):
        for i, (space_pos, space_size) in enumerate(free_spaces):
            if space_pos >= file_pos:
                break
            if file_size > space_size:
                continue

            files[file_id] = (space_pos, file_size)
            new_space_size = space_size - file_size

            if new_space_size == 0:
                free_spaces.pop(i)
            else:
                free_spaces[i] = (space_pos + file_size, new_space_size)
            break

    return sum(
        sum(file_id * pos for pos in range(start, start + size))
        for file_id, (start, size) in files.items()
    )

def solve(disk_map: List[int]) -> int:

    part2_checksum = compact_disk_with_files(disk_map)

    return part2_checksum

if __name__ == "__main__":
    input_data = load_input("input")
    part2 = solve(input_data)
    print(f"Part 2: {part2}")