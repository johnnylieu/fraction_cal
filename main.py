# Write a function which takes a string input and returns whether the string is an operator or not

import sys

string = sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4]
string = string.split()
print(string)

def string_or_not():
    for i in string:
        if i == "+" or string == "-" or string == "*" or string == "/":
            print("string has an operator")
        else:
            print("string has no operator")

string_or_not()