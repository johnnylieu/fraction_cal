import unittest
from fractions import *

from pip import main
from main import get_num1, get_num2, num1_whole_number, num2_whole_number

class Test(unittest.TestCase):
    def test_get_num1(self):
        self.assertAlmostEqual(get_num1(1), num1_whole_number = 1)

# if __name__ == "__main__":
#     unittest.main()