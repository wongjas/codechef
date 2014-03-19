#!/usr/bin/python

import unittest
import LASTDIG as last

class test_LASTDIG(unittest.TestCase):

    def test_is_odd(self):
        self.assertEquals(last.is_odd(1), True)
        self.assertEquals(last.is_odd(5), True)
        self.assertFalse(last.is_odd(4))

    def test_sum_digits(self):
        self.assertEquals(last.sum_digits("5678"), "40")

    def test_get_last_digit(self):
        self.assertEquals(last.get_last_digit("12345"), 5)
        
    def test_get_all_sums(self):
        self.assertEquals(last.get_all_sums("1", "2"), 3)
        self.assertEquals(last.get_all_sums("1", "8"), 36)


if __name__ == "__main__":
    unittest.main()
