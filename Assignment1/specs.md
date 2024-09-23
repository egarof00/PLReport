# Assignment 1: CPSC 354

**Name:** Emma Garofalo

**Email:** garofalo@chapman.edu

**Section:** 2

## Included Files:
* calculator.py
* parentheses.py

### calculator.py
Methods and purpose:
* **tokenize(expression):** 
    This method takes the user input string and splits it into a list of tokens for other methods to process. It appends the operators as characters and the numbers as number values to the list.
* **precedence(op):**
    This method assigns a "precedence" or ranking to each operation so that they are able to be put into the correct order of operations. Exponents are given a 3, which is higher than multiplication and division at 2, and addition and subtraction at 1. 
* **apply_operator(operators, values):**
    Apply Operator is where the actual mathmatical calculation takes place. Depending on what operator is passed to the method, it performs the necessary mathematical calculation with the values to the right and left of the operator and replaces the value in the correct position of the list. 
* **evaluate_expression(tokens):**
    This traverses the token list and performs the operations in the proper order considering PEMDAS. It goes through this method until there is only one element left to be the final answer.


### parentheses.py
Methods and purpose:
* **check_parentheses(expression):**
    This method takes the expression it is given, and iterates over each character in that expression. If the character is an open parenthesis, a one is added to the parentheses count, and if it is a closed parentheses, one is subtracted from the count. If at any point this value becomes negative, the parentheses are not balanced because an open parentheses must precede a closed parentheses. At the end, if the count value does not equal zero, then there is not a matching number of open and closed parentheses, and the mathematical expression is invalid. If all parentheses are balanced, this method will return 0.


### General Program Flow:
parentheses.py is a simple program, so once an expression is given, it performs the single method it has, and returns "yes" or "no" to demonstrate whether the parentheses are balanced or not. 

calculator.py is a little more complicated. An expression is given to the program, and the first step is the tokenize method. It is broken into a list for processing. Then evaluate_expression is called passing in the token list that was created, which is the main function of this program. Number values become appended to the values list, and operators become appended to the operators list. While iterating through these values, parentheses are focused on first, and the precedence of each operator is calculated to inform the program which order to perform the expressions in. The expressions are performed in the proper order within the parentheses, then once there are no remaining parentheses, they are performed among all the remaining values. This is all done with the apply_operator method. Once there is one remaining value, it is returned as the final answer and printed to the screen. 