import itertools

class Sentence:
    def evaluate(self, model):
        raise NotImplementedError

    def symbols(self):
        raise NotImplementedError

class Symbol(Sentence):
    def __init__(self, name):
        self.name = name

    def evaluate(self, model):
        return model[self.name]

    def symbols(self):
        return {self.name}

    def __repr__(self):
        return self.name

class Not(Sentence):
    def __init__(self, operand):
        self.operand = operand

    def evaluate(self, model):
        return not self.operand.evaluate(model)

    def symbols(self):
        return self.operand.symbols()

    def __repr__(self):
        return f"¬{self.operand}"

class And(Sentence):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, model):
        return self.left.evaluate(model) and self.right.evaluate(model)

    def symbols(self):
        return self.left.symbols().union(self.right.symbols())

    def __repr__(self):
        return f"({self.left} ∧ {self.right})"

class Or(Sentence):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, model):
        return self.left.evaluate(model) or self.right.evaluate(model)

    def symbols(self):
        return self.left.symbols().union(self.right.symbols())

    def __repr__(self):
        return f"({self.left} ∨ {self.right})"

class Implication(Sentence):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, model):
        return not self.left.evaluate(model) or self.right.evaluate(model)

    def symbols(self):
        return self.left.symbols().union(self.right.symbols())

    def __repr__(self):
        return f"({self.left} → {self.right})"

class Biconditional(Sentence):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, model):
        return self.left.evaluate(model) == self.right.evaluate(model)

    def symbols(self):
        return self.left.symbols().union(self.right.symbols())

    def __repr__(self):
        return f"({self.left} ↔ {self.right})"
    
class PropositionalEvaluator:
    def __init__(self):
        """Initialize the propositional logic evaluator"""
        pass
    
    def get_symbols(self, expression):
        """Extract all unique symbols from an expression"""
        return sorted(list(expression.symbols()))
    
    def generate_truth_assignments(self, symbols):
        """Generate all possible truth value combinations for given symbols"""
        n = len(symbols)
        assignments = []
        for i in range(2**n):
            assignment = {}
            for j, symbol in enumerate(symbols):
                # Use bit manipulation to generate combinations
                assignment[symbol] = bool(i & (1 << (n-j-1)))
            assignments.append(assignment)
        return assignments
    
    def evaluate_expression(self, expression, assignment):
        """Evaluate an expression with given truth assignments"""
        return expression.evaluate(assignment)
    
    def print_truth_table(self, expression):
        """Print truth table for a given expression"""
        symbols = self.get_symbols(expression)
        assignments = self.generate_truth_assignments(symbols)
        
        # Print header
        header = " ".join([f"{sym:^5}" for sym in symbols])
        header += f" | {str(expression.formula()):^10}"
        print(header)
        print("-" * len(header))
        
        # Print rows
        for assignment in assignments:
            # Print symbol values
            row = " ".join([f"{'T' if assignment[sym] else 'F':^5}" for sym in symbols])
            # Print result
            result = self.evaluate_expression(expression, assignment)
            row += f" | {'T' if result else 'F':^10}"
            print(row)
    
    