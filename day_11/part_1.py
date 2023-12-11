class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y


with open("input.txt") as file:
    input = [line.rstrip() for line in file]

galaxies = [Coordinates(x, y) for y in range(len(input))
            for x in range(len(input[0])) if input[y][x] == "#"]

v = {x for x in range(len(input)) if "#" not in [row[x] for row in input]}
h = {y for y in range(len(input)) if "#" not in input[y]}

n = 0
for g1 in galaxies:
    for g2 in galaxies:
        for y in range(min(g1.x, g2.x), max(g1.x, g2.x)):
            if y in v:
                n += 1

        for x in range(min(g1.y, g2.y), max(g1.y, g2.y)):
            if x in h:
                n += 1

        n += abs(g2.y - g1.y) + abs(g2.x - g1.x)

print(int(n / 2))
