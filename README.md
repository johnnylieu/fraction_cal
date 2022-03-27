# Coding Challenge

Write a command line program in the language of your choice that will take operations on fractions as an input and produce a fractional result.
Legal operators shall be *, /, +, - (multiply, divide, add, subtract).
Operands and operators shall be separated by one or more spaces.
Mixed numbers will be represented by whole_numerator/denominator. e.g. "3_1/4"
Improper fractions and whole numbers are also allowed as operands. 

Example run:

? 1/2 * 3_3/4

= 1_7/8
 
? 2_3/8 + 9/8

 = 3_1/2


Hint:
return integer first,
look into % (modular) for fraction,
remainder/denominator.

## Usage

**Video demo**: <https://youtu.be/cewlfWZ7nIQ>

-download main.py

-install Python 3

-navigate to the folder holding main.py

-open your terminal

-run app in command line by typing this format: "* *python3 main.py ? a_number a_operand another_number* *"

for example:

"* *python3 main.py ? 1/2 * 3_3/4* *"

or

"* *python3 main.py ? 1 + 3* *"

-the app will return an answer in this format: "* *= whole_number _ numerator / denominator* *"

for example:
"* *python3 main.py ? 1/2 * 3_3/4* *" will return "* *= 1_7/8* *"

and

"* *python3 main.py ? 1 + 3* *" will return "* *= 4* *"