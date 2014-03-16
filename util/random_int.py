#!/usr/bin/python

import csv
import random
import sys

# int -> print
def main(n):
    min = 0
    max = 1000000000
    rand_nums = [random.randint(min,max) for i in range(0, n)]
    writer = csv.writer(sys.stdout, delimiter=' ')
    writer.writerow(rand_nums)

if __name__ == "__main__":
    main(int(sys.argv[1]))
