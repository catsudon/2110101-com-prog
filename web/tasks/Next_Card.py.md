
# Task: Next_Card.py

``` py
mp = {"c": 0, "d": 1, "h": 2, "s": 3}
namae = ["club", "diamond", "heart", "spade"]


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "({} {})".format(self.value, self.suit)

    def next1(self):
        score = ['3', '4', '5', '6', '7', '8',
                 '9', '10', 'J', 'Q', 'K', 'A', '2']
        val = score.index(self.value)
        face = mp[self.suit[0]] + 1
        if (face > 3):
            val += 1
            face %= 4
        val %= 13
        return Card(score[val], namae[face])

    def next2(self):
        score = ['3', '4', '5', '6', '7', '8',
                 '9', '10', 'J', 'Q', 'K', 'A', '2']
        val = score.index(self.value)
        face = mp[self.suit[0]] + 1
        if (face > 3):
            val += 1
            face %= 4
        val %= 13
        self.value = score[val]
        self.suit = namae[face]


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
```
    