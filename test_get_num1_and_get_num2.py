import unittest
from main import get_num1, get_num2, num1_whole_number, num2_whole_number

class Test(unittest.TestCase):
    def test_get_num1(self):
        # given a whole number, it should be appended to num1_whole_number
        #arrange
        # act
        #assert
        self.assertEqual(get_num1("2"), num1_whole_number.append("2"))

    def test_get_num2(self):
        # given a whole number, it should be appended to num1_whole_number
        #arrange
        # act
        #assert
        self.assertEqual(get_num2("3"), num2_whole_number.append("3"))

if __name__ == "__main__":
    unittest.main()