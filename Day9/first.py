
import re
from typing import List

# Funktion zum Laden und Parsen der Eingabe
def load_input(file_path: str) -> List[int]:
    with open(file_path) as f:
        return list(map(int, re.findall(r'\d', f.read())))

# Funktion zur Berechnung der Checksumme nach dem Verschieben einzelner Blöcke
def calculate_checksum(disk: List[int]) -> int:
    return sum(pos * file_id for pos, file_id in enumerate(disk) if file_id != -1)

# Funktion zur Komprimierung von Dateien durch das Verschieben einzelner Blöcke
def compact_disk_with_blocks(disk_map: List[int]) -> List[int]:
    # Initiale Diskstruktur erstellen
    disk = []
    for i, length in enumerate(disk_map):
        if i % 2 == 0:  # Datei
            disk.extend([i // 2] * length)
        else:  # Freiraum
            disk.extend([-1] * length)

    # Liste der freien Positionen finden
    free_positions = [i for i, val in enumerate(disk) if val == -1]

    # Dateien verschieben, um Freiraum zu minimieren
    for free_pos in free_positions:
        while disk[-1] == -1:  # Überflüssigen Freiraum entfernen
            disk.pop()
        if len(disk) <= free_pos:  # Keine weiteren Verschiebungen möglich
            break
        disk[free_pos] = disk.pop()  # Letzten Block verschieben

    return disk


# Hauptfunktion zur Lösung beider Teile der Aufgabe
def solve(disk_map: List[int]) -> int:
    # Kompakter Zustand nach Blöcken
    compacted_disk = compact_disk_with_blocks(disk_map)
    part1_checksum = calculate_checksum(compacted_disk)

    return part1_checksum

# Ausführung des Programms
if __name__ == "__main__":
    input_data = load_input("input")
    part1 = solve(input_data)
    print(f"Part 1: {part1}")


