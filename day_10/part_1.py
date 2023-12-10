class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)


with open("input.txt") as file:
    input = [line.rstrip() for line in file]

start = Coordinates(0, 0)
for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == "S":
            start = Coordinates(x, y)


def path(position):
    traversal = [[position]]
    seen = [[False] * len(input[0]) for _ in range(len(input))]

    while traversal[-1]:
        stack = [location for location in traversal[-1]]
        next_positions = []
        while stack:
            pos = stack.pop()

            if pos.x < 0 or pos.x > len(input[0]) - 1 or pos.y < 0 or pos.y > len(input) - 1:
                continue
            if seen[pos.y][pos.x]:
                continue
            if input[pos.y][pos.x] == ".":
                continue

            seen[pos.y][pos.x] = True

            if input[pos.y][pos.x] == "|":
                next_positions.append(pos + Coordinates(0, 1))
                next_positions.append(pos + Coordinates(0, -1))
            elif input[pos.y][pos.x] == "-":
                next_positions.append(pos + Coordinates(1, 0))
                next_positions.append(pos + Coordinates(-1, 0))
            elif input[pos.y][pos.x] == "7":
                next_positions.append(pos + Coordinates(-1, 0))
                next_positions.append(pos + Coordinates(0, 1))
            elif input[pos.y][pos.x] == "L":
                next_positions.append(pos + Coordinates(1, 0))
                next_positions.append(pos + Coordinates(0, -1))
            elif input[pos.y][pos.x] == "J":
                next_positions.append(pos + Coordinates(-1, 0))
                next_positions.append(pos + Coordinates(0, -1))
            elif input[pos.y][pos.x] in ["F", "S"]:
                next_positions.append(pos + Coordinates(1, 0))
                next_positions.append(pos + Coordinates(0, 1))

        traversal.append(next_positions)

    return traversal[1:-1]


print(len(path(start)) - 1)
