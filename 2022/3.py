from parser import parse_newline_delimited_array, parse_newline_delimited_array_in_groups_of


def part_one():
    rucksacks = parse_newline_delimited_array(
        '2022/3-example.in', lambda e: [e[:len(e)//2], e[len(e)//2:]])
    rucksacks = parse_newline_delimited_array(
        '2022/3.in', lambda e: [e[:len(e)//2], e[len(e)//2:]])
    sum = 0
    for bag in rucksacks:
        repeated = list(set(bag[0]).intersection(set(bag[1])))[0]
        print(set(bag[0]).intersection(set(bag[1])))
        priority = ord(repeated) - \
            ord('A') + 27 if repeated <= 'Z' else ord(repeated) - ord('a') + 1
        print(priority)
        sum += priority

    print(sum)


def part_two():
    groups = parse_newline_delimited_array_in_groups_of(
        '2022/3-example.in', lambda e: e, 3)
    groups = parse_newline_delimited_array_in_groups_of(
        '2022/3.in', lambda e: e, 3)

    sum = 0
    for bags in groups:
        repeated = list(set(bags[0]).intersection(
            set(bags[1])).intersection(set(bags[2])))[0]
        priority = ord(repeated) - \
            ord('A') + 27 if repeated <= 'Z' else ord(repeated) - ord('a') + 1
        sum += priority

    print(sum)


# part_one()
part_two()
