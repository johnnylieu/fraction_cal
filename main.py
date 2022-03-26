# Write a function which takes a string input and returns whether the string is an operator or not

import sys

def is_it_operator():
    print(sys.argv)
    is_operator = False
    if sys.argv == '+' or sys.argv == '-' or sys.argv == '*' or sys.argv == '/':
        is_operator = True
    
    print(is_operator)

is_it_operator()