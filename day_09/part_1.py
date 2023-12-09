with open("input.txt") as file:
    input = [line.rstrip().split() for line in file]

input = [[int(i) for i in line] for line in input]


def find_next(seq):
    if not seq:
        return 0

    pred = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]

    n = find_next(pred)

    return seq[-1] + n


ans = sum([find_next(line) for line in input])

print(ans)
