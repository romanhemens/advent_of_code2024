
file = open('input').read().splitlines()
a = []
b = []
for line in file:
    x = line.split('   ')
    a.append(int(x[0]))
    b.append(int(x[1]))

sum = 0
for i in range(len(a)):
    sum += b.count(a[i]) * a[i]

print(sum)
