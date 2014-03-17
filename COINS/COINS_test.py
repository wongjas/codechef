#!/usr/bin/python

import unittest

import COINS as coins

class test_COINS(unittest.TestCase):
    
    def test_exchange(self):
        self.assertEquals(coins.exchange(12), [6, 4, 3])
        self.assertEquals(coins.exchange(24), [12, 8, 6])
        self.assertEquals(coins.exchange(100), [50, 33, 25])

    def test_max_amount(self):
        self.assertEquals(coins.max_amount(100), 120)
        self.assertEquals(coins.max_amount(24), 27)
        self.assertEquals(coins.max_amount(12), 13)
        self.assertEquals(coins.max_amount(0), 0)
        self.assertEquals(coins.max_amount(1000000000), 4243218150) 

if __name__ == "__main__":
    unittest.main()
