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