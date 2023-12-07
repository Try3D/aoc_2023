class Cards:
    def __init__(self, hand):
        self.hand = hand

        self.count = {}
        for card in hand:
            if card in self.count:
                self.count[card] += 1
            else:
                self.count[card] = 1

        if "J" in self.count and not self.count["J"] == 5:
            no_of_J = self.count.pop("J")

            highest_cards = []
            highest_count = 0
            for count in self.count:
                if self.count[count] > highest_count:
                    highest_count = self.count[count]
                    highest_cards = [count]
                elif self.count[count] == highest_count:
                    highest_cards += [count]

            if len(highest_cards) == 1:
                self.count[highest_cards[0]] += no_of_J
            else:
                highest_cards.sort(
                    key=lambda x: self.priority[x], reverse=True)
                self.count[highest_cards[0]] += no_of_J

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
        "J": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "Q": 11,
        "K": 12,
        "A": 13,
    }


input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.rstrip())

cards = []
points = []

for card in input:
    hand, point = card.split()
    cards.append(Cards(hand))
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
