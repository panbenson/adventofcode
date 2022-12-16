from parser import parse_newline_delimited_array


def get_rock_set(paths):
    rocks = set()

    # rock paths only go horizonally or vertically
    for path in paths:
        start = path[0]
        for next in path[1:]:
            # x coordinate the same, vertical line
            if start[0] == next[0]:
                for y in range(min(start[1], next[1]), max(start[1], next[1]) + 1):
                    rocks.add((start[0], y))
            # horizontal line
            else:
                for x in range(min(start[0], next[0]), max(start[0], next[0]) + 1):
                    rocks.add((x, start[1]))

            start = next

    return rocks


def simulate(rocks, start, lowest):
    rest = set()

    while True:
        sand = start
        while (sand[1] < lowest):
            down = (sand[0], sand[1] + 1)
            down_left = (sand[0] - 1, sand[1] + 1)
            down_right = (sand[0] + 1, sand[1] + 1)

            # move down
            if down not in rocks and down not in rest:
                sand = down
            # down left
            elif down_left not in rocks and down_left not in rest:
                sand = down_left
            # down right
            elif down_right not in rocks and down_right not in rest:
                sand = down_right
            else:
                rest.add(sand)
                break

        if sand[1] >= lowest:
            break

        # part_two: if we've blocked the start
        if start in rest:
            break

    print(len(rest))


def part_one():
    paths = parse_newline_delimited_array(
        '2022/14-example.in', lambda e: [list(map(int, x.split(',')))for x in e.split(' -> ')])
    paths = parse_newline_delimited_array(
        '2022/14.in', lambda e: [list(map(int, x.split(',')))for x in e.split(' -> ')])
    rocks = get_rock_set(paths)
    print(rocks)
    # find the lowest rocks
    lowest = max([y for x, y in rocks])
    print(lowest)

    # sand starts falling at 500,0
    simulate(rocks, (500, 0), lowest)


def part_two():
    paths = parse_newline_delimited_array(
        '2022/14-example.in', lambda e: [list(map(int, x.split(',')))for x in e.split(' -> ')])
    paths = parse_newline_delimited_array(
        '2022/14.in', lambda e: [list(map(int, x.split(',')))for x in e.split(' -> ')])
    rocks = get_rock_set(paths)

    # find the lowest rocks
    lowest = max([y for x, y in rocks])

    # just add a really long horizontal line at lowest + 2
    for i in range(-1000, 1000):
        rocks.add((i, lowest + 2))

    # sand starts falling at 500,0
    simulate(rocks, (500, 0), lowest + 2)


# part_one()
part_two()
