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

# Now is the time you write the loop to go through each item
# Here is a hint. Initialize a variable `sum` to 0.0. Start iterating from the beginning. Check if it is a num. Reuse the function here. If it is an operator, you can continue
# Otherwise, if it is a number, do total(sum, the number at the current index, operation at index - 1)
# So after you complete the step you're on right now, most of the problem is solved
# You just now need to parse the input
# Search "python string split"
# You need to not split operators. When it is a number, first split by "_", then by "/"
# Convert the number from mixed fractions to decimal numbers
# Also, for the solution, you need to convert decimal back to mixed fraction