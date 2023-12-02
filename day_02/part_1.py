import re

a = []

with open("input.txt") as file:
    for line in file:
        a.append(line.rstrip())

n = set()

for i in range(len(a)):
    n.add(i + 1)

for num, item in enumerate(a):
    x, y = item.split(":")

    z = y.split(";")

    for i in z:
        blue_matches = re.findall(r"(\d+)\s+blue", i)
        if blue_matches and int(blue_matches[0]) > 14:
            try:
                n.remove(num + 1)
            except KeyError:
                continue

        red_matches = re.findall(r"(\d+)\s+red", i)
        if red_matches and int(red_matches[0]) > 12:
            try:
                n.remove(num + 1)
            except KeyError:
                continue

        green_matches = re.findall(r"(\d+)\s+green", i)
        if green_matches and int(green_matches[0]) > 13:
            try:
                n.remove(num + 1)
            except KeyError:
                continue

sum = 0

for i in n:
    sum += i

print(sum)
