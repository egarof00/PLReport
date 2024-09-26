from lark import Lark, Transformer
import sys

# Load the grammar from grammarl.lark
with open("grammar.lark", "r") as grammar_file:
    grammar = grammar_file.read()

# Create a Lark parser
parser = Lark(grammar, parser='lalr')

# Define an AST transformer
# In this special case the transformer is the identity function
class CalcTransformer(Transformer):
    def plus(self, items):
        return ('plus', items[0], items[1])
    
    def minus(self, items):
        return ('minus', items[0], items[1])
    
    def times(self, items):
        return ('times', items[0], items[1])
    
    def negative(self, items):
        return ('negative', items[0])
    
    def num(self, items):
        return ('num', float(items[0]))
    
    def exponent(self, items):
        return ('exponent', items[0], items[1])

# Function to evaluate the AST
def evaluate(ast):
    if ast[0] == 'plus':
        return evaluate(ast[1]) + evaluate(ast[2])
    elif ast[0] == 'minus':
        return evaluate(ast[1]) - evaluate(ast[2])
    elif ast[0] == 'times':
        return evaluate(ast[1]) * evaluate(ast[2])
    elif ast[0] == 'negative':
        return (-1 * evaluate(ast[1])) 
    elif ast[0] == 'num':
        return ast[1]
    elif ast[0] == 'exponent':
        return evaluate(ast[1]) ** evaluate(ast[2])
    else:
        raise ValueError(f"Unknown operation: {ast}")
    

# Main execution
if __name__ == "__main__":
    calc_transformer = CalcTransformer() 
    input_string = sys.argv[1]
    tree = parser.parse(input_string)  # Add this line
    #print(tree)
    ast = calc_transformer.transform(tree)
    #print(ast)
    result = evaluate(ast)
    print(result)
