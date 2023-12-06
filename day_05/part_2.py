from math import sqrt

input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.rstrip())


def destionation(seed):
    mappings = []

    line = 1
    while line < len(input):
        if input[line] == "":
            line += 2

            map = []

            while input[line] != "":
                if line >= len(input) - 1:
                    map.append(input[line].split(" "))
                    line += 1
                    break
                map.append(input[line].split(" "))
                line += 1

            mappings.append(map)

    for map in mappings:
        for values in map:
            if int(values[1]) <= int(seed) and int(seed) < int(values[1]) + int(values[2]):
                seed = int(values[0]) + int(seed) - int(values[1])
                break

    return seed


seeds = input[0].lstrip("seeds: ").split()

pairs = [[int(seeds[i]), int(seeds[i + 1])] for i in range(0, len(seeds), 2)]

iter = 0
for i in pairs:
    iter += i[1]
jumps = int(sqrt(iter))

lowest = -1
lowest_range = -1

for i in pairs:
    for j in range(i[0], i[0] + i[1]):
        if j % jumps == 0:
            iter = destionation(j)
            if lowest < 0 or destionation(j) < lowest:
                lowest = iter
                lowest_range = j

for i in range(lowest_range - jumps, lowest_range + jumps):
    iter = destionation(i)
    if destionation(i) < lowest:
        lowest = iter

print(lowest)
