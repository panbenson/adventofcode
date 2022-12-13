from parser import parse_newline_delimited_array
from collections import deque


def find_char(arr, char):
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col] == char:
                return (col, row)


def find_chars(arr, char):
    chars = []
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col] == char:
                chars.append((col, row))
    return chars


def part_one():
    arr = parse_newline_delimited_array(
        '2022/12-example.in', lambda e: list(e))
    arr = parse_newline_delimited_array(
        '2022/12.in', lambda e: list(e))
    start = find_char(arr, 'S')
    end = find_char(arr, 'E')
    # make things easier
    arr[start[1]][start[0]] = 'a'
    arr[end[1]][end[0]] = 'z'
    horizon = deque([(start, 0)])

    costs = [[float('Inf') for i in range(len(arr[0]))]
             for n in range(len(arr))]

    def traverseable(new_x, new_y, prev_x, prev_y):
        return ord(arr[new_y][new_x]) - ord(arr[prev_y][prev_x]) <= 1

    while len(horizon):
        (x, y), cost = horizon.popleft()
        new_cost = cost + 1
        print(x, y)

        if x == end[0] and y == end[1]:
            print(cost)
            break

        if x - 1 >= 0 and traverseable(x - 1, y, x, y) and new_cost < costs[y][x - 1]:
            horizon.append(((x - 1, y), new_cost))
            costs[y][x - 1] = new_cost
        if x + 1 < len(arr[0]) and traverseable(x + 1, y, x, y) and new_cost < costs[y][x + 1]:
            horizon.append(((x + 1, y), new_cost))
            costs[y][x + 1] = new_cost
        if y - 1 >= 0 and traverseable(x, y - 1, x, y) and new_cost < costs[y - 1][x]:
            horizon.append(((x, y - 1), new_cost))
            costs[y - 1][x] = new_cost
        if y + 1 < len(arr) and traverseable(x, y + 1, x, y) and new_cost < costs[y + 1][x]:
            horizon.append(((x, y + 1), new_cost))
            costs[y + 1][x] = new_cost


def part_two():
    arr = parse_newline_delimited_array(
        '2022/12-example.in', lambda e: list(e))
    arr = parse_newline_delimited_array(
        '2022/12.in', lambda e: list(e))
    start = find_char(arr, 'S')
    end = find_char(arr, 'E')
    # make things easier
    arr[start[1]][start[0]] = 'a'
    arr[end[1]][end[0]] = 'z'

    def traverseable(new_x, new_y, prev_x, prev_y):
        return ord(arr[new_y][new_x]) - ord(arr[prev_y][prev_x]) <= 1

    starting_points = find_chars(arr, 'a')
    lowest_cost = float('Inf')
    # if we built the "chain" we could have just return the first 'a'
    # but i guess bruce force works too
    for starting_point in starting_points:
        start = starting_point

        horizon = deque([(start, 0)])

        costs = [[float('Inf') for i in range(len(arr[0]))]
                 for n in range(len(arr))]

        while len(horizon):
            (x, y), cost = horizon.popleft()
            new_cost = cost + 1

            if x == end[0] and y == end[1]:
                lowest_cost = min(lowest_cost, cost)
                break

            if x - 1 >= 0 and traverseable(x - 1, y, x, y) and new_cost < costs[y][x - 1]:
                horizon.append(((x - 1, y), new_cost))
                costs[y][x - 1] = new_cost
            if x + 1 < len(arr[0]) and traverseable(x + 1, y, x, y) and new_cost < costs[y][x + 1]:
                horizon.append(((x + 1, y), new_cost))
                costs[y][x + 1] = new_cost
            if y - 1 >= 0 and traverseable(x, y - 1, x, y) and new_cost < costs[y - 1][x]:
                horizon.append(((x, y - 1), new_cost))
                costs[y - 1][x] = new_cost
            if y + 1 < len(arr) and traverseable(x, y + 1, x, y) and new_cost < costs[y + 1][x]:
                horizon.append(((x, y + 1), new_cost))
                costs[y + 1][x] = new_cost

    print(lowest_cost)


# part_one()
part_two()
