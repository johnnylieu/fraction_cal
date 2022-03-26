# Write a function which takes a string input and returns whether the string is an operator or not

import sys

def is_it_operator(item):
    is_operator = False
    if item == '+' or item == '-' or item == '*' or item == '/':
        is_operator = True
    print(is_operator)
    # print(f"sys argvs: {sys.argv}") # works
    # is_operator = False
    # if sys.argv[3] == '+' or sys.argv[3] == '-' or sys.argv[3] == '*' or sys.argv[3] == '/':
    #     is_operator = True
    # print(is_operator)

is_it_operator("+")