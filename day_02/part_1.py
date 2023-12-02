import re

input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.rstrip())

games = set()
for id in range(len(input)):
    games.add(id + 1)

for num, item in enumerate(input):
    game, cubes = item.split(":")
    round = cubes.split(";")

    for hand in round:
        blue = re.findall(r"(\d+)\s+blue", hand)
        if blue and int(blue[0]) > 14:
            try:
                games.remove(num + 1)
            except KeyError:
                continue

        red = re.findall(r"(\d+)\s+red", hand)
        if red and int(red[0]) > 12:
            try:
                games.remove(num + 1)
            except KeyError:
                continue

        green = re.findall(r"(\d+)\s+green", hand)
        if green and int(green[0]) > 13:
            try:
                games.remove(num + 1)
            except KeyError:
                continue

sum = 0

for id in games:
    sum += id

print(sum)
