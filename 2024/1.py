from collections import defaultdict
import copy
import sys
import re
import math

def day_1_1():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        left_list = []
        right_list = []
        for line in file:
            row = line.split('   ')
            left_list.append(int(row[0]))
            right_list.append(int(row[1]))

        left_list = sorted(left_list)
        right_list = sorted(right_list)

        print(sum(map(lambda x: abs(left_list[x] - right_list[x]), range(len(left_list)))))


def day_1_2():

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        left_list = []
        right_list = defaultdict(int)
        for line in file:
            row = line.split('   ')
            left_list.append(int(row[0]))
            right_list[int(row[1])] += 1

        similarity_score = 0
        for left_num in left_list:
            similarity_score += left_num * right_list[left_num]
        print(similarity_score)

# day_1_1()
day_1_2()
