from collections import defaultdict
import sys
import re
import math

def day_5_1():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        min_loc = math.inf
        # store everything in a huge array
        data = [[] for i in range(8)]
        i = 0

        for line in file:
            text = line.strip()

            if text == '':
                i += 1
                continue

            if 'map:' in text:
                continue

            if i == 0:
                data[i] = list(map(int, text.split(': ')[1].split()))
            else:
                data[i].append(list(map(int, text.split())))

        

        for seed in data[0]:
            plant_idx = seed
            for plant_map in range(1, len(data)):
                for dest_start, source_start, range_length in data[plant_map]:
                    if plant_idx >= source_start and plant_idx <= (source_start + range_length):
                        plant_idx = (plant_idx - source_start) + dest_start
                        break

                if plant_map + 1 == len(data):
                    min_loc = min(plant_idx, min_loc)


        print(min_loc)


def collapse_ranges(ranges):
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    current = sorted_ranges[0]
    merged = []
    i = 0

    while i < len(sorted_ranges) - 1:
        if sorted_ranges[i][0] > current[1]:
            merged.append(current)
            current = sorted_ranges[i]
        else:
            current = [current[0], max(current[1], sorted_ranges[i][1])]

        i += 1

    merged.append(current)

    return merged


#pt 2  - need to switch to ranges for everything
def day_5_2():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        min_loc = math.inf
        # store everything in a huge array
        data = [[] for i in range(8)]
        i = 0

        for line in file:
            text = line.strip()

            if text == '':
                i += 1
                continue

            if 'map:' in text:
                continue

            if i == 0:
                data[i] = list(map(int, text.split(': ')[1].split()))
            else:
                data[i].append(list(map(int, text.split())))

        

        for i in range(0, len(data[0]), 2):
            plant_ranges = [[data[0][i], data[0][i] + data[0][i + 1]]]
            for plant_map in range(1, len(data)):
                print(f"step {plant_map}")
                print()
                print(plant_ranges)
                new_ranges = []
                while len(plant_ranges):
                    plant_range = plant_ranges.pop()
                    # print(">>> mapping range", plant_range)
                    was_mapped = False
                    for dest_start, source_start, range_length in data[plant_map]:
                        # print(f"trying to map {dest_start}, {source_start}, {range_length}")
                        # theres 3 possible overlapping scenarios
                        # if the source can be completely transformed
                        if source_start <= plant_range[0] and (source_start + range_length) >= plant_range[1]:
                            # print(f"fully overlaps! {plant_range} --> {[(plant_range[0] - source_start) + dest_start, (plant_range[1] - source_start) + dest_start]}")
                            new_ranges.append([(plant_range[0] - source_start) + dest_start, (plant_range[1] - source_start) + dest_start])
                            was_mapped = True
                        # only the right side overlaps
                        elif source_start >= plant_range[0] and source_start <= plant_range[1]:
                            # print(f"right side overlaps! {plant_range} --> {[plant_range[0], source_start - 1]}, {[dest_start, (plant_range[1] - source_start) + dest_start]}")
                            plant_ranges.append([plant_range[0], source_start - 1])
                            new_ranges.append([dest_start, (plant_range[1] - source_start) + dest_start])
                            was_mapped = True
                        # only the left side overlaps
                        elif (source_start + range_length) >= plant_range[0] and (source_start + range_length) <= plant_range[1]:
                            # print(f"left side overlaps! {plant_range} --> {[(plant_range[0] - source_start) + dest_start, (plant_range[1] - source_start) + dest_start]}, {[source_start + range_length + 1, plant_range[1]]}")
                            new_ranges.append([(plant_range[0] - source_start) + dest_start, (plant_range[1] - source_start) + dest_start])
                            plant_ranges.append([source_start + range_length + 1, plant_range[1]])
                            was_mapped = True
                    if not was_mapped:
                        new_ranges.append(plant_range)

                plant_ranges = collapse_ranges(new_ranges)

                if plant_map + 1 == len(data):
                    print('finding min')
                    min_loc = min(min(map(lambda x: x[0], plant_ranges)), min_loc)
                    print(min_loc)


        print(min_loc)


day_5_2()
