#!/usr/bin/python

import sys

# File -> iterator([string])
def parse_input():
    with open(sys.stdin, 'r') as input:
        numTestCases = input.readline()
        for i in range (0, numTestCases):
            numInts = input.readline()   # Probably do something useful with this later
            yield split(input.readline(), " ")  # Give the ints in an array here


if __name__ == "__main__":
    parse_input()
