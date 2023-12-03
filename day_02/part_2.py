import re

input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.rstrip())

games = dict()

for num, item in enumerate(input):
    game, cubes = item.split(":")
    round = cubes.split(";")

    games[num + 1] = [0, 0, 0]

    for hand in round:
        blue = re.findall(r"(\d+) blue", hand)
        if blue and games[num + 1][0] < int(blue[0]):
            games[num + 1][0] = int(blue[0])

        red = re.findall(r"(\d+) red", hand)
        if red and games[num + 1][1] < int(red[0]):
            games[num + 1][1] = int(red[0])

        green = re.findall(r"(\d+) green", hand)
        if green and games[num + 1][2] < int(green[0]):
            games[num + 1][2] = int(green[0])

sum = 0

for id in games:
    sum += (games[id][0] * games[id][1] * games[id][2])

print(sum)
