# checks if parentheses are "balanced"

def check_parentheses(expression):
    # Initialize a counter
    parentheses_count = 0

    # Iterate through each character in the expression
    for char in expression:
        if char == '(':
            parentheses_count += 1  # Increment for an open parenthesis
        elif char == ')':
            parentheses_count -= 1  # Decrement for a closed parenthesis
            # If at any point the count goes negative, there's a mismatch
            if parentheses_count < 0:
                return False

    # if count is 0, parentheses match, otherwise they don't
    return parentheses_count == 0


expr = input("Enter a mathematical expression: ")
if check_parentheses(expr):
    print("yes")
else:
    print("no")