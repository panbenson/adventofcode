from parser import parse_newline_delimited_array


def part_one():
    pairs = parse_newline_delimited_array(
        '2022/5-example.in', lambda e: [[int(n) for n in i.split('-')]for i in e.split(',')])
    pairs = parse_newline_delimited_array(
        '2022/5.in', lambda e: [[int(n) for n in i.split('-')]for i in e.split(',')])
    fully_overlapped = 0
    for pair in pairs:
        if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1] or\
                pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
            fully_overlapped += 1

    print(fully_overlapped)


def part_two():
    pairs = parse_newline_delimited_array(
        '2022/5-example.in', lambda e: [[int(n) for n in i.split('-')]for i in e.split(',')])
    pairs = parse_newline_delimited_array(
        '2022/5.in', lambda e: [[int(n) for n in i.split('-')]for i in e.split(',')])
    fully_overlapped = 0
    for pair in pairs:
        if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][0] or\
                pair[0][0] >= pair[1][0] and pair[0][0] <= pair[1][1]:
            fully_overlapped += 1

    print(fully_overlapped)


part_one()
part_two()
