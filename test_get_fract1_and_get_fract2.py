import unittest
from main import get_fract1, get_fract2, num2_fraction, num1_fraction

class Test(unittest.TestCase):
    def test_get_num1(self):
        # given a fraction, it should be appended to num1_fraction
        #arrange
        # act
        #assert
        self.assertEqual(get_fract1("2/3"), num1_fraction.append("2/3"))

    def test_get_num2(self):
        # given a fraction, it should be appended to num2_fraction
        #arrange
        # act
        #assert
        self.assertEqual(get_fract2("5/4"), num2_fraction.append("5/4"))

if __name__ == "__main__":
    unittest.main()