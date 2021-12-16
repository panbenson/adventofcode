# https://adventofcode.com/2021/day/13
import read_input
from collections import defaultdict
from collections import deque


def day_thirteen(input_file):
    lines = read_input.parse_lines(input_file)

    total = 0
    parsed_dots = False
    dots = []
    folds = []
    for line in lines:
        if line == '':
            parsed_dots = True
            continue
        if not parsed_dots:
            dots.append([int(val) for val in line.split(',')])
        else:
            folds.append((line.split(' ')[2]).split('='))

    for fold in folds:
        axis, value = fold
        fold_idx = int(value)

        # fold the paper
        for idx, dot in enumerate(dots):
            x, y = dot
            if axis == 'y' and y > fold_idx:
                dots[idx] = [x, fold_idx - (y - fold_idx)]
            if axis == 'x' and x > fold_idx:
                dots[idx] = [fold_idx - (x - fold_idx), y]

    max_x = max([x for x, y in dots])
    max_y = max([y for x, y in dots])
    grid = [['.' for i in range(max_x + 1)] for n in range(max_y + 1)]
    for dot in dots:
        x, y = dot
        if grid[y][x] == '.':
            total += 1
        grid[y][x] = '#'

    print(total)


def day_thirteen_p2(input_file):
    lines = read_input.parse_lines(input_file)

    total = 0
    parsed_dots = False
    dots = []
    folds = []
    for line in lines:
        if line == '':
            print('ok')
            parsed_dots = True
            continue
        if not parsed_dots:
            dots.append([int(val) for val in line.split(',')])
        else:
            folds.append((line.split(' ')[2]).split('='))

    for fold in folds:
        axis, value = fold
        fold_idx = int(value)

        # fold the paper
        for idx, dot in enumerate(dots):
            x, y = dot
            if axis == 'y' and y > fold_idx:
                dots[idx] = [x, fold_idx - (y - fold_idx)]
            if axis == 'x' and x > fold_idx:
                dots[idx] = [fold_idx - (x - fold_idx), y]

    max_x = max([x for x, y in dots])
    max_y = max([y for x, y in dots])
    grid = [['.' for i in range(max_x + 1)] for n in range(max_y + 1)]
    for dot in dots:
        x, y = dot
        if grid[y][x] == '.':
            total += 1
        grid[y][x] = '#'

    print('\n'.join([' '.join(row) for row in grid]))


def main():
    # input_file = '13-example.in'
    input_file = '13.in'
    day_thirteen(input_file)
    day_thirteen_p2(input_file)


main()
