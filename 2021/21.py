# https://adventofcode.com/2021/day/21
import read_input
import heapq
import math
from collections import defaultdict
from collections import deque
from itertools import permutations
import json


def day_twenty_one(input_file):
    lines = read_input.parse_lines(input_file)
    p1, p2 = [int(line.split(': ')[1]) for line in lines]
    p1_score = 0
    p2_score = 0
    rolls = 0
    die = 1
    p1_goes = True
    print(f"Player 1 starting at {p1}")
    print(f"Player 2 starting at {p2}")
    while p1_score < 1000 and p2_score < 1000:
        roll1 = die
        roll2 = (die + 1) // 101 + (die + 1) % 101
        roll3 = (die + 2) % 101 + (die + 2) // 101
        steps = roll1 + roll2 + roll3
        if p1_goes:
            p1 = (p1 + steps) % 10 if (p1 + steps) % 10 > 0 else 10
            p1_score += p1
        else:
            p2 = (p2 + steps) % 10 if (p2 + steps) % 10 > 0 else 10
            p2_score += p2

        print(f"Player {'1' if p1_goes else '2'} rolls {roll1}+{roll2}+{roll3} and moves to space {p1 if p1_goes else p2} for a total score of {p1_score if p1_goes else p2_score}.")
        die = (die + 3) % 101 + (die + 3) // 101
        rolls += 3
        p1_goes = not p1_goes

    if p1_score >= 1000:
        print(p2_score * rolls)
    else:
        print(p1_score * rolls)


def day_twenty_one_p2(input_file):
    pass


def main():
    input_file = '21-example.in'
    input_file = '21.in'
    # 657120 too low
    day_twenty_one(input_file)
    day_twenty_one_p2(input_file)


main()
