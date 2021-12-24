# https://adventofcode.com/2021/day/17
import read_input
import heapq
from collections import defaultdict
from collections import deque


def day_seventeen(input_file):
    x_dest = [20, 30]
    y_dest = [-10, -5]
    # target area: x=60..94, y=-171..-136
    x_dest = [60, 94]
    y_dest = [-171, -136]

    # determine min dx we need, highest will always happen here
    min_dx = 0
    while sum(range(min_dx + 1)) < x_dest[0]:
        min_dx += 1

    # find the right dy
    global_max_y = 0
    global_dy = 0
    # we know when it crosses y = 0, its dy = -dy meaning dy is at most -y_dest[0]
    for i in range(-y_dest[0] + 1):
        dy = i
        dx = min_dx
        x = 0
        y = 0
        max_y = 0
        while x <= x_dest[1] and y >= y_dest[0]:
            x += dx
            y += dy
            max_y = max(max_y, y)
            if x >= x_dest[0] and x <= x_dest[1] and y >= y_dest[0] and y <= y_dest[1]:
                # hit!
                global_max_y = max(global_max_y, max_y)
                global_dy = i

            dx = max(dx - 1, 0)
            dy -= 1

    print(global_max_y, global_dy)


def day_seventeen_p2(input_file):
    x_dest = [20, 30]
    y_dest = [-10, -5]
    # target area: x=60..94, y=-171..-136
    x_dest = [60, 94]
    y_dest = [-171, -136]

    # determine min dx we need, highest will always happen here
    min_dx = 0
    while sum(range(min_dx + 1)) < x_dest[0]:
        min_dx += 1

    initial_d = []
    for n in range(min_dx, x_dest[1] + 1):
        for i in range(y_dest[0], -y_dest[0] + 1):
            dy = i
            dx = n
            x = 0
            y = 0
            while x <= x_dest[1] and y >= y_dest[0]:
                x += dx
                y += dy
                if x >= x_dest[0] and x <= x_dest[1] and y >= y_dest[0] and y <= y_dest[1]:
                    # hit!
                    initial_d.append([n, i])
                    break

                dx = max(dx - 1, 0)
                dy -= 1

    print(len(initial_d))


def main():
    input_file = '17-example.in'
    input_file = '17.in'
    day_seventeen(input_file)
    day_seventeen_p2(input_file)


main()
