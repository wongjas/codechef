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
    print >> sys.stderr, n
    max = lookup(n)
    if max == None:
        coins = exchange(n)
        max = sum(coins) # change to lambda function which is faster
        store(n, max)
    if n > max: 
        return n
    else:
        coins = exchange(n)
        return sum([max_amount(i) for i in coins])

if __name__ == "__main__":
    for line in fileinput.input():
        print >> sys.stdout, max_amount(int(line))
