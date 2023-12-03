class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_adjacent(self):
        adjacents = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.x + i >= 0 and self.x + i < len(input[0]) and self.y + j >= 0 and self.y + j < len(input):
                    adjacents.append(Coordinates(self.x + i, self.y + j))

        return adjacents

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.rstrip())

num_cords = []

for y in range(len(input)):
    x = 0
    while x < len(input[0]):
        cord = []
        if input[y][x].isdigit():
            cord.append(Coordinates(x, y))
            while x < len(input[0]) and input[y][x].isdigit():
                x += 1
            cord.append(Coordinates(x - 1, y))
            num_cords.append(cord)
        else:
            x += 1

adj_num = []

for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == "*":
            cord = Coordinates(x, y)
            gears = []
            for number in num_cords:
                if number[0] in cord.get_adjacent() or number[1] in cord.get_adjacent():
                    gears.append(number)
            adj_num.append(gears)

sum = 0

for num in adj_num:
    if len(num) == 2:
        g1 = 0
        for number in range(num[0][0].x, num[0][1].x + 1):
            g1 = g1 * 10 + int(input[num[0][0].y][number])

        g2 = 0
        for number in range(num[1][0].x, num[1][1].x + 1):
            g2 = g2 * 10 + int(input[num[1][0].y][number])

        sum += g1 * g2

print(sum)
