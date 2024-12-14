
import re

def load_input(file_path: str) -> dict:
    robots = {}
    counter = 0
    with open(file_path) as file:
        for line in file:
            robot = re.findall(r"-?\d+", line)
            pos = [int(robot[0]), int(robot[1])]
            vel = [int(robot[2]), int(robot[3])]
            robots[counter] = pos, vel
            counter += 1
    return robots



def determine_final_pos(pos: list, velocity: list, width: int, height: int) -> tuple:

    for _ in range(100):
        next_pos = [pos[0] + velocity[0], pos[1] + velocity[1]]
        if next_pos[0] < 0:
            next_pos[0] = width + next_pos[0]
        elif next_pos[0] >= width:
            next_pos[0] = next_pos[0] - width

        if next_pos[1] < 0:
            next_pos[1] = height + next_pos[1]
        elif next_pos[1] >= height:
            next_pos[1] = next_pos[1] - height

        pos = next_pos

    return pos


def solve(robots: dict, width: int, height: int) -> int:
    middle_ver = width // 2
    middle_hor = height // 2
    quadrants = {'q1': 0, 'q2': 0, 'q3': 0, 'q4': 0}

    for i in range(len(robots)):
        pos = robots[i][0]
        vel = robots[i][1]

        final_pos = determine_final_pos(pos, vel, width, height)

        if not(final_pos[0] == middle_ver or final_pos[1] == middle_hor):

            if final_pos[0] < middle_ver:
                if final_pos[1] < middle_hor:
                    quadrants['q1'] += 1
                else:
                    quadrants['q3'] += 1
            else:
                if final_pos[1] < middle_hor:
                    quadrants['q2'] += 1
                else:
                    quadrants['q4'] += 1

    safety_factor = quadrants['q1'] * quadrants['q2'] * quadrants['q3'] * quadrants['q4']

    return safety_factor


if __name__ == '__main__':
    robots = load_input('input')

    safety_factor = solve(robots, 101, 103)

    print(F'Part 1: {safety_factor}')
