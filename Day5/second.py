from Day5.first import preprocess, findMiddle

file = open('input').read().splitlines()

test = open('test').read().splitlines()

def order_the_incorrectly(incorrect_update, rules):

    def order(page):
        pos = 0
        for other_page in incorrect_update:
            if page in rules.get(other_page, set()):
                pos += 1

        return pos

    return sorted(incorrect_update, key=order)

def identify_incorrect_updates(file):
    order_dic, update_list = preprocess(file)
    result = 0
    incorrect_updates = []
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

        if len(correct) < len(list):
            incorrect_updates.append(list)

    for list in incorrect_updates:
        correctly_ordered = order_the_incorrectly(list, order_dic)
        middle = findMiddle(correctly_ordered)
        result += middle


    return result


print('Answer - Part 2: ', identify_incorrect_updates(file))