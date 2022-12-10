from parser import parse_newline_delimited_array


def move_tail(tail_x, tail_y, head_x, head_y):
    if abs(tail_x - head_x) <= 1 and abs(tail_y - head_y) <= 1:
        return tail_x, tail_y

    if abs(tail_x - head_x) == 2 and abs(tail_y - head_y) == 0:
        return tail_x + (1 if head_x > tail_x else -1), tail_y
    elif abs(tail_x - head_x) == 0 and abs(tail_y - head_y) == 2:
        return tail_x, tail_y + (1 if head_y > tail_y else -1)
    else:
        return tail_x + (1 if head_x > tail_x else -1), tail_y + (1 if head_y > tail_y else -1)


def simulate(steps):
    visited = {}
    tail_x, tail_y = 0, 0
    head_x, head_y = 0, 0

    visited[(tail_x, tail_y)] = 1

    for step in steps:
        direction = step[0]
        for i in range(step[1]):
            if direction == 'R':
                head_x += 1
            elif direction == 'L':
                head_x -= 1
            elif direction == 'U':
                head_y += 1
            elif direction == 'D':
                head_y -= 1
            tail_x, tail_y = move_tail(tail_x, tail_y, head_x, head_y)
            visited[(tail_x, tail_y)] = 1

    print(len(visited.keys()))


def simulate_v2(steps):
    visited = {}
    rope = [[0, 0] for i in range(10)]

    visited[(0, 0)] = 1

    for step in steps:
        direction = step[0]
        for i in range(step[1]):
            if direction == 'R':
                rope[0][0] += 1
            elif direction == 'L':
                rope[0][0] -= 1
            elif direction == 'U':
                rope[0][1] += 1
            elif direction == 'D':
                rope[0][1] -= 1

            # move the segments that happen after
            for knot in range(9):
                rope[knot + 1][0], rope[knot + 1][1] = move_tail(
                    rope[knot + 1][0], rope[knot + 1][1], rope[knot][0], rope[knot][1])
            # this is the new tail
            visited[(rope[9][0], rope[9][1])] = 1

    print(len(visited.keys()))


def part_one():
    arr = parse_newline_delimited_array(
        '2022/9-example.in', lambda e: [e.split()[0], int(e.split()[1])])
    arr = parse_newline_delimited_array(
        '2022/9.in', lambda e: [e.split()[0], int(e.split()[1])])

    simulate(arr)


def part_two():
    arr = parse_newline_delimited_array(
        '2022/9-example2.in', lambda e: [e.split()[0], int(e.split()[1])])
    arr = parse_newline_delimited_array(
        '2022/9.in', lambda e: [e.split()[0], int(e.split()[1])])

    simulate_v2(arr)


# part_one()
part_two()
