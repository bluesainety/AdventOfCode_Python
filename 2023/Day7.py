from enum import Enum, IntEnum
from operator import countOf, itemgetter

from helper import file_handler as fh

lines = fh.readLinesFromFile("Inputs/Day7.txt", ' ')

cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

class Hand(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

def add_scores(line: list) -> int:
    for x in line[0]:
        line.append(cards.index(x))

def cat_hand(hand) -> Hand:
    card_repetitions = {i: hand.count(i) for i in cards}

    if 5 in card_repetitions.values():
        return Hand.FIVE_OF_A_KIND
    elif 4 in card_repetitions.values():
        return Hand.FOUR_OF_A_KIND
    elif 3 in card_repetitions.values() and 2 in card_repetitions.values():
        return Hand.FULL_HOUSE
    elif 3 in card_repetitions.values():
        return Hand.THREE_OF_A_KIND
    elif countOf(card_repetitions.values(), 2) == 2:
        return Hand.TWO_PAIR
    elif 2 in card_repetitions.values():
        return Hand.ONE_PAIR
    else:
        return Hand.HIGH_CARD

for i, line in enumerate(lines):
    (hand, bid) = line
    if 'J' in hand:
        changedHand = hand
        max_cat = Hand.HIGH_CARD
        for x in cards:
            changedHand = hand.replace('J', x)
            if cat_hand(changedHand) > max_cat:
                max_cat = cat_hand(changedHand)
        line.append(max_cat)
    else:
        line.append(cat_hand(hand))

    add_scores(line)

lines = sorted(lines, key=itemgetter(2, 3, 4, 5, 6, 7))

final_score = 0

for i, line in enumerate(lines):
    line.append(int(line[1]) * (i + 1))
    print(f"{i + 1} - {line}")

print(sum([i[-1] for i in lines]))