from parser import parse_raw_newline_delimited_groups
import re
from collections import defaultdict


def part_one():
    arr = parse_raw_newline_delimited_groups(
        '2022/5-example.in', lambda e: str(e))
    arr = parse_raw_newline_delimited_groups(
        '2022/5.in', lambda e: str(e))

    # construct the stacks
    stacks = defaultdict(lambda: [])
    for row in reversed(arr[0][:-1]):
        print(row)
        for i in range(1, len(arr[0][0]), 4):
            if row[i] != ' ':
                stacks[i // 4 + 1].append(row[i])

    for move in arr[1]:
        match = re.search("move (\d+) from (\d+) to (\d+)", move)
        containers = int(match.group(1))
        from_idx = int(match.group(2))
        to_idx = int(match.group(3))

        for i in range(containers):
            stacks[to_idx].append(stacks[from_idx].pop())

        print(stacks)

    print("".join([a[-1] for a in stacks.values()]))


def part_two():
    arr = parse_raw_newline_delimited_groups(
        '2022/5-example.in', lambda e: str(e))
    arr = parse_raw_newline_delimited_groups(
        '2022/5.in', lambda e: str(e))

    # construct the stacks
    stacks = defaultdict(lambda: [])
    for row in reversed(arr[0][:-1]):
        print(row)
        for i in range(1, len(arr[0][0]), 4):
            if row[i] != ' ':
                stacks[i // 4 + 1].append(row[i])

    for move in arr[1]:
        match = re.search("move (\d+) from (\d+) to (\d+)", move)
        containers = int(match.group(1))
        from_idx = int(match.group(2))
        to_idx = int(match.group(3))

        temp = stacks[from_idx][-1 * containers:]
        stacks[from_idx] = stacks[from_idx][:-1 * containers]
        stacks[to_idx] += temp

        print(stacks)

    print("".join([a[-1] for a in stacks.values()]))


# part_one()
part_two()
