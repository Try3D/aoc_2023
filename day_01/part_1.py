with open("input.txt") as file:
    input = [line.rstrip() for line in file]

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
