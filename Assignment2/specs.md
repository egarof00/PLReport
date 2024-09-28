# Assignment 2: CPSC 354

**Name:** Emma Garofalo

**Email:** garofalo@chapman.edu

**Section:** 2

## Included Files:
* calculator_cfg.py
* grammar.lark

### calculator_cfg.py
Sections and purposes:
* **class CalcTransformer(Transformer):** 
    This identity function defines the abstract syntax tree for the calculator. For every single existing operation, there is a transformer function that returns the necessary information to perform each operation along with a value that corresponds with the evaluate method described below.
* **evaluate(ast):**
    Depending on what was returned from the AST transformer, this method performs the corresponding operation. If it is given an operation that has not been defined, it will notify the user that that operation is unknown. 
* **Main execution:**
    The main of this program creates an instance of the transformer, then takes the given input string from the user, creating a tree then ast from that tree that is then evaluated, returning the single value that is the answer to the given math expression.


### grammar.lark
* **Breaking down the grammar:**
    When analyzing this cfg, the order of the operations will be performed from the rule furthest from the "start", then finish at the "start" step. My first rule handles parenthesis. Then my order of operations continues to logarithm, exponent, negative, multiplication, then addition and subtraction. Logarithm is handled before exponent as it's inverse operation. A notable thing to point out is that the exponent operation is given right to left precedence, so if an expression like "5^2^3" is given to the program, the "2^3" portion is handled first to be sure that the correct answer is given. Negative must come after the exponent step so that expressions like "-3^2" can be handled properly. The rest of the grammar follows normal PEMDAS, giving precedence to multiplication before addition and subtraction which are handled in the same level from left to right.

