from parser import parse_newline_delimited_arrays


def part_one():
    # elves = parse_newline_delimited_arrays('2022/1-example.in', lambda e: int(e))
    elves = parse_newline_delimited_arrays('2022/1.in', lambda e: int(e))

    # sum each group
    elves_total = map(lambda x: sum(x), elves)
    print(max(elves_total))


def part_two():
    elves = parse_newline_delimited_arrays(
        '2022/1-example.in', lambda e: int(e))
    elves = parse_newline_delimited_arrays('2022/1.in', lambda e: int(e))

    # sum each group
    elves_total = map(lambda x: sum(x), elves)
    sorted_total = sorted(elves_total, reverse=True)
    print(sum(sorted_total[:3]))


# part_one()
part_two()
