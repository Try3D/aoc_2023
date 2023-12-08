import re

with open("input.txt") as file:
    input = [line.rstrip() for line in file]

games = {id + 1 for id in range(len(input))}

for num, item in enumerate(input):
    game, cubes = item.split(":")
    round = cubes.split(";")

    for hand in round:
        blue = re.findall(r"(\d+) blue", hand)
        if blue and int(blue[0]) > 14:
            try:
                games.remove(num + 1)
            except KeyError:
                continue

        red = re.findall(r"(\d+) red", hand)
        if red and int(red[0]) > 12:
            try:
                games.remove(num + 1)
            except KeyError:
                continue

        green = re.findall(r"(\d+) green", hand)
        if green and int(green[0]) > 13:
            try:
                games.remove(num + 1)
            except KeyError:
                continue

sum = 0

for id in games:
    sum += id

print(sum)
