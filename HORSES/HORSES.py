#!/usr/bin/python

'''Average case is O(n^2) because there needs to be two sorts (maybe)
   In any case, two sorts is bad.'''

import fileinput
import string
import sys

# int -> int
def find_diff(int1, int2):
    return abs(int2 - int1)

# [int] -> int
def min_diff(horseSkills):
    sortedHorses = sorted(horseSkills) # one sort
    horseDiffs = [] 
    for i in range(0, len(sortedHorses) - 1):
        horseDiffs.append(find_diff(sortedHorses[i], sortedHorses[i+1]))
    sorted(horseDiffs) # second sort
    return horseDiffs[0]
    
# File -> iterator([int])
def parse_input():
    input = fileinput.input()
    numTestCases = int(input.readline())
    for i in range (0, numTestCases):
        numInts = input.readline()   # Probably do something useful with this later
        yield map(int, string.split(input.readline().strip(), " "))  # Give the ints in an array here


if __name__ == "__main__":
    for testCase in parse_input():
        print >> sys.stdout, min_diff(testCase)
