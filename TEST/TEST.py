#!/usr/bin/python

import fileinput
import sys

def main():
    for line in fileinput.input():
        number = line.strip()
        if number != '42':
            print >> sys.stdout, number
        else:
            break

if __name__ == "__main__":
    main()
