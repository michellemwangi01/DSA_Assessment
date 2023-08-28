from collections import deque

# Stacks:

# Question 1: Implement a function is_balanced(expression) that takes a string
# containing parentheses, curly braces, and square brackets,and determines whether
# the expression is balanced.

# An expression is considered balanced if each opening bracket has a corresponding closing
# bracket in the correct order.

# sample input =

# expression1 = "([]{})"
# expression2 = "([)]"
# print(is_balanced(expression1))  # Output: True
# print(is_balanced(expression2))  # Output: False


#  1. collection.deque


def is_balanced_one(your_string):
    my_bracket_dict = {"[": "]", "{": "}", "(": ")"}
    new_dict = [key for key in my_bracket_dict if key in your_string]
    print(new_dict)
    keys = [key for key in new_dict]
    partner_check = list()
    for key in keys:
        partner = my_bracket_dict.get(key)
        print(partner)
        if partner in your_string:
            partner_check.append(True)
        else:
            partner_check.append(False)

    print(partner_check)
    if False in partner_check:
        return False
    else:
        return True


print("-------------------------------------------------------------------")


def is_balanced_two(sequence):
    stack = []
    my_bracket_dict = {"[": "]", "{": "}", "(": ")"}
    for char in sequence:
        if char in my_bracket_dict:
            stack.append(char)
    print(stack)
