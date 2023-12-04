input = []

with open('input.txt') as file:
    for line in file:
        input.append(line.rstrip())

list1 = []
list2 = []

for card in input:
    num, data = card.split(": ")

    s1, s2 = data.split(" | ")

    list1.append(s1.split(" "))
    list2.append(s2.split(" "))

list1 = [[elem for elem in sublist if elem != ''] for sublist in list1]
list2 = [[elem for elem in sublist if elem != ''] for sublist in list2]

points = 0

for i in range(len(list1)):
    p = 0
    for j in range(len(list1[0])):
        for k in range(len(list2[0])):
            if list1[i][j] == list2[i][k]:
                p += 1
    points += 2 ** (p - 1) if p > 0 else 0

print(points)
