class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


with open("input.txt") as file:
    input = [line.rstrip() for line in file]


def main():
    start = Coordinates(0, 0)
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == "S":
                start = Coordinates(x, y)

    main_loop = path(start)

    matrix = ["" for _ in range(len(input) * 3)]

    set_matrix(matrix, main_loop)

    n = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "." and check_enclosed(matrix, x, y):
                n += 1

    print(n)


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

    loop = []
    for i in traversal[0:-1]:
        for j in i:
            loop.append(j)
    return loop


def set_matrix(matrix, loop):
    for y in range(len(input)):
        for x in range(len(input[0])):
            cord = Coordinates(x, y)
            if cord in loop and input[y][x] == "|":
                l1 = " # "
                l2 = " # "
                l3 = " # "
            elif Coordinates(x, y) in loop and input[y][x] == "-":
                l1 = "   "
                l2 = "###"
                l3 = "   "
            elif Coordinates(x, y) in loop and input[y][x] == "L":
                l1 = " # "
                l2 = " ##"
                l3 = "   "
            elif Coordinates(x, y) in loop and input[y][x] in ["F", "S"]:
                l1 = "   "
                l2 = " ##"
                l3 = " # "
            elif Coordinates(x, y) in loop and input[y][x] == "7":
                l1 = "   "
                l2 = "## "
                l3 = " # "
            elif Coordinates(x, y) in loop and input[y][x] == "J":
                l1 = " # "
                l2 = "## "
                l3 = "   "
            else:
                l1 = "   "
                l2 = " . "
                l3 = "   "
            matrix[3 * y] += l1
            matrix[3 * y + 1] += l2
            matrix[3 * y + 2] += l3


def check_enclosed(matrix, x, y):
    path = [Coordinates(x, y)]
    seen = [[0] * len(matrix[0]) for _ in range(len(matrix))]

    while path:
        z = path.pop()

        if z.x < 0 or z.x > len(matrix[0]) - 1 or z.y < 0 or z.y > len(matrix) - 1:
            return False
        if seen[z.y][z.x]:
            continue
        if matrix[z.y][z.x] == "#":
            continue

        seen[z.y][z.x] = 1

        path.append(z + Coordinates(1, 0))
        path.append(z + Coordinates(-1, 0))
        path.append(z + Coordinates(0, 1))
        path.append(z + Coordinates(0, -1))

    return True


if __name__ == "__main__":
    main()
