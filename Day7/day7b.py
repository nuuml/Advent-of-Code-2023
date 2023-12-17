from functools import cmp_to_key
from collections import Counter

source = open('day7.txt', 'r').read().split("\n")

def custom_comparison(a, b):
    def get_type(hand):
        jokers = hand.count('J')
        hand = [c for c in hand if c != 'J']
        counts = sorted(Counter(hand).values(), reverse=True)
        if not counts:
            counts = [0]
        if counts[0] + jokers == 5:
            return 6
        if counts[0] + jokers == 4:
            return 5
        if counts[0] + jokers == 3 and counts[1] == 2:
            return 4
        if counts[0] + jokers == 3:
            return 3
        if counts[0] == 2 and (jokers or counts[1] == 2):
            return 2
        if counts[0] == 2 or jokers:
            return 1
        return 0

    def compare_cards(card_a, card_b):
        return cards.index(card_a) - cards.index(card_b)

    type_a = get_type(a.split(" ")[0])
    type_b = get_type(b.split(" ")[0])

    if type_a > type_b:
        return 1
    elif type_a < type_b:
        return -1
    else:
        # Resolve ties by comparing individual cards
        hand_a = a.split(" ")[0]
        hand_b = b.split(" ")[0]
        for card_a, card_b in zip(hand_a, hand_b):
            if card_a != card_b:
                return compare_cards(card_a, card_b)

    return 0


cards = 'J23456789TQKA'

sorted_array = sorted(source, key=cmp_to_key(custom_comparison))

total = 0
for i in range(len(sorted_array)):
    mult = i + 1
    add = int(sorted_array[i].split(" ")[1]) * mult
    total += add

print(total)
