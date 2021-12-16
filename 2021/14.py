# https://adventofcode.com/2021/day/14
import read_input
from collections import defaultdict
from collections import deque


def day_fourteen(input_file):
    lines = read_input.parse_lines(input_file)

    total = 0
    parse_break = False
    pairs = []
    polymer = ''
    for line in lines:
        if line == '':
            parse_break = True
            continue
        if parse_break:
            pairs.append(line.split(' -> '))
        else:
            polymer = line

    steps = 10

    for step in range(steps):
        new_polymer = polymer[0]
        counts = defaultdict(int)

        for i in range(len(polymer) - 1):
            chunk = polymer[i: i + 2]
            for pair in pairs:
                s, add = pair
                if chunk == s:
                    new_polymer += add + s[1]
                    break
        polymer = new_polymer

    counts = defaultdict(int)
    for i in polymer:
        counts[i] += 1

    print(max(counts.values()) - min(counts.values()))


def day_fourteen_p2(input_file):
    lines = read_input.parse_lines(input_file)

    parse_break = False
    pairs = {}
    polymer = ''
    for line in lines:
        if line == '':
            parse_break = True
            continue
        if parse_break:
            chunk, add = line.split(' -> ')
            pairs[chunk] = add
        else:
            polymer = line

    steps = 40
    counts = defaultdict(int)
    letter_counts = defaultdict(int)

    for i in polymer:
        letter_counts[i] += 1

    for i in range(len(polymer) - 1):
        chunk = polymer[i: i + 2]
        counts[chunk] += 1

    for step in range(steps):
        new_polymer = counts.copy()

        for chunk in counts.keys():
            first_new = chunk[0] + pairs[chunk]
            second_new = pairs[chunk] + chunk[1]

            letter_counts[pairs[chunk]] += counts[chunk]
            new_polymer[first_new] += counts[chunk]
            new_polymer[second_new] += counts[chunk]
            new_polymer[chunk] = max(new_polymer[chunk] - counts[chunk], 0)

        counts = new_polymer

    print(max(letter_counts.values()) - min(letter_counts.values()))


def main():
    # input_file = '14-example.in'
    input_file = '14.in'
    day_fourteen(input_file)
    day_fourteen_p2(input_file)


main()
