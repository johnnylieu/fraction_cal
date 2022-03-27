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

from fractions import *
from operator import *
from operator import *
import sys
# help(operator)
# dir(operator)

# Now is the time you write the loop to go through each item
# Here is a hint. Initialize a variable `sum` to 0.0. Start iterating from the beginning. Check if it is a num. Reuse the function here. If it is an operator, you can continue
# Otherwise, if it is a number, do total(sum, the number at the current index, operation at index - 1)

def is_it_operator(item):
    is_operator = False
    if item == '+' or item == '-' or item == '*' or item == '/':
        is_operator = True
    print(f"{item} is an operator: {is_operator}")

def total(num1, num2, operand):
    is_it_operator(operand)
    if operand == "+":
        return float(num1) + float(num2)
    elif operand == "-":
        return float(num1) - float(num2)
    elif operand == "*":
        return float(num1) * float(num2)
    elif operand == "/":
        return float(num1) / float(num2)

def loop(item):
    sum = 0.0
    sum_list = []
    for i in range(len(item)-1):
        print(item[i])
        if is_it_operator(item[i]) == None:
            sum_list.append(item[i])
            print(sum_list)
            sum = float(sum) + float(item[i])
            print(f"sum: {sum}")
        elif is_it_operator(item[i]) == True:
            continue

# input = ["3.9", "+", "6.8", "-", "1.3"]
input = ["3.9", "2.1", "+"]
loop(input)

# print(total("3.9", "2.1", "+"))
# print(total("2.1", "3.9", "-"))
# print(total("4", "12", "*"))
# print(total("12", "4", "/"))
# print(total("12", "4", "4"))

# is_it_operator("+")
# is_it_operator("-")
# is_it_operator("*")
# is_it_operator("/")
# is_it_operator("4")


    # print(f"sys argvs: {sys.argv}") # works
    # is_operator = False
    # if sys.argv[3] == '+' or sys.argv[3] == '-' or sys.argv[3] == '*' or sys.argv[3] == '/':
    #     is_operator = True
    # print(is_operator)