from parser import parse_raw_newline_delimited_groups
import json


def compare(left, right):
    # print('compare', left, right)
    if type(left) is int and type(right) is int:
        # right order
        if left < right:
            return 1
        # wrong order
        if left > right:
            return -1
        # no decision
        return 0
    if type(left) is list and type(right) is list:
        idx = 0
        while idx < len(left) and idx < len(right):
            decision = compare(left[idx], right[idx])

            if decision != 0:
                return decision

            idx += 1

        # no decision
        if idx >= len(left) and idx >= len(right):
            return 0
        # right order
        elif idx >= len(left):
            return 1
        else:
            return -1

    if type(left) is int and type(right) is list:
        return compare([left], right)
    if type(left) is list and type(right) is int:
        return compare(left, [right])


def part_one():
    arr = parse_raw_newline_delimited_groups(
        '2022/13-example.in', lambda e: json.loads(e) if e else None)
    arr = parse_raw_newline_delimited_groups(
        '2022/13.in', lambda e: json.loads(e) if e else None)
    # fix up the parser
    arr[-1] = arr[-1][:-1]

    sum = 0
    for idx, pair in enumerate(arr):
        left, right = pair
        if compare(left, right) == 1:
            sum += idx + 1
            # print(left, right, idx + 1)

    print(sum)


def part_two():
    arr = parse_raw_newline_delimited_groups(
        '2022/13-example.in', lambda e: json.loads(e) if e else None)
    arr = parse_raw_newline_delimited_groups(
        '2022/13.in', lambda e: json.loads(e) if e else None)
    # fix up the parser
    arr[-1] = arr[-1][:-1]

    flat_arr = []
    for pair in arr:
        flat_arr.append(pair[0])
        flat_arr.append(pair[1])

    # add the two divider packets
    flat_arr.append([[2]])
    flat_arr.append([[6]])

    # since we have a comparator to swap things, use insertion sort
    for i in range(1, len(flat_arr)):
        item = flat_arr[i]

        j = i - 1
        # shift the item down until its in the correct spot
        while j >= 0 and compare(item, flat_arr[j]) == 1:
            flat_arr[j + 1] = flat_arr[j]
            j -= 1
        flat_arr[j + 1] = item

    print((flat_arr.index([[2]]) + 1) * (flat_arr.index([[6]]) + 1))


# part_one()
part_two()
