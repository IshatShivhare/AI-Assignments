<<<<<<< HEAD
from logic import *


def evaluate_questions(self):
        """Evaluate and print truth tables for all assignment questions"""
        # Define basic symbols
        P = Symbol("P")
        Q = Symbol("Q")
        R = Symbol("R")
        
        # List of expressions from questions
        expressions = [
            # 1. ~P->Q
            Implication(Not(P), Q),
            
            # 2. ~P ∧ ~Q
            And(Not(P), Not(Q)),
            
            # 3. ~P ∨ ~Q
            Or(Not(P), Not(Q)),
            
            # 4. ~P->~Q
            Implication(Not(P), Not(Q)),
            
            # 5. ~P <-> ~Q
            Biconditional(Not(P), Not(Q)),
            
            # 6. (P ∨ Q)∧(~P->Q)
            And(Or(P, Q), Implication(Not(P), Q)),
            
            # 7. ((P ∨ Q)->~R)
            Implication(Or(P, Q), Not(R)),
            
            # 8. (((P ∨ Q)->~R) <-> ((~P∧~Q)->~R))
            Biconditional(
                Implication(Or(P, Q), Not(R)),
                Implication(And(Not(P), Not(Q)), Not(R))
            ),
            
            # 9. (((P->Q)∧(Q->R))->(Q->R))
            Implication(
                And(Implication(P, Q), Implication(Q, R)),
                Implication(Q, R)
            ),
            
            # 10. (((P->(Q∨R)) -> (~P∧~Q∧~R)))
            Implication(
                Implication(P, Or(Q, R)),
                And(Not(P), And(Not(Q), Not(R)))
            )
        ]
        
        # Print truth table for each expression
        for i, expr in enumerate(expressions, 1):
            print(f"\nQuestion {i}:")
            print(f"Expression: {expr.formula()}")
            self.print_truth_table(expr)

def main():
    # Create evaluator instance
    evaluator = PropositionalEvaluator()
    
    # Evaluate all questions
    evaluator.evaluate_questions()
    
    # Example of evaluating a single expression
    P = Symbol("P")
    Q = Symbol("Q")
    expr = Implication(Not(P), Q)
    print("\nExample single expression:")
    print(f"Expression: {expr.formula()}")
    evaluator.print_truth_table(expr)

if __name__ == "__main__":
    main()
=======
from logic import *
import itertools
import re

def parse_formula(formula, symbols_map):
    """Parses a logical formula from a string into an expression tree."""
    
    formula = formula.replace(" ", "")  # Remove spaces
    
    # Handle parentheses
    while formula.startswith("(") and formula.endswith(")"):
        formula = formula[1:-1]

    # If it's a single symbol, return it as a Symbol object
    if formula in symbols_map:
        return symbols_map[formula]

    # Handle NOT (~)
    if formula.startswith("~"):
        return Not(parse_formula(formula[1:], symbols_map))

    # Find main logical operator
    depth = 0
    for i in range(len(formula) - 1, -1, -1):
        if formula[i] == ")":
            depth += 1
        elif formula[i] == "(":
            depth -= 1
        elif depth == 0:
            if formula[i:i+2] == "->":  # Implication
                left = parse_formula(formula[:i], symbols_map)
                right = parse_formula(formula[i+2:], symbols_map)
                return Implication(left, right)
            elif formula[i] == "∧" or formula[i] == "^":  # AND
                left = parse_formula(formula[:i], symbols_map)
                right = parse_formula(formula[i+1:], symbols_map)
                return And(left, right)
            elif formula[i] == "∨" or formula[i] == "^":  # OR
                left = parse_formula(formula[:i], symbols_map)
                right = parse_formula(formula[i+1:], symbols_map)
                return Or(left, right)
            elif formula[i:i+3] == "<=>":  # Biconditional
                left = parse_formula(formula[:i], symbols_map)
                right = parse_formula(formula[i+3:], symbols_map)
                return Biconditional(left, right)

    raise ValueError(f"Invalid formula: {formula}")

def generate_truth_table(expression):
    """Generates a truth table for a given logical expression."""
    symbols = sorted(expression.symbols())  # Extract symbols
    truth_values = list(itertools.product([False, True], repeat=len(symbols)))

    # Print header
    print(" | ".join(symbols) + " | " + str(expression))
    print("-" * (7 * len(symbols) + 10))

    # Print rows
    for values in truth_values:
        model = dict(zip(symbols, values))
        result = expression.evaluate(model)
        values_str = " | ".join(str(v).ljust(5) for v in values)
        print(f"{values_str} | {result}")

if __name__ == "__main__":
    # Take input from the user
    formula_str = input("Enter a logical formula: ")

    # Extract unique symbols
    symbols_set = sorted(set(re.findall(r'[A-Z]', formula_str)))  # Extract uppercase letters (P, Q, R, etc.)
    symbols_map = {s: Symbol(s) for s in symbols_set}  # Create Symbol objects

    # Parse the formula into an expression tree
    try:
        expression = parse_formula(formula_str, symbols_map)
        generate_truth_table(expression)
    except Exception as e:
        print(f"Error: {e}")
>>>>>>> main
