# Write a function which takes a string input and returns whether the string is an operator or not

def is_it_operator(item):
    is_operator = False
    if item == '+' or item == '-' or item == '*' or item == '/':
        is_operator = True
    print(f"{item} is an operator: {is_operator}")

is_it_operator("+")
is_it_operator("-")
is_it_operator("*")
is_it_operator("/")
is_it_operator("5")
is_it_operator(3)
is_it_operator("T")