
file = open('input').read().splitlines()
a = []
b = []
for line in file:
    x = line.split('   ')
    a.append(int(x[0]))
    b.append(int(x[1]))

a = sorted(a)
b = sorted(b)
sum = 0

for i in range(len(a)):
    sum += abs(a[i]-b[i])

print(sum)