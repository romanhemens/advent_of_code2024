import re

corrupted_memory = open('input').read()

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
instructions = re.findall(pattern, corrupted_memory)

mul_enabled = True
result = 0

for ins in instructions:
    if ins == "do()":
        mul_enabled = True
    elif ins == "don't()":
        mul_enabled = False
    elif 'mul' in ins and mul_enabled:
        nums = re.findall(r"\d+", ins)
        if len(nums) == 2:
            x, y = map(int, nums)
            result += x * y

print('Answer: ',result)



