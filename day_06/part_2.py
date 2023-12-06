import re

input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.rstrip())

times = int("".join(re.findall(r"\b\d+\b", input[0])))
distances = int("".join(re.findall(r"\b\d+\b", input[1])))

n = 0

for i in range(times):
    if i * (times - i) > distances:
        n += 1

print(n)
