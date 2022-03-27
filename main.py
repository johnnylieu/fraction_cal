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

input = ["3.9", "+", "6.8", "-", "1.3"]
print(f"input: {input}")

def is_it_operator(item):
    is_operator = False
    if item == '+' or item == '-' or item == '*' or item == '/':
        is_operator = True
    print(f"{item} is an operator: {is_operator}")

def add():
    filtered_input = [x for x in input if x!="+" if x!="-" if x!="*" if x!= "/"]
    print(f"filtered input: {filtered_input}")
    total = Fraction(0)
    for i in filtered_input:
        i = Fraction(i)
        print(i)
        total = total + i
    print(f"total sum is: {total}")

# is_it_operator()
add()

    # print(f"sys argvs: {sys.argv}") # works
    # is_operator = False
    # if sys.argv[3] == '+' or sys.argv[3] == '-' or sys.argv[3] == '*' or sys.argv[3] == '/':
    #     is_operator = True
    # print(is_operator)