#!/usr/bin/python

import fileinput
import math
import sys

# int -> [int]
def exchange(n):
    first_coin = int(math.floor(n//2))
    second_coin = int(math.floor(n//3))
    third_coin = int(math.floor(n//4))
    return [first_coin, second_coin, third_coin]

# int -> int
def max_amount(n):
    coins = exchange(n)
    if n > sum(coins): #change to lambda function which is faster
        return n
    else:
        return sum([max_amount(i) for i in coins])

if __name__ == "__main__":
    for line in fileinput.input():
        print >> sys.stdout, max_amount()
