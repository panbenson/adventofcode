from collections import defaultdict
import copy
import sys
import re
import math

word = 'XMAS'

def search(word_search, x, y):
    matches = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue

            valid_x = x + dx * (len(word) - 1) >=0 and x + dx * (len(word) - 1) < len(word_search[0])
            valid_y = y + dy * (len(word) - 1) >=0 and y + dy * (len(word) - 1) < len(word_search)
            if valid_x and valid_y:
                selected_word = ''
                for i in range(len(word)):
                    selected_word += word_search[y + dy * i][x + dx * i]

                if selected_word == word:
                    print(f"({x}, {y}) in ({dx}, {dy}) direction")
                    matches += 1
    return matches

def day_4_1():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        word_search = list(map(lambda line: list(line.strip()), file.readlines()))
        total = 0
        for y in range(len(word_search)):
            for x in range(len(word_search[0])):
                if word_search[y][x] == 'X':
                    total += search(word_search, x, y)

        print(total)


def search_xmas(word_search, x, y):
    valid_x = x - 1 >=0 and x + 1 < len(word_search[0])
    valid_y = y - 1 >=0 and y + 1 < len(word_search)
    if valid_x and valid_y:
        if (word_search[y - 1][x - 1] == 'M' and word_search[y + 1][x + 1] == 'S' or \
            word_search[y - 1][x - 1] == 'S' and word_search[y + 1][x + 1] == 'M') and \
            (word_search[y - 1][x + 1] == 'M' and word_search[y + 1][x - 1] == 'S' or \
            word_search[y - 1][x + 1] == 'S' and word_search[y + 1][x - 1] == 'M'):
            return 1
    return 0


def day_4_2():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        word_search = list(map(lambda line: list(line.strip()), file.readlines()))
        total = 0
        for y in range(len(word_search)):
            for x in range(len(word_search[0])):
                if word_search[y][x] == 'A':
                    total += search_xmas(word_search, x, y)

        print(total)


# day_4_1()
day_4_2()
