from collections import defaultdict
import sys
import re
import math

def day_6_1():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        lines = file.readlines()
        time = list(map(int, lines[0].split(':')[1].split()))
        distance = list(map(int, lines[1].split(':')[1].split()))
        product = 1

        for i in range(len(distance)):
            # the max distance to be travelled is roughly the square root
            min_time = math.floor(distance[i] ** 0.5)
            max_time = math.ceil(distance[i] ** 0.5)

            while min_time * (time[i] - min_time) > distance[i]:
                min_time -= 1

            while max_time * (time[i] - max_time) > distance[i]:
                max_time += 1

            print(min_time, max_time)
            print(f"time {time[i]}, distance {distance[i]}")

            product *= max_time - min_time - 1

        print(product)

       
def day_6_2():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        lines = file.readlines()
        time = int(lines[0].split(':')[1].replace(' ', ''))
        distance = int(lines[1].split(':')[1].replace(' ', ''))

        print(time, distance)

        #     # the max distance to be travelled is roughly the square root
        min_time = math.floor(distance ** 0.5)
        max_time = math.ceil(distance ** 0.5)

        while min_time * (time - min_time) > distance:
            min_time -= 1

        while max_time * (time - max_time) > distance:
            max_time += 1

        print(min_time, max_time)
        print(max_time - min_time - 1)


day_6_2()
