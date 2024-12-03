from parser import parse_newline_delimited_array


def get_rock(rock_num, top):
    rock_type = rock_num % 5

    # 2 from left, 3 from the top
    from_top = top + 3 + 1
    if rock_type == 0:
        return [(i, from_top) for i in range(2, 2 + 4)]
    elif rock_type == 1:
        return [(i, from_top + 1) for i in range(2, 2 + 3)] + [(3, from_top), (3, from_top + 2)]
    elif rock_type == 2:
        return [(i, from_top) for i in range(2, 2 + 3)] + [(2 + 2, i) for i in range(from_top + 1, from_top + 3)]
    elif rock_type == 3:
        return [(2, i) for i in range(from_top, from_top + 4)]
    elif rock_type == 4:
        return [(i, from_top) for i in range(2, 2 + 2)] + [(i, from_top + 1) for i in range(2, 2 + 2)]


def valid(chamber, rock):
    # check if outside of walls
    for i in rock:
        if i[0] >= 7 or i[0] < 0 or i in chamber:
            return False

    return True


def part_one():
    arr = parse_newline_delimited_array(
        '2022/17-example.in', lambda e: list(e))[0]
    arr = parse_newline_delimited_array(
        '2022/17.in', lambda e: list(e))[0]
    # the chamber is 7 wide
    # rocks appear left edge 2 from the left wall, 3 above prev highest

    # gets pushed 1 unit by arrow then falls 1 unit down
    # If any movement would cause any part of the rock to move into the walls, floor, or a stopped rock, the movement instead does not occur.
    # if we fall onto stopped item, stop and move to next rock

    print(arr)

    # chamber grows upwards, starting at 0,0
    chamber = set([(i, 0) for i in range(7)])

    rock_num = 0
    top = 0
    move = 0
    while rock_num < 2022:
        rock = get_rock(rock_num, top)
        # print(rock)
        falling = True

        while move < len(arr) and falling:
            if arr[move] == '>':
                # print('right')
                moved_rock = [(i[0] + 1, i[1]) for i in rock]
                if valid(chamber, moved_rock):
                    rock = moved_rock
                # else:
                #     print('nothing happens')
            else:
                # print('left')
                moved_rock = [(i[0] - 1, i[1]) for i in rock]
                if valid(chamber, moved_rock):
                    rock = moved_rock
                # else:
                #     print('nothing happens')

            # fall down
            moved_rock = [(i[0], i[1] - 1) for i in rock]
            if valid(chamber, moved_rock):
                # print('down')
                rock = moved_rock
            else:
                falling = False

            move = (move + 1) % len(arr)

        for i in rock:
            chamber.add(i)
        top = max([i[1] for i in rock] + [top])

        if rock == 1:
            break
        rock_num += 1

    lines = []
    for y in range(18):
        row = ''
        for x in range(7):
            if (x, y) in chamber:
                row += '#'
            else:
                row += '.'
        lines = [row] + lines
    # print('\n'.join(lines))

    print(top)


def part_two():
    arr = parse_newline_delimited_array(
        '2022/17-example.in', lambda e: list(e))[0]
    # arr = parse_newline_delimited_array(
    #     '2022/17.in', lambda e: list(e))[0]
    # the chamber is 7 wide
    # rocks appear left edge 2 from the left wall, 3 above prev highest

    # gets pushed 1 unit by arrow then falls 1 unit down
    # If any movement would cause any part of the rock to move into the walls, floor, or a stopped rock, the movement instead does not occur.
    # if we fall onto stopped item, stop and move to next rock

    print(arr)

    # chamber grows upwards, starting at 0,0
    chamber = set([(i, 0) for i in range(7)])

    rock_num = 0
    top = 0
    move = 0
    while rock_num < 1000000000000:
        if rock_num % 10000000000 == 0:
            print('1/1000')
        rock = get_rock(rock_num, top)
        # print(rock)
        falling = True

        while move < len(arr) and falling:
            if arr[move] == '>':
                # print('right')
                moved_rock = [(i[0] + 1, i[1]) for i in rock]
                if valid(chamber, moved_rock):
                    rock = moved_rock
                # else:
                #     print('nothing happens')
            else:
                # print('left')
                moved_rock = [(i[0] - 1, i[1]) for i in rock]
                if valid(chamber, moved_rock):
                    rock = moved_rock
                # else:
                #     print('nothing happens')

            # fall down
            moved_rock = [(i[0], i[1] - 1) for i in rock]
            if valid(chamber, moved_rock):
                # print('down')
                rock = moved_rock
            else:
                falling = False

            move = (move + 1) % len(arr)

        for i in rock:
            chamber.add(i)
        top = max([i[1] for i in rock] + [top])

        if rock == 1:
            break
        rock_num += 1

    lines = []
    for y in range(18):
        row = ''
        for x in range(7):
            if (x, y) in chamber:
                row += '#'
            else:
                row += '.'
        lines = [row] + lines
    # print('\n'.join(lines))

    print(top)


# part_one()
part_two()
