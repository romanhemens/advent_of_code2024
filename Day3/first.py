import re

corrupted_memory = open('input').read()

pattern = r"mul\(\d+,\d+\)"
sections = re.findall(pattern, corrupted_memory)

result = 0

for sec in sections:
    nums = re.findall(r"\d+", sec)
    if len(nums) == 2:
        x, y = map(int, nums)
        result += x * y

print("Answer:", result)
