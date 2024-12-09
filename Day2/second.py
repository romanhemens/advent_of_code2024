
file = open('input').read().splitlines()

def is_safe(lst):
    ascending = True
    descending = True
    i = 0
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1] <= lst[i] + 3 and ascending:
            descending = False
        elif lst[i + 1] < lst[i] <= lst[i + 1] + 3 and descending:
            ascending = False
        else:
            return False

    return True

def problem_damper(lst):
    if is_safe(lst):
        return True

    for i in range(len(lst)):
        temp_lst = lst[:i] + lst[i + 1:]
        if is_safe(temp_lst):
            return True

    return False


sum_safe = 0
for line in file:
    x = list(map(int, line.split()))
    if problem_damper(x):
        sum_safe += 1

print(sum_safe)
