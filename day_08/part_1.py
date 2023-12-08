import re

input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.rstrip())

nav = input[0]

directions = {}
for direction in input[2:]:
    m, l, r = re.findall(r"(.*) = \((.*), (.*)\)", direction)[0]

    directions[m] = [l, r]

cur = "AAA"
end = "ZZZ"

n = 0
while cur != end:
    for dir in nav:
        if dir == "L":
            cur = directions[cur][0]
        else:
            cur = directions[cur][1]
        n += 1

print(n)
