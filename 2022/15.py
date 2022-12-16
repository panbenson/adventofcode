import re
from parser import parse_newline_delimited_array


def combine_ranges(ranges):
    sorted_ranges = sorted(ranges)
    curr = sorted_ranges[0]
    idx = 1
    collapsed = []

    while idx < len(sorted_ranges):
        if curr[1] >= sorted_ranges[idx][0]:
            curr = (curr[0], max(curr[1], sorted_ranges[idx][1]))
        else:
            collapsed.append(curr)
            curr = sorted_ranges[idx]

        idx += 1

    collapsed.append(curr)
    return collapsed


def part_one():
    arr = parse_newline_delimited_array(
        '2022/15-example.in', lambda e: [(int(re.search(r'x=(\-?\d+)', sb).group(1)), int(re.search(r'y=(\-?\d+)', sb).group(1))) for sb in e.split(':')])
    arr = parse_newline_delimited_array(
        '2022/15.in', lambda e: [(int(re.search(r'x=(\-?\d+)', sb).group(1)), int(re.search(r'y=(\-?\d+)', sb).group(1))) for sb in e.split(':')])
    target = 10
    target = 2000000
    ranges = []

    for sensor, beacon in arr:
        manhattan = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        to_target = abs(sensor[1] - target)

        if to_target < manhattan:
            dx = manhattan - to_target
            ranges.append((sensor[0] - dx, sensor[0] + dx))

    print(combine_ranges(ranges)[0][1] - combine_ranges(ranges)[0][0])


def part_two():
    arr = parse_newline_delimited_array(
        '2022/15-example.in', lambda e: [(int(re.search(r'x=(\-?\d+)', sb).group(1)), int(re.search(r'y=(\-?\d+)', sb).group(1))) for sb in e.split(':')])
    arr = parse_newline_delimited_array(
        '2022/15.in', lambda e: [(int(re.search(r'x=(\-?\d+)', sb).group(1)), int(re.search(r'y=(\-?\d+)', sb).group(1))) for sb in e.split(':')])
    target = 10
    target = 2000000

    # 3337613
    for target in range(4000000, 0, -1):
        if target % 10000 == 0:
            print(target)
        ranges = []
        for sensor, beacon in arr:
            manhattan = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
            to_target = abs(sensor[1] - target)

            if to_target < manhattan:
                dx = manhattan - to_target
                ranges.append((sensor[0] - dx, sensor[0] + dx))

        if len(combine_ranges(ranges)) > 1:
            print(combine_ranges(ranges))
            break


def part_two_helper():
    arr = parse_newline_delimited_array(
        '2022/15-example.in', lambda e: [(int(re.search(r'x=(\-?\d+)', sb).group(1)), int(re.search(r'y=(\-?\d+)', sb).group(1))) for sb in e.split(':')])
    arr = parse_newline_delimited_array(
        '2022/15.in', lambda e: [(int(re.search(r'x=(\-?\d+)', sb).group(1)), int(re.search(r'y=(\-?\d+)', sb).group(1))) for sb in e.split(':')])
    target = 3337614
    ranges = []
    # 2933732
    for sensor, beacon in arr:
        manhattan = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        to_target = abs(sensor[0] - target)

        if to_target < manhattan:
            dy = manhattan - to_target
            ranges.append((sensor[1] - dy, sensor[1] + dy))

    # if len(combine_ranges(ranges)) > 1:
    print(combine_ranges(ranges))


# part_one()
# part_two()
part_two_helper()
print(4000000 * 3337614 + 2933732)
