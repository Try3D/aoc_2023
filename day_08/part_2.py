import re
from math import lcm

with open("input.txt") as file:
    input = [line.rstrip() for line in file]

nav = input[0]

directions = {}
for direction in input[2:]:
    m, l, r = re.findall(r"(.*) = \((.*), (.*)\)", direction)[0]

    directions[m] = [l, r]

cur = [location for location in directions if location.endswith("A")]

n = 1
end_len = []

while cur:
    for dir in nav:
        new_cur = []
        for path in cur:
            if dir == "L":
                item = directions[path][0]
                if item.endswith("Z"):
                    end_len.append(n)
                else:
                    new_cur.append(item)
            else:
                item = directions[path][1]
                if item.endswith("Z"):
                    end_len.append(n)
                else:
                    new_cur.append(item)
        cur = new_cur
        n += 1

print(lcm(*end_len))
