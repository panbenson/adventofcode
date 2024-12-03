from parser import parse_newline_delimited_array


def parse_operation(e):
    parts = e.split(': ')
    if '+' in parts[1] or '-' in parts[1] or '*' in parts[1] or '/' in parts[1]:
        return (parts[0], parts[1].split())
    else:
        return (parts[0], int(parts[1]))


def calculate(monkeys, monkey):
    value = monkeys[monkey]
    if type(value) is int:
        return value
    else:
        if value[1] == '+':
            return calculate(monkeys, value[0]) + calculate(monkeys, value[2])
        elif value[1] == '-':
            return calculate(monkeys, value[0]) - calculate(monkeys, value[2])
        elif value[1] == '*':
            return calculate(monkeys, value[0]) * calculate(monkeys, value[2])
        else:
            return calculate(monkeys, value[0]) / calculate(monkeys, value[2])


def calculate_you(monkeys, monkey, you):
    value = monkeys[monkey]
    if monkey == 'humn':
        return you
    if type(value) is int:
        return value
    else:
        if value[1] == '+':
            return calculate_you(monkeys, value[0], you) + calculate_you(monkeys, value[2], you)
        elif value[1] == '-':
            return calculate_you(monkeys, value[0], you) - calculate_you(monkeys, value[2], you)
        elif value[1] == '*':
            return calculate_you(monkeys, value[0], you) * calculate_you(monkeys, value[2], you)
        else:
            return calculate_you(monkeys, value[0], you) / calculate_you(monkeys, value[2], you)


def calc_to_string(monkeys, monkey):
    value = monkeys[monkey]
    if monkey == 'humn':
        return 'you'
    if type(value) is int:
        return value
    else:
        a = calc_to_string(monkeys, value[0])
        b = calc_to_string(monkeys, value[2])
        if value[1] == '+':
            if type(a) is int and type(b) is int:
                return a + b
            else:
                return f'({a} + {b})'
        elif value[1] == '-':
            if type(a) is int and type(b) is int:
                return a - b
            else:
                return f'({a} - {b})'
        elif value[1] == '*':
            if type(a) is int and type(b) is int:
                return a * b
            else:
                return f'({a} * {b})'
        else:
            if type(a) is int and type(b) is int:
                return a / b
            else:
                return f'({a} / {b})'


def part_one():
    arr = parse_newline_delimited_array(
        '2022/21-example.in', parse_operation)
    arr = parse_newline_delimited_array(
        '2022/21.in', parse_operation)

    monkeys_dict = {m[0]: m[1] for m in arr}

    print(calculate(monkeys_dict, 'root'))


def part_two():
    arr = parse_newline_delimited_array(
        '2022/21-example.in', parse_operation)
    # arr = parse_newline_delimited_array(
    #     '2022/21.in', parse_operation)

    monkeys_dict = {m[0]: m[1] for m in arr}

    # lets binary search it, +/- 1000000
    min = -1000000000000000000000
    max = 1000000000000000000000

    a = 1
    b = 0

    i = 0
    while a != b:
        print(a, b)
        mid = (min + max) // 2
        a = calculate_you(
            monkeys_dict, monkeys_dict['root'][0], mid)
        b = calculate_you(
            monkeys_dict, monkeys_dict['root'][2], mid)

        if a == b:
            print(mid)
        elif a > b:
            min = mid
        else:
            max = mid
        i += 1


# part_one()
part_two()
