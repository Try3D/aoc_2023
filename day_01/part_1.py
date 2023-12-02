input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.rstrip())

sum = 0

for item in input:
    start = 0
    end = len(item) - 1

    while not item[start].isnumeric():
        start += 1

    while not item[end].isnumeric():
        end -= 1

    sum += int(item[start]) * 10 + int(item[end])

print(sum)
