import re

a = []
things = dict()

with open("input.txt") as file:
    for line in file:
        a.append(line.rstrip())

for num, item in enumerate(a):
    x, y = item.split(":")

    z = y.split(";")

    things[num + 1] = [0, 0, 0]

    for i in z:
        blue_matches = re.findall(r"(\d+)\s+blue", i)

        if blue_matches and things[num + 1][0] < int(blue_matches[0]):
            things[num + 1][0] = int(blue_matches[0])

        red_matches = re.findall(r"(\d+)\s+red", i)

        if red_matches and things[num + 1][1] < int(red_matches[0]):
            things[num + 1][1] = int(red_matches[0])

        green_matches = re.findall(r"(\d+)\s+green", i)

        if green_matches and things[num + 1][2] < int(green_matches[0]):
            things[num + 1][2] = int(green_matches[0])

sum = 0

for i in things:
    sum += (things[i][0] * things[i][1] * things[i][2])

print(sum)
