from parser import parse_newline_delimited_array


def part_one():
    arr = parse_newline_delimited_array(
        '2022/18-example.in', lambda e: tuple(map(int, e.split(','))))
    arr = parse_newline_delimited_array(
        '2022/18.in', lambda e: tuple(map(int, e.split(','))))

    exposed = 0
    cubes = set(arr)
    # check all 6 sides
    for cube in arr:
        if (cube[0], cube[1], cube[2] + 1) not in cubes:
            exposed += 1
        if (cube[0], cube[1], cube[2] - 1) not in cubes:
            exposed += 1
        if (cube[0], cube[1] + 1, cube[2]) not in cubes:
            exposed += 1
        if (cube[0], cube[1] - 1, cube[2]) not in cubes:
            exposed += 1
        if (cube[0] + 1, cube[1], cube[2]) not in cubes:
            exposed += 1
        if (cube[0] - 1, cube[1], cube[2]) not in cubes:
            exposed += 1

    print(exposed)


def find_air(root, cubes, plane, traversed):
    horizon = [root]
    while len(horizon):
        curr = horizon.pop()
        traversed.add(curr)
        # dfs it
        if (curr[0], curr[1], curr[2] + 1) not in cubes and (curr[0], curr[1], curr[2] + 1) not in plane and (curr[0], curr[1], curr[2] + 1) not in traversed:
            horizon.append((curr[0], curr[1], curr[2] + 1))
        if (curr[0], curr[1], curr[2] - 1) not in cubes and (curr[0], curr[1], curr[2] - 1) not in plane and (curr[0], curr[1], curr[2] - 1) not in traversed:
            horizon.append((curr[0], curr[1], curr[2] - 1))
        if (curr[0], curr[1] + 1, curr[2]) not in cubes and (curr[0], curr[1] + 1, curr[2]) not in plane and (curr[0], curr[1] + 1, curr[2]) not in traversed:
            horizon.append((curr[0], curr[1] + 1, curr[2]))
        if (curr[0], curr[1] - 1, curr[2]) not in cubes and (curr[0], curr[1] - 1, curr[2]) not in plane and (curr[0], curr[1] - 1, curr[2]) not in traversed:
            horizon.append((curr[0], curr[1] - 1, curr[2]))
        if (curr[0] + 1, curr[1], curr[2]) not in cubes and (curr[0] + 1, curr[1], curr[2]) not in plane and (curr[0] + 1, curr[1], curr[2]) not in traversed:
            horizon.append((curr[0] + 1, curr[1], curr[2]))
        if (curr[0] - 1, curr[1], curr[2]) not in cubes and (curr[0] - 1, curr[1], curr[2]) not in plane and (curr[0] - 1, curr[1], curr[2]) not in traversed:
            horizon.append((curr[0] - 1, curr[1], curr[2]))


def borders_plane(plane, arr):
    any_borders = False
    for cube in arr:
        if (cube[0], cube[1], cube[2] + 1) in plane:
            print(cube, (cube[0], cube[1], cube[2] + 1))
            any_borders = True
            break
        if (cube[0], cube[1], cube[2] - 1) in plane:
            print(cube, (cube[0], cube[1], cube[2] - 1))
            any_borders = True
            break
        if (cube[0], cube[1] + 1, cube[2]) in plane:
            print(cube, (cube[0], cube[1] + 1, cube[2]))
            any_borders = True
            break
        if (cube[0], cube[1] - 1, cube[2]) in plane:
            print(cube, (cube[0], cube[1] - 1, cube[2]))
            any_borders = True
            break
        if (cube[0] + 1, cube[1], cube[2]) in plane:
            print(cube, (cube[0] + 1, cube[1], cube[2]))
            any_borders = True
            break
        if (cube[0] - 1, cube[1], cube[2]) in plane:
            print(cube, (cube[0] - 1, cube[1], cube[2]))
            any_borders = True
            break

    return any_borders


def part_two():
    arr = parse_newline_delimited_array(
        '2022/18-example.in', lambda e: tuple(map(int, e.split(','))))
    arr = parse_newline_delimited_array(
        '2022/18.in', lambda e: tuple(map(int, e.split(','))))

    exposed = 0
    cubes = set(arr)
    min_x = min([cube[0] for cube in arr]) - 1
    max_x = max([cube[0] for cube in arr]) + 1
    min_y = min([cube[1] for cube in arr]) - 1
    max_y = max([cube[1] for cube in arr]) + 1
    min_z = min([cube[2] for cube in arr]) - 1
    max_z = max([cube[2] for cube in arr]) + 1

    # check all 6 sides
    for cube in arr:
        if (cube[0], cube[1], cube[2] + 1) not in cubes:
            exposed += 1
        if (cube[0], cube[1], cube[2] - 1) not in cubes:
            exposed += 1
        if (cube[0], cube[1] + 1, cube[2]) not in cubes:
            exposed += 1
        if (cube[0], cube[1] - 1, cube[2]) not in cubes:
            exposed += 1
        if (cube[0] + 1, cube[1], cube[2]) not in cubes:
            exposed += 1
        if (cube[0] - 1, cube[1], cube[2]) not in cubes:
            exposed += 1

    plane = set()
    # x planes
    for z in range(min_z, max_z + 1):
        for y in range(min_y, max_y + 1):
            plane.add((min_x, y, z))
            plane.add((max_x, y, z))
    # y planes
    for z in range(min_z, max_z + 1):
        for x in range(min_x, max_x + 1):
            plane.add((x, min_y, z))
            plane.add((x, max_y, z))
    # z planes
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            plane.add((x, y, min_z))
            plane.add((x, y, max_z))

    external_cube = cubes.copy()
    air = set()
    # find air pockets
    for z in range(min_z + 1, max_z):
        for y in range(min_y + 1, max_y):
            for x in range(min_x + 1, max_x):
                if (x, y, z) in external_cube:
                    continue
                traversed = set()
                find_air((x, y, z), external_cube, plane, traversed)
                if borders_plane(plane, list(traversed)):
                    # set all in external cube
                    for cube in traversed:
                        external_cube.add(cube)
                else:
                    # set all in air
                    for cube in traversed:
                        air.add(cube)

    for cube in list(air):
        if (cube[0], cube[1], cube[2] + 1) in external_cube:
            exposed -= 1
        if (cube[0], cube[1], cube[2] - 1) in external_cube:
            exposed -= 1
        if (cube[0], cube[1] + 1, cube[2]) in external_cube:
            exposed -= 1
        if (cube[0], cube[1] - 1, cube[2]) in external_cube:
            exposed -= 1
        if (cube[0] + 1, cube[1], cube[2]) in external_cube:
            exposed -= 1
        if (cube[0] - 1, cube[1], cube[2]) in external_cube:
            exposed -= 1

    print(exposed)


# part_one()
part_two()
