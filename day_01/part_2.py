numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.rstrip())


def get_number(line):
    s1 = 0
    s2 = 0

    e1 = len(line)
    e2 = len(line)

    while True:
        if line[s1:s2] in numbers:
            break
        elif s2 > len(line) - 1:
            s1 += 1
            s2 = s1
        else:
            s2 += 1

    while True:
        if line[e1:e2] in numbers:
            break
        elif e1 < 0:
            e2 -= 1
            e1 = e2
        else:
            e1 -= 1

    return numbers[line[s1:s2]] * 10 + numbers[line[e1:e2]]


sum = 0

for item in input:
    sum += get_number(item)

print(sum)
