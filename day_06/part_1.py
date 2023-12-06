import re

input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.rstrip())

times = re.findall(r"\b\d+\b", input[0])
distances = re.findall(r"\b\d+\b", input[1])

races = []

for time in times:
    runs = []

    for t in range(int(time) + 1):
        runs.append(t * (int(time) - t))

    races.append(runs)

runs = 1

for time in range(len(races)):
    n = 0
    for t in races[time]:
        if t > int(distances[time]):
            n += 1

    runs = runs * n

print(runs)
