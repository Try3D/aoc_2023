class Card:
    def __init__(self, hand):
        self.hand = hand

        self.count = {}
        for card in hand:
            if card in self.count:
                self.count[card] += 1
            else:
                self.count[card] = 1

    def __gt__(self, other):
        self_list = []
        other_list = []

        for card in self.count:
            self_list.append(self.count[card])
        for card in other.count:
            other_list.append(other.count[card])

        self_list.sort(reverse=True)
        other_list.sort(reverse=True)

        for i in range(min(len(self_list), len(other_list))):
            if self_list[i] > other_list[i]:
                return True
            elif self_list[i] < other_list[i]:
                return False

        for i in range(len(self.hand)):
            if self.priority[self.hand[i]] > other.priority[other.hand[i]]:
                return True
            elif self.priority[self.hand[i]] < other.priority[other.hand[i]]:
                return False

    priority = {
        "2": 1,
        "3": 2,
        "4": 3,
        "5": 4,
        "6": 5,
        "7": 6,
        "8": 7,
        "9": 8,
        "T": 9,
        "J": 10,
        "Q": 11,
        "K": 12,
        "A": 13,
    }


with open("input.txt") as file:
    input = [line.rstrip() for line in file]

cards = []
points = []

for card in input:
    hand, point = card.split()
    cards.append(Card(hand))
    points.append(int(point))

for i in range(len(cards) - 1):
    for j in range(len(cards) - i - 1):
        if cards[j] > cards[j + 1]:
            cards[j], cards[j + 1] = cards[j + 1], cards[j]
            points[j], points[j + 1] = points[j + 1], points[j]

sum = 0
for num, val in enumerate(points):
    sum += (num + 1) * val

print(sum)
