
file = open('input').read().splitlines()

def is_sorted_descending(lst):
    return all(
        lst[index+1] < lst[index] <= lst[index+1] + 3
        for index in range(len(lst) - 1)
    )

def is_sorted_ascending(lst):
    return all(
        lst[index] < lst[index+1] <= lst[index]+3
        for index in range(len(lst) - 1)
    )

def check_reports(lst):
    if is_sorted_descending(lst) or is_sorted_ascending(lst):
        return True
    return False


sum = 0
for line in file:
    x = list(map(int, line.split()))
    if check_reports(x):
        sum += 1


print(sum)