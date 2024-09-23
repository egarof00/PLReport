import sys
# split string into a list of tokens
def tokenize(expression):
    # Tokenizes the input string expression into a list of numbers and operators
    tokens = []
    number = ''
    
    for char in expression:
        if char.isdigit() or char == '.':
            number += char  # Build multi-digit numbers and decimal points
        else:
            if number:
                tokens.append(number)  # Append the number when an operator is found
                number = ''
            if char.strip():  # Ignore whitespace
                tokens.append(char)  # Append operators and parentheses
    if number:
        tokens.append(number)  # Append the last number if exists

    return tokens

# processes next operation with the top two stack values
def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    
    # perform addition
    if operator == '+':
        values.append(left + right)
    # perform subtraction
    elif operator == '-':
        values.append(left - right)
    # perform multiplication
    elif operator == '*':
        values.append(left * right)
    # perform division
    elif operator == '/':
        values.append(left / right)
    # perform exponent
    elif operator == '^':
        values.append(left ** right)

# how to determine which order to perform operators in
def precedence(op):
    # third
    if op in ('+', '-'):
        return 1
    # second
    if op in ('*', '/'):
        return 2
    # first
    if op == '^':
        return 3
    return 0

# use stack to evaluate expression according to PEMDAS
def evaluate_expression(tokens):
    values = []
    operators = []

    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token.isnumeric() or '.' in token:  # Check for numbers (including decimals)
            values.append(float(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()  # Remove the '(' from stack
        else:
            # Operator
            while (operators and precedence(operators[-1]) >= precedence(token)):
                apply_operator(operators, values)
            operators.append(token)
        i += 1

    # Apply remaining operators
    while operators:
        apply_operator(operators, values)

    return values[0]  # The result will be the only element in values

# print("Enter an expression to be calculated: ")
# expression = input()
expression = sys.argv[1]
tokens = tokenize(expression)
result = evaluate_expression(tokens)
print(result)
