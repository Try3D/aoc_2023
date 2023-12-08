with open("input.txt") as file:
    input = [line.rstrip() for line in file]

seeds = []
s = []
for n, number in enumerate(input[0].lstrip("seeds: ").split()):
    if n % 2:
        s.append(s[0] + int(number))
        seeds.append(s)
        s = []
    else:
        s.append(int(number))

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

        new_seeds = []

        while len(seeds):
            i = seeds.pop()

            s = i[0]
            e = i[1]

            flag = 1
            for m in map:
                a = int(m[0])
                b = int(m[1])
                c = int(m[2])

                os = max(s, b)
                oe = min(e, b + c)

                if os < oe:
                    new_seeds.append([os - b + a, oe - b + a])
                    if os > s:
                        seeds.append([s, os])
                    if oe < e:
                        seeds.append([oe, e])
                    flag = 0
                    break

            if flag:
                new_seeds.append([s, e])

        seeds = new_seeds

lowest = -1
for seed in seeds:
    if lowest < 0 or seed[0] < lowest:
        lowest = seed[0]

print(lowest)
