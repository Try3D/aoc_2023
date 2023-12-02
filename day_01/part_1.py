a = []
sum = 0

with open("./input.txt") as file:
    for line in file:
        a.append(line.rstrip())

for item in a:
    s = 0
    e = len(item) - 1

    while not item[s].isnumeric():
        s += 1

    while not item[e].isnumeric():
        e -= 1

    sum += int(item[s]) * 10 + int(item[e])

print(sum)
