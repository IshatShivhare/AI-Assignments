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