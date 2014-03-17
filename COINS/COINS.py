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

calculated = dict([]) # stores the already calculated values

# dict(int:int) -> int or None
def lookup(key):
    return calculated.get(key)

# int, int -> None
def store(key, value):
    calculated[key] = value

# int -> int
def max_amount(n):
    max = lookup(n)
    if max == None:
        coins = exchange(n)
        max = sum(coins) # change to lambda function which is faster
        if n >= max: 
            return n
        else:
            new_max = sum([max_amount(i) for i in coins])
            store(n, new_max)
            return new_max
    else:
        return max


if __name__ == "__main__":
    for line in fileinput.input():
        print >> sys.stdout, max_amount(int(line))

