# Coding Challenge
 
# Write a command line program in the language of your choice that will take operations on fractions as an input and produce a fractional result.
# Legal operators shall be *, /, +, - (multiply, divide, add, subtract)
# Operands and operators shall be separated by one or more spaces
# Mixed numbers will be represented by whole_numerator/denominator. e.g. "3_1/4"
# Improper fractions and whole numbers are also allowed as operands 
# Example run:
# ? 1/2 * 3_3/4
# = 1_7/8
 
# ? 2_3/8 + 9/8
# = 3_1/2

# return integer first
# look into % (modular) for fraction
# remainder/denominator

from ast import operator
from fractions import *
from operator import *
from operator import *
from os import times
# help(operator)
# dir(operator)

input = ["3.9", "+", "6.8", "-", "1.3"]

def is_it_operator(item):
    is_operator = False
    if item == '+' or item == '-' or item == '*' or item == '/':
        is_operator = True
    print(f"{item} is an operator: {is_operator}")

def total(num1, num2, operand):
    if operand == "+":
        sum = float(num1) + float(num2)
        print(f"the sum is: {sum}")
    elif operand == "-":
        difference = float(num1) - float(num2)
        print(f"the diff is: {difference}")
    elif operand == "*":
        times = float(num1) * float(num2)
        print(f"the times is: {times}")
    elif operand == "/":
        dividend = float(num1) / float(num2)
        print(f"the dividend is: {dividend}")
    elif operand != "+" or op != "-" or op != "*" or op != "/":
        print(f"Please choose a valid operand (+, *, -, /)")

# is_it_operator()
total("3.9", "2.1", "+")
total("2.1", "3.9", "-")
total("4", "12", "*")
total("12", "4", "/")
total("12", "4", "4")

    # print(f"sys argvs: {sys.argv}") # works
    # is_operator = False
    # if sys.argv[3] == '+' or sys.argv[3] == '-' or sys.argv[3] == '*' or sys.argv[3] == '/':
    #     is_operator = True
    # print(is_operator)