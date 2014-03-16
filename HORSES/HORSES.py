#!/usr/bin/python

'''Average case is O(n^2) because there needs to be two sorts (maybe)
   In any case, two sorts is bad.'''

import fileinput
import string
import sys

# int -> int
def find_diff(int1, int2):
    return abs(int2 - int1)

# [int] -> [int]
def find_diffs(list):
    if len(list) == 2:
        return [find_diff(list[0], list[1])]
    else:
        return [find_diff(list[i], list[i+1])
                for i in range(0, len(list) - 1)]

# [int] -> int
def min_diff(horseSkills):
    sortedHorses = sorted(horseSkills) # one sort
    horseDiffs = find_diffs(sortedHorses)
    return sorted(horseDiffs)[0] # second sort
    
# str -> [int]
def str2list_ints(str):
    return map(int, string.split(str.strip(), " "))  # Give the ints in an array here

# File -> iterator([int])
def parse_input():
    input = fileinput.input()
    numTestCases = int(input.readline())
    for i in range (0, numTestCases):
        numInts = input.readline()   # Probably do something useful with this later
        yield str2list_ints(input.readline())  # Give the ints in an array here


if __name__ == "__main__":
    for testCase in parse_input():
        print >> sys.stdout, min_diff(testCase)
