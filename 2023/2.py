from collections import defaultdict
import sys
import re

def day_2_1():
    input_file = sys.argv[1]

    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    with open(input_file, 'r') as file:
        sum = 0
        for line in file:
            text = line.strip()
            match = re.search(r"Game (\d+): (.*)", text)
            game_num = int(match.group(1))
            games = match.group(2).split('; ')

            for game in games:
                cubes = game.split(', ')
                game_cubes = defaultdict(int)
                possible = True

                # enumerate cubes used in a game
                for cube in cubes:
                    num_cubes, color = cube.split(' ')
                    game_cubes[color] = int(num_cubes)

                # check if it exceeds max_cubes
                for max_cube in max_cubes:
                    if game_cubes[max_cube] > max_cubes[max_cube]:
                        possible = False

                # exit early
                if not possible:
                    break

            if possible:
                sum += game_num

    print(f"sum: {sum}")


def day_2_2():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        sum = 0
        for line in file:
            text = line.strip()
            match = re.search(r"Game (\d+): (.*)", text)
            games = match.group(2).split('; ')
            max_cubes = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }

            for game in games:
                cubes = game.split(', ')
                game_cubes = defaultdict(int)
                possible = True

                # enumerate cubes used in a game
                for cube in cubes:
                    num_cubes, color = cube.split(' ')
                    game_cubes[color] = int(num_cubes)

                # update max_cubes
                for max_cube in max_cubes:
                    max_cubes[max_cube] = max(max_cubes[max_cube], game_cubes[max_cube])

            if possible:
                sum += max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]

    print(f"sum: {sum}")

day_2_2()
