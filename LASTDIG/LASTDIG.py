#!/usr/bin/python

import sys


# int -> boolean
def is_odd(str):
    return str % 2 != 0

# string -> string
def sum_digits(string):
    sum = 0
    for i in range(0, string.__len__()):
        current_digit = int(string[i])
        if is_odd(current_digit):
            sum += current_digit
        else:
            sum += current_digit * 2
    return str(sum)

# string -> int
def get_last_digit(str):
    return int(str[-1])

# string -> string
def get_all_sums(num1, num2):
    all_nums = [sum_digits(str(i)) for i in range(int(num1), int(num2)+1)]
    ints = map(int, map(get_last_digit, all_nums))
    return reduce(lambda x, y: x+y, ints)

# stdin -> stdout
def parse_input():
    num_cases = int(sys.stdin.readline())
    for i in range(0, num_cases):
        first, second = sys.stdin.readline().strip().split(" ")
        print >> sys.stdout, get_all_sums(first, second)
        

if __name__ == "__main__":
    parse_input()
