import re

with open("input.txt") as file:
    input = [line.rstrip() for line in file]

times = int("".join(re.findall(r"\b\d+\b", input[0])))
distances = int("".join(re.findall(r"\b\d+\b", input[1])))

n = 0

for i in range(times):
    if i * (times - i) > distances:
        n += 1

print(n)
