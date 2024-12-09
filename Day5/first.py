file = open('input').read().splitlines()

def preprocess(file):
    order_dic = {}
    update_list = []
    updates = False
    for line in file:
        if line == '':
            updates = True
        elif not updates:
            first, second = line.split('|')

            first = int(first)
            second = int(second)

            if first not in order_dic:
                order_dic[first] = {second}
            else:
                order_dic[first].add(second)
        elif updates:
            update_list.append(list(map(int, line.split(','))))

    return order_dic, update_list

def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return input_list[int(middle)], input_list[int(middle - 1)]


def identify_correct_updates(file):
    order_dic, update_list = preprocess(file)
    result = 0

    for list in update_list:

        for i in range(len(list)):
            if i == 0:
                correct = {list[i]}
            else:
                if list[i] in order_dic:
                    if any(x in correct for x in order_dic[list[i]]):
                        break
                    else:
                        correct.add(list[i])
                else:
                    correct.add(list[i])

        if len(correct) == len(list):
            middle = findMiddle(list)
            result += middle

    return result

test = open('test').read().splitlines()

print('Answer - Part 1:', identify_correct_updates(file))











