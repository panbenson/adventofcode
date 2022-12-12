from parser import parse_newline_delimited_array
from collections import deque


def part_one():
    arr = parse_newline_delimited_array(
        '2022/10-example.in', lambda e: e.split())
    arr = parse_newline_delimited_array(
        '2022/10.in', lambda e: e.split())

    interesting_signals = [20 + i * 40 for i in range(6)]
    cycle = 1
    x = 1
    total = 0
    for command in arr:
        # addx command
        if len(command) > 1:
            for i in range(2):
                # just keep it simple, check total here too
                if cycle in interesting_signals:
                    total += cycle * x
                cycle += 1
            x += int(command[1])
            print(f'cycle: {cycle}, x: {x}')
        else:
            print(f'cycle: {cycle}, x: {x}')
            cycle += 1

    print(total)


def part_two():
    arr = parse_newline_delimited_array(
        '2022/10-example.in', lambda e: e.split())
    arr = parse_newline_delimited_array(
        '2022/10.in', lambda e: e.split())

    crt = ''
    cycle = 1
    x = 1
    total = 0
    for command in arr:
        # addx command
        if len(command) > 1:
            for i in range(2):
                if abs(x - ((cycle - 1) % 40)) <= 1:
                    crt += '#'
                else:
                    crt += '.'
                cycle += 1
            x += int(command[1])
            print(f'cycle: {cycle + 1}, x: {x}')
        else:
            if abs(x - ((cycle - 1) % 40)) <= 1:
                crt += '#'
            else:
                crt += '.'
            print(f'cycle: {cycle + 1}, x: {x}')
            cycle += 1

    for i in range(6):
        print(crt[i * 40:(i + 1) * 40])


# part_one()
part_two()
