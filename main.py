from fractions import *
from operator import *
from operator import *
import sys
# help(operator)
# dir(operator)

num1_whole_number = []
num1_fraction = []

num2_whole_number = []
num2_fraction = []

def get_num1_and_num2():
    num1 = num1_fraction + num1_whole_number
    num1 = [x for x in num1 if x!= "0"]
    # print(f"num1: {num1}")
    if len(num1) == 1:
        num1 = Fraction(num1[0]) + Fraction(0)
    elif len(num1) == 0:
        num1 = Fraction("0")
    else:
        num1 = Fraction(num1[0]) + Fraction(num1[1])
    # print(f"num1: {num1}")

    num2 = num2_fraction + num2_whole_number
    num2 = [x for x in num2 if x!= "0"]
    # print(f"num2: {num2}")
    if len(num2) == 1:
        num2 = Fraction(num2[0]) + Fraction(0)
    else:
        num2 = Fraction(num2[0]) + Fraction(num2[1])
    # print(f"num2: {num2}")

    if sys.argv[3] == "+":
        # print(f"num1 and num2: {num1} & {num2}")
        sum = num1 + num2
        # print(f"sum: {sum}")
        sum = str(sum)
        sum = sum.split("/")
        # print(f"sum: {sum}")
        if len(sum) == 1:
            print(f"= {sum[0]}")
        else:
            numerator = sum[0]
            denominator = sum[1]
            # print(f"numerator & denominator: {numerator} & {denominator}")
            modular = int(numerator) % int(denominator)
            # print(f"modular: {modular}")
            if abs(int(numerator)) > abs(int(denominator)):
                whole = int(numerator) / int(denominator)
                whole = str(whole)
                whole = whole.split(".")
                whole = whole[0]
                # print(f"whole: {whole}")
                print(f"= {whole}_{modular}/{denominator}") # works
            elif int(numerator) < int(denominator):
                print(f"= {numerator}/{denominator}")

    if sys.argv[3] == "-":
        sum = num1 - num2
        sum = str(sum)
        sum = sum.split("/")
        # print(sum)
        if len(sum) == 1:
            print(f"= {sum[0]}")
        else:
            numerator = sum[0]
            denominator = sum[1]
            # print(f"numerator & denominator: {numerator} & {denominator}")
            modular = int(numerator) % int(denominator)
            # print(f"modular: {modular}")
            if abs(int(numerator)) > abs(int(denominator)):
                whole = int(numerator) / int(denominator)
                whole = str(whole)
                whole = whole.split(".")
                whole = whole[0]
                # print(f"whole: {whole}")
                print(f"= {whole}_{modular}/{denominator}") # works
            elif int(numerator) < int(denominator):
                print(f"= {numerator}/{denominator}")

    if sys.argv[3] == "*":
        sum = num1 * num2
        sum = str(sum)
        sum = sum.split("/")
        # print(sum)
        if len(sum) == 1:
            print(f"= {sum[0]}")
        else:
            numerator = sum[0]
            denominator = sum[1]
            # print(f"numerator & denominator: {numerator} & {denominator}")
            modular = int(numerator) % int(denominator)
            # print(f"modular: {modular}")
            if abs(int(numerator)) > abs(int(denominator)):
                whole = int(numerator) / int(denominator)
                whole = str(whole)
                whole = whole.split(".")
                whole = whole[0]
                # print(f"whole: {whole}")
                print(f"= {whole}_{modular}/{denominator}") # works
            elif int(numerator) < int(denominator):
                print(f"= {numerator}/{denominator}")

    if sys.argv[3] == "/":
        sum = num1 / num2
        sum = str(sum)
        sum = sum.split("/")
        # print(sum)
        if len(sum) == 1:
            print(f"= {sum[0]}")
        else:
            numerator = sum[0]
            denominator = sum[1]
            # print(f"numerator & denominator: {numerator} & {denominator}")
            modular = int(numerator) % int(denominator)
            # print(f"modular: {modular}")
            if abs(int(numerator)) > abs(int(denominator)):
                whole = int(numerator) / int(denominator)
                whole = str(whole)
                whole = whole.split(".")
                whole = whole[0]
                # print(f"whole: {whole}")
                print(f"= {whole}_{modular}/{denominator}") # works
            elif int(numerator) < int(denominator):
                print(f"= {numerator}/{denominator}")

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
            # print(f"num1 fraction: {num1_fraction}") # works

def get_fract2(fract2):
    fract2 = split(fract2)
    # print(f"fract2: {fract2}") # works
    for i,x in enumerate(fract2):
        if fract2[i] == "/":
            fraction1 = fract2[i-1] + "/" + fract2[i+1]
            # print(f"fraction1: {fraction1}") # works
            num2_fraction.append(fraction1)
            # print(f"num2 fraction: {num2_fraction}") # works

def get_num1(num1):
    num1 = split(num1)
    # print(f"num1: {num1}")
    for i,x in enumerate(num1):
        if num1[i] == "_":
            whole_number = num1[i-1]
            # print(f"whole number: {whole_number}")
            num1_whole_number.append(whole_number)
            # print(f"whole_num1: {num1_whole_number}")
        elif num1[i] != "_" and num1[i]!= "/":
            num1_whole_number.append("0")
            # print(f"whole_num1: {num1_whole_number}")

def get_num2(num2):
    num2 = split(num2)
    # print(f"num1: {num2}")
    for i,x in enumerate(num2):
        if num2[i] == "_":
            whole_number = num2[i-1]
            # print(f"whole number: {whole_number}")
            num2_whole_number.append(whole_number)
            # print(f"whole_num2: {num2_whole_number}")
        elif num2[i] != "_" and num2[i]!= "/":
            num2_whole_number.append("0")
            # print(f"whole_num2: {num2_whole_number}")

if __name__ == "__main__":
    get_num1(sys.argv[2])
    get_num2(sys.argv[4])
    get_fract1(sys.argv[2])
    get_fract2(sys.argv[4])
    get_num1_and_num2()