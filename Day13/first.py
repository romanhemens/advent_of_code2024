
from scipy import optimize
import numpy as np
from typing import List

def load_input(file_path: str) ->List[List[int]]:
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
                        current_problem['Price_X'], current_problem['Price_Y']
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
                current_problem['Price_X'], current_problem['Price_Y']
            ])

    return problems

def optimization(A_X, A_Y, B_X, B_Y, Price_X, Price_Y):
    def constraint_x(optVar):
        x_A, x_B = optVar
        return x_A * A_X + x_B * B_X - Price_X

    def constraint_y(optVar):
        x_A, x_B = optVar
        return x_A * A_Y + x_B * B_Y - Price_Y

    def objFun(optVar):
        x_A, x_B = optVar
        return 3 * x_A + x_B

    cons = [
        {'type': 'eq', 'fun': constraint_x},
        {'type': 'eq', 'fun': constraint_y}
    ]

    bounds = ((0, 100), (0, 100))

    optVar_start = [0, 0]

    try:
        res = optimize.minimize(objFun, optVar_start, method='SLSQP', bounds=bounds, constraints=cons)

        if not res.success:
            return -1
        else:
            x_A, x_B = np.round(res.x).astype(int)
            if (np.isclose(x_A * A_X + x_B * B_X, Price_X) and
                    np.isclose(x_A * A_Y + x_B * B_Y, Price_Y)):
                return 3*x_A + x_B
            else:
                return -1
    except Exception as e:
        return -1

def solve(input: List[List[int]]) -> int:
    tokens = 0

    for problem in input:
        A_X, A_Y, B_X, B_Y, Price_X, Price_Y = problem
        solution = optimization(A_X, A_Y, B_X, B_Y, Price_X, Price_Y)
        if solution > 0:
            tokens += solution

    return tokens

if __name__ == '__main__':
    input = load_input('input')
    tokens = solve(input)
    print(f'Part 1: {tokens}')
