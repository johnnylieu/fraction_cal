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
# So after you complete the step you're on right now, most of the problem is solved
# You just now need to parse the input
# Search "python string split"
# You need to not split operators. When it is a number, first split by "_", then by "/"
# Convert the number from mixed fractions to decimal numbers
# Also, for the solution, you need to convert decimal back to mixed fraction

num1_whole_number = []
num1_fraction = []

num2_whole_number = []
num2_fraction = []

def get_num1_and_num2():
    num1 = num1_fraction + num1_whole_number
    num1 = [x for x in num1 if x!= "0"]
    print(f"num1: {num1}")
    num1 = Fraction(num1[0]) + Fraction(num1[1])
    print(f"num1: {num1}")

    num2 = num2_fraction + num2_whole_number
    num2 = [x for x in num2 if x!= "0"]
    print(f"num1: {num2}")
    num2 = Fraction(num2[0]) + Fraction(num2[1])
    print(f"num1: {num2}")

    if sys.argv[3] == "+":
        sum = num1 + num2
        sum = Fraction(sum)
        print(f"= {sum}") # works

def is_it_operator(item):
    is_operator = False
    if item == '+' or item == '-' or item == '*' or item == '/':
        is_operator = True
    print(f"{item} is an operator: {is_operator}")

def split(word):
    return [char for char in word]

def get_fract1(fract1):
    fract1 = split(fract1)
    # print(f"fract1: {fract1}") # works
    for i,x in enumerate(fract1):
        if fract1[i] == "/":
            fraction1 = fract1[i-1] + "/" + fract1[i+1]
            # print(f"fraction1: {fraction1}") # works
            num1_fraction.append(fraction1)
            print(f"num1 fraction: {num1_fraction}") # works

def get_fract2(fract2):
    fract2 = split(fract2)
    # print(f"fract2: {fract2}") # works
    for i,x in enumerate(fract2):
        if fract2[i] == "/":
            fraction1 = fract2[i-1] + "/" + fract2[i+1]
            # print(f"fraction1: {fraction1}") # works
            num2_fraction.append(fraction1)
            print(f"num2 fraction: {num2_fraction}") # works

def get_num1(num1):
    num1 = split(num1)
    # print(f"num1: {num1}")
    for i,x in enumerate(num1):
        if num1[i] == "_":
            whole_number = num1[i-1]
            # print(f"whole number: {whole_number}")
            num1_whole_number.append(whole_number)
            # print(f"whole_num1: {num1_whole_number}")
        else:
            num1_whole_number.append("0")
            print(f"whole_num1: {num1_whole_number}")

def get_num2(num2):
    num2 = split(num2)
    # print(f"num1: {num2}")
    for i,x in enumerate(num2):
        if num2[i] == "_":
            whole_number = num2[i-1]
            # print(f"whole number: {whole_number}")
            num2_whole_number.append(whole_number)
            # print(f"whole_num2: {num2_whole_number}")
        else:
            num1_whole_number.append("0")
            print(f"whole_num2: {num2_whole_number}")

if __name__ == "__main__":
    get_num1(sys.argv[2])
    get_num2(sys.argv[4])
    get_fract1(sys.argv[2])
    get_fract2(sys.argv[4])

    get_num1_and_num2()



# def get_num2(num2):
#     num2 = split(num2)
#     print(f"num2: {num2}")
#     for i,x in enumerate(num2):
#         if num2[i] == "_":
#             whole_number = num2[i-1]
#             print(f"whole number: {whole_number}")
#             num2_whole_number.append(whole_number)
#             print(f"whole_num1: {num2_whole_number}")
#         else:
#             num2_whole_number.append("0")
#             print(f"whole_num2: {num2_whole_number}")

# def total(num1, num2, operand):
#     is_it_operator(operand)
#     if operand == "+":
#         return float(num1) + float(num2)
#     elif operand == "-":
#         return float(num1) - float(num2)
#     elif operand == "*":
#         return float(num1) * float(num2)
#     elif operand == "/":
#         return float(num1) / float(num2)

# def loop(item):
#     sum = 0.0
#     sum_list = []
#     for i in range(len(item)-1):
#         print(item[i])
#         if is_it_operator(item[i]) == None:
#             sum_list.append(item[i])
#             # print(sum_list)
#             sum = float(sum) + float(item[i])
#         elif is_it_operator(item[i]) == True:
#             continue
#     print(f"sum: {sum}")

# input = ["3.9", "2.1", "+"]
# loop(input)

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