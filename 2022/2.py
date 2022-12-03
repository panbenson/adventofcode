from parser import parse_space_delimited_arrays


def part_one():
    total_score = 0
    rounds = parse_space_delimited_arrays(
        '2022/2-example.in', lambda e: str(e))
    rounds = parse_space_delimited_arrays(
        '2022/2.in', lambda e: str(e))
    # A = rock, b = paper, c = scissors
    # we are second index, X rock = 1, Y paper = 2, z scissors = 3
    # outcome loss = 0, tie = 3, win = 6
    for you, me in rounds:
        # rock
        if me == 'X':
            total_score += 1
            if you == 'A':
                total_score += 3
            elif you == 'C':
                total_score += 6
        if me == 'Y':
            total_score += 2
            if you == 'B':
                total_score += 3
            elif you == 'A':
                total_score += 6
        if me == 'Z':
            total_score += 3
            if you == 'C':
                total_score += 3
            elif you == 'B':
                total_score += 6

    # print(rounds)
    print(total_score)


def part_two():
    total_score = 0
    rounds = parse_space_delimited_arrays(
        '2022/2-example.in', lambda e: str(e))
    rounds = parse_space_delimited_arrays(
        '2022/2.in', lambda e: str(e))
    # A = rock, b = paper, c = scissors
    # we are second index, X rock = 1, Y paper = 2, z scissors = 3
    # outcome loss = 0, tie = 3, win = 6
    for you, me in rounds:
        # need to lose
        if me == 'X':
            if you == 'A':
                total_score += 3
            elif you == 'B':
                total_score += 1
            elif you == 'C':
                total_score += 2
        # need to draw
        if me == 'Y':
            if you == 'B':
                total_score += 2 + 3
            elif you == 'A':
                total_score += 1 + 3
            elif you == 'C':
                total_score += 3 + 3
        # need to win
        if me == 'Z':
            if you == 'A':
                total_score += 2 + 6
            elif you == 'B':
                total_score += 3 + 6
            elif you == 'C':
                total_score += 1 + 6

    # print(rounds)
    print(total_score)


# part_one()
part_two()
