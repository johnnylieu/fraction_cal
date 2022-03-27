import unittest
from fractions import *

from pip import main
from main import get_num1, get_num2, num1_whole_number, num2_whole_number

def TestGetNum1(self):
    # number should be imported to num1_whole_number so its length should be greater than 0
    self.assertAlmostEqual(get_num1(1), (len(num1_whole_number) > 0))

def TestGetNum1(self):
    # number should be imported to num1_whole_number so its length should be greater than 0
    self.assertAlmostEqual(get_num1(3/4), (len(num1_whole_number) > 0))

def TestGetNum2(self):
    # number should be imported to num1_whole_number so its length should be greater than 0
    self.assertAlmostEqual(get_num2(1), (len(num2_whole_number) > 0))

def TestGetNum2(self):
    # number should be imported to num1_whole_number so its length should be greater than 0
    self.assertAlmostEqual(get_num2(2_1/2), (len(num2_whole_number) > 0))