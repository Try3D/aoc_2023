input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.rstrip())


def destination(seed):
    mappings = []

    line = 1
    while line < len(input):
        if input[line] == "":
            line += 2

            map = []

            while input[line] != "":
                if line >= len(input) - 1:
                    map.append(input[line].split())
                    line += 1
                    break
                map.append(input[line].split())
                line += 1

            mappings.append(map)

    for map in mappings:
        for values in map:
            if int(values[1]) <= int(seed) and int(seed) < int(values[1]) + int(values[2]):
                seed = int(values[0]) + int(seed) - int(values[1])
                break

    return seed


seeds = input[0].lstrip("seeds: ").split()

for n in range(len(seeds)):
    seeds[n] = destination(seeds[n])

seeds.sort()

print(seeds[0])
