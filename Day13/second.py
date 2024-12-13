from sympy import solve
from sympy import Eq
from sympy.abc import x, y
from typing import List

def load_input(file_path: str, prize_offset=int) -> List[List[int]]:
    problems = []
    current_problem = {}

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                if current_problem:
                    problems.append([
                        current_problem['A_X'], current_problem['A_Y'],
                        current_problem['B_X'], current_problem['B_Y'],
                        current_problem['Price_X'] + prize_offset,
                        current_problem['Price_Y'] + prize_offset
                    ])
                    current_problem = {}
            elif line.startswith("Button A:"):
                parts = line.split(',')
                current_problem['A_X'] = int(parts[0].split('+')[1])
                current_problem['A_Y'] = int(parts[1].split('+')[1])
            elif line.startswith("Button B:"):
                parts = line.split(',')
                current_problem['B_X'] = int(parts[0].split('+')[1])
                current_problem['B_Y'] = int(parts[1].split('+')[1])
            elif line.startswith("Prize:"):
                parts = line.split(',')
                current_problem['Price_X'] = int(parts[0].split('=')[1])
                current_problem['Price_Y'] = int(parts[1].split('=')[1])

        if current_problem:
            problems.append([
                current_problem['A_X'], current_problem['A_Y'],
                current_problem['B_X'], current_problem['B_Y'],
                current_problem['Price_X'] + prize_offset,
                current_problem['Price_Y'] + prize_offset
            ])

    return problems

def optimization(A_X: int, A_Y: int, B_X: int, B_Y: int, Price_X: int, Price_Y: int) -> int:
    equations = [
        Eq(x * A_X + y * B_X, Price_X),
        Eq(x * A_Y + y * B_Y, Price_Y)
    ]

    sol = solve(equations, (x, y))
    if sol and all(sol[var].is_integer for var in [x, y]):
        return 3 * int(sol[x]) + int(sol[y])
    return -1

def prizes(input: List[List[int]]) -> int:
    tokens = 0
    for problem in input:
        A_X, A_Y, B_X, B_Y, Price_X, Price_Y = problem
        solution = optimization(A_X, A_Y, B_X, B_Y, Price_X, Price_Y)
        if solution >0:
            tokens += solution

    return tokens

if __name__ == '__main__':
    input = load_input('input', 10000000000000)

    tokens = prizes(input)
    print(f'Part 2: {tokens}')