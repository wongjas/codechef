#!/usr/bin/python

import unittest
import sys

import HORSES as horse

class HorseTest(unittest.TestCase):

    def test_find_diffs(self):
        orig = [1,5,8,3,6]
        self.assertEquals(horse.find_diffs(orig), [4, 3, 5, 3])
        self.assertEquals(len(horse.find_diffs(orig)), len(orig) -1)
        self.assertEquals(horse.find_diffs([1,2]), [1])

    def test_min_diffs(self):
        horse_skills = [23421, 1324, 1000, 239043, 5230]
        self.assertEquals(horse.min_diff(horse_skills), 324)
        self.assertEquals(horse.min_diff([0,0,0,0,0]), 0)
        self.assertEquals(horse.min_diff([101010, 100000, 23532]), 1010)
        self.assertIs(type(horse.min_diff([10,100])), int)

    def test_str2list_ints(self):
        self.assertEquals(horse.str2list_ints("1 2 52 3 53 2 1"), [1, 2, 52, 3 ,53, 2, 1])

if __name__ == "__main__":
    unittest.main()
