with open("input.txt") as file:
    input = [line.rstrip() for line in file]

list1 = []
list2 = []

for card in input:
    num, data = card.split(": ")

    s1, s2 = data.split(" | ")

    list1.append(s1.split(" "))
    list2.append(s2.split(" "))

list1 = [[elem for elem in sublist if elem != ""] for sublist in list1]
list2 = [[elem for elem in sublist if elem != ""] for sublist in list2]


def get_cards(hand):
    n = 0
    for i in range(len(list1[0])):
        for j in range(len(list2[0])):
            if list1[hand - 1][i] == list2[hand - 1][j]:
                n += 1
    return [hand + i + 1 for i in range(n)]


queue = [i + 1 for i in range(len(input))]
points = 0

while queue:
    queue += get_cards(queue.pop())
    points += 1

print(points)
