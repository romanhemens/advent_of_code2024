
import re
from typing import List

def load_input(file_path: str) -> List[int]:
    with open(file_path) as f:
        return list(map(int, re.findall(r'\d', f.read())))

def calculate_checksum(disk: List[int]) -> int:
    return sum(pos * file_id for pos, file_id in enumerate(disk) if file_id != -1)

def compact_disk_with_blocks(disk_map: List[int]) -> List[int]:
    disk = []
    for i, length in enumerate(disk_map):
        if i % 2 == 0:
            disk.extend([i // 2] * length)
        else:
            disk.extend([-1] * length)

    free_positions = [i for i, val in enumerate(disk) if val == -1]

    for free_pos in free_positions:
        while disk[-1] == -1:
            disk.pop()
        if len(disk) <= free_pos:
            break
        disk[free_pos] = disk.pop()

    return disk

def solve(disk_map: List[int]) -> int:
    compacted_disk = compact_disk_with_blocks(disk_map)
    part1_checksum = calculate_checksum(compacted_disk)

    return part1_checksum

if __name__ == "__main__":
    input_data = load_input("input")
    part1 = solve(input_data)
    print(f"Part 1: {part1}")


