from itertools import product

file = open('input').read().splitlines()
test = open('test').read().splitlines()

def evaluation(target, values):
    n = len(values) - 1
    operators = product(['+', '*'], repeat=n)

    for operator in operators:
        result = values[0]
        for i, op in enumerate(operator):
            if op == '+':
                result += values[i + 1]
            elif op == '*':
                result *= values[i + 1]
        if result == target:
            return True
    return False

def calibration(file):
    cal_result = []
    for line in file:
        target, equation = line.split(': ')
        equation = list(map(int, equation.split(' ')))
        if evaluation(int(target), equation):
            cal_result.append(int(target))

    return sum(cal_result)

print('Answer - Part 1 =', calibration(file))

