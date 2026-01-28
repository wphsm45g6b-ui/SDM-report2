#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))
        def test_boundary_values(self):
                self.assertEqual(1, calc(1, 1))
                self.assertEqual(998001, calc(999, 999))

        def test_out_of_range(self):
                self.assertEqual(-1, calc(0, 10))
                self.assertEqual(-1, calc(1000, 10))
                self.assertEqual(-1, calc(10, 0))
                self.assertEqual(-1, calc(10, 1000))

        def test_non_integer(self):
                self.assertEqual(-1, calc(0.5, 10))
                self.assertEqual(-1, calc(10, 0.5))
                self.assertEqual(-1, calc("a", 10))
                self.assertEqual(-1, calc(10, "b"))
