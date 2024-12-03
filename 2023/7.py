from collections import defaultdict
import sys
import re
import math


def count_cards(hand):
    cards = defaultdict(int)
    for char in hand:
        cards[char] += 1

    return cards


def char_to_int(char):
    if char == 'A':
        return 0
    elif char == 'K':
        return 1
    elif char == 'Q':
        return 2
    elif char == 'J':
        return 3
    elif char == 'T':
        return 4
    else:
        return 5 + ord('9') - ord(char)


def hand_to_tuple(hand):
    return tuple(char_to_int(char) for char in hand)


def cards_to_type(cards):
    if 5 in cards.values():
        return 1
    elif 4 in cards.values():
        return 2
    elif 3 in cards.values() and 2 in cards.values():
        return 3
    elif 3 in cards.values():
        return 4
    elif list(cards.values()).count(2) == 2:
        return 5
    elif 2 in cards.values():
        return 6
    else:
        return 7


def day_7_1():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        lines = file.readlines()
        hands = [[line.split()[0], int(line.split()[1])] for line in lines]
        print(hands)

        sorted_hands = []
        for hand, bid in hands:
            cards = count_cards(hand)
            sorted_hands.append((cards_to_type(cards), hand_to_tuple(hand), hand, bid))

        sorted_hands = sorted(sorted_hands)
        sorted_hands.reverse()

        print(sum([(i + 1) * sorted_hands[i][3] for i in range(len(sorted_hands))]))



def char_to_int_2(char):
    if char == 'A':
        return 0
    elif char == 'K':
        return 1
    elif char == 'Q':
        return 2
    elif char == 'J':
        return 30
    elif char == 'T':
        return 4
    else:
        return 5 + ord('9') - ord(char)
    

def hand_to_tuple_2(hand):
    return tuple(char_to_int_2(char) for char in hand)


def get_wildcard_value(hand):
    cards = count_cards(hand)
    if 'J' in cards:
        sorted_cards = sorted([(count, -1 * char_to_int_2(card), card) for card, count in cards.items()])
        sorted_cards.reverse()
        if sorted_cards[0][2] != 'J':
            cards[sorted_cards[0][2]] += cards['J']
            del cards['J']
        elif len(sorted_cards) > 1:
            cards[sorted_cards[1][2]] += cards['J']
            del cards['J']
    
    return cards_to_type(cards)


def day_7_2():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        lines = file.readlines()
        hands = [[line.split()[0], int(line.split()[1])] for line in lines]

        sorted_hands = []
        for hand, bid in hands:
            sorted_hands.append((get_wildcard_value(hand), hand_to_tuple_2(hand), hand, bid))

        sorted_hands = sorted(sorted_hands)
        sorted_hands.reverse()
        # print(sorted_hands)

        print(sum([(i + 1) * sorted_hands[i][3] for i in range(len(sorted_hands))]))


day_7_2()
