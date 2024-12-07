from itertools import product

def evaluation(target, values):
    n = len(values) - 1
    operators = product(['+', '*', '||'], repeat=n)

    def concat(a, b):
        return int(f"{a}{b}")

    for operator in operators:
        result = values[0]
        for i, op in enumerate(operator):
            if op == '+':
                result += values[i + 1]
            elif op == '*':
                result *= values[i + 1]
            elif op == '||':
                result = concat(result, values[i + 1])
        if result == target:
            return True
    return False

def calibration(file):
    total = 0
    for line in file:
        target, equation = line.split(': ')
        equation = list(map(int, equation.split(' ')))
        if evaluation(int(target), equation):
            total += int(target)
    return total

file = open('input').read().splitlines()
test = open('test').read().splitlines()

print('Answer - Part 2 =', calibration(file))