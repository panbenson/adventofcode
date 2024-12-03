from collections import defaultdict
import copy
import sys
import re
import math

def day_5_1():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        # store the input as a huge array
        maps = []
        current_entry = []

        for raw_line in file:
            line = raw_line.strip()
            if line.startswith("seeds: "):
                current_entry = list(map(int,line.split("seeds: ")[1].split(" ")))
            # move on to the next map
            elif line.endswith("map:"):
                maps.append(current_entry)
                current_entry = []
            elif line != "":
                current_entry.append(list(map(int, line.split(" "))))

        # process the last map
        maps.append(current_entry)

        min_location = math.inf
        for seed in maps[0]:
            location = seed
            for mapping in maps[1:]:
                # check if we have any special mappings
                special_mapping = -1
                for [dest, source, length] in mapping:
                    if location >= source and location <= (source + length):
                        special_mapping = dest + (location - source)
                        break

                if special_mapping > -1:
                    # print(f"special mapping {location} => {special_mapping}")
                    location = special_mapping
                # else:
                #     print(f"mapping {location} => {location}")

            # print(f"location for seed {seed} is {location}")
            min_location = min(min_location, location)

        print(min_location)



def day_5_2():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        # store the input as a huge array
        maps = []
        current_entry = []

        for raw_line in file:
            line = raw_line.strip()
            if line.startswith("seeds: "):
                current_entry = list(map(int,line.split("seeds: ")[1].split(" ")))
            # move on to the next map
            elif line.endswith("map:"):
                maps.append(current_entry)
                current_entry = []
            elif line != "":
                current_entry.append(list(map(int, line.split(" "))))

        # process the last map
        maps.append(current_entry)

        min_location = math.inf
        location_ranges = []
        for i in range(0, len(maps[0]), 2):
            location_ranges.append([maps[0][i], maps[0][i] + maps[0][i+1] - 1])

        # update part two, seeds are ranges
        # NOTE: iterating thru the rangers is prohibitively large, operate on ranges instead
        for mapping in maps[1:]:
            print(location_ranges)
            location_ranges_copy = copy.deepcopy(location_ranges)
            next_location_ranges = []

            while len(location_ranges_copy):
                [start, end] = location_ranges_copy.pop()
                had_special_mapping = False
                # check if we have any special mappings
                for [dest, source, length] in mapping:
                    # END RANGE SHOULD NOT BE INCLUSIVE!!!
                    if start >= source and start < source + length - 1 or end >= source and end < source + length - 1:
                        # left
                        if start < source:
                            location_ranges_copy.append([start , source - 1])
                        # right
                        if end > source + length - 1:
                            location_ranges_copy.append([source + length, end])
                        # overlap
                        next_location_ranges.append([dest + max(start, source) - source, dest + min(end, source + length - 1) - source])
                        had_special_mapping = True
                        break

                if not had_special_mapping:
                    next_location_ranges.append([start, end])

            location_ranges = next_location_ranges

        print(min(map(lambda x: x[0], location_ranges)))



# day_5_1()
day_5_2()
