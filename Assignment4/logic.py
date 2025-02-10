import itertools


class Sentence():

    def evaluate(self, model):
        """Evaluates the logical sentence."""
        raise Exception("nothing to evaluate")

    def formula(self):
        """Returns string formula representing logical sentence."""
        return ""

    def symbols(self):
        """Returns a set of all symbols in the logical sentence."""
        return set()

    @classmethod
    def validate(cls, sentence):
        if not isinstance(sentence, Sentence):
            raise TypeError("must be a logical sentence")

    @classmethod
    def parenthesize(cls, s):
        """Parenthesizes an expression if not already parenthesized."""
        def balanced(s):
            """Checks if a string has balanced parentheses."""
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    if count <= 0:
                        return False
                    count -= 1
            return count == 0
        if not len(s) or s.isalpha() or (
            s[0] == "(" and s[-1] == ")" and balanced(s[1:-1])
        ):
            return s
        else:
            return f"({s})"


class Symbol(Sentence):

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Symbol) and self.name == other.name

    def __hash__(self):
        return hash(("symbol", self.name))

    def __repr__(self):
        return self.name

    def evaluate(self, model):
        try:
            return bool(model[self.name])
        except KeyError:
            raise EvaluationException(f"variable {self.name} not in model")

    def formula(self):
        return self.name

    def symbols(self):
        return {self.name}


class Not(Sentence):
    def __init__(self, operand):
        Sentence.validate(operand)
        self.operand = operand

    def __eq__(self, other):
        return isinstance(other, Not) and self.operand == other.operand

    def __hash__(self):
        return hash(("not", hash(self.operand)))

    def __repr__(self):
        return f"Not({self.operand})"

    def evaluate(self, model):
        return not self.operand.evaluate(model)

    def formula(self):
        return "¬" + Sentence.parenthesize(self.operand.formula())

    def symbols(self):
        return self.operand.symbols()


class And(Sentence):
    def __init__(self, *conjuncts):
        for conjunct in conjuncts:
            Sentence.validate(conjunct)
        self.conjuncts = list(conjuncts)

    def __eq__(self, other):
        return isinstance(other, And) and self.conjuncts == other.conjuncts

    def __hash__(self):
        return hash(
            ("and", tuple(hash(conjunct) for conjunct in self.conjuncts))
        )

    def __repr__(self):
        conjunctions = ", ".join(
            [str(conjunct) for conjunct in self.conjuncts]
        )
        return f"And({conjunctions})"

    def add(self, conjunct):
        Sentence.validate(conjunct)
        self.conjuncts.append(conjunct)

    def evaluate(self, model):
        return all(conjunct.evaluate(model) for conjunct in self.conjuncts)

    def formula(self):
        if len(self.conjuncts) == 1:
            return self.conjuncts[0].formula()
        return " ∧ ".join([Sentence.parenthesize(conjunct.formula())
                           for conjunct in self.conjuncts])

    def symbols(self):
        return set.union(*[conjunct.symbols() for conjunct in self.conjuncts])


class Or(Sentence):
    def __init__(self, *disjuncts):
        for disjunct in disjuncts:
            Sentence.validate(disjunct)
        self.disjuncts = list(disjuncts)

    def __eq__(self, other):
        return isinstance(other, Or) and self.disjuncts == other.disjuncts

    def __hash__(self):
        return hash(
            ("or", tuple(hash(disjunct) for disjunct in self.disjuncts))
        )

    def __repr__(self):
        disjuncts = ", ".join([str(disjunct) for disjunct in self.disjuncts])
        return f"Or({disjuncts})"

    def evaluate(self, model):
        return any(disjunct.evaluate(model) for disjunct in self.disjuncts)

    def formula(self):
        if len(self.disjuncts) == 1:
            return self.disjuncts[0].formula()
        return " ∨ ".join([Sentence.parenthesize(disjunct.formula())
                            for disjunct in self.disjuncts])

    def symbols(self):
        return set.union(*[disjunct.symbols() for disjunct in self.disjuncts])


class Implication(Sentence):
    def __init__(self, antecedent, consequent):
        Sentence.validate(antecedent)
        Sentence.validate(consequent)
        self.antecedent = antecedent
        self.consequent = consequent

    def __eq__(self, other):
        return (isinstance(other, Implication)
                and self.antecedent == other.antecedent
                and self.consequent == other.consequent)

    def __hash__(self):
        return hash(("implies", hash(self.antecedent), hash(self.consequent)))

    def __repr__(self):
        return f"Implication({self.antecedent}, {self.consequent})"

    def evaluate(self, model):
        return ((not self.antecedent.evaluate(model))
                or self.consequent.evaluate(model))

    def formula(self):
        antecedent = Sentence.parenthesize(self.antecedent.formula())
        consequent = Sentence.parenthesize(self.consequent.formula())
        return f"{antecedent} => {consequent}"

    def symbols(self):
        return set.union(self.antecedent.symbols(), self.consequent.symbols())


class Biconditional(Sentence):
    def __init__(self, left, right):
        Sentence.validate(left)
        Sentence.validate(right)
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (isinstance(other, Biconditional)
                and self.left == other.left
                and self.right == other.right)

    def __hash__(self):
        return hash(("biconditional", hash(self.left), hash(self.right)))

    def __repr__(self):
        return f"Biconditional({self.left}, {self.right})"

    def evaluate(self, model):
        return ((self.left.evaluate(model)
                 and self.right.evaluate(model))
                or (not self.left.evaluate(model)
                    and not self.right.evaluate(model)))

    def formula(self):
        left = Sentence.parenthesize(str(self.left))
        right = Sentence.parenthesize(str(self.right))
        return f"{left} <=> {right}"

    def symbols(self):
        return set.union(self.left.symbols(), self.right.symbols())

class LogicalReasoning:
    def __init__(self):
        """Initialize the logical reasoning system"""
        pass
        
    def forward_chaining(self, knowledge, query):
        """
        Performs forward chaining to determine if knowledge base entails query.
        Returns True if query can be inferred, False otherwise.
        """
        kb_symbols = knowledge.symbols()
        known_facts = set()
        rules = []
        
        def extract_facts_and_rules(sentence):
            if isinstance(sentence, And):
                for conjunct in sentence.conjuncts:
                    extract_facts_and_rules(conjunct)
            elif isinstance(sentence, Implication):
                rules.append(sentence)
            elif isinstance(sentence, Symbol):
                known_facts.add(sentence.name)
        
        extract_facts_and_rules(knowledge)
        
        while True:
            new_facts = set()
            
            for rule in rules:
                if isinstance(rule.antecedent, Symbol):
                    if rule.antecedent.name in known_facts:
                        if isinstance(rule.consequent, Symbol):
                            new_facts.add(rule.consequent.name)
                elif isinstance(rule.antecedent, And):
                    all_known = True
                    for conjunct in rule.antecedent.conjuncts:
                        if isinstance(conjunct, Symbol):
                            if conjunct.name not in known_facts:
                                all_known = False
                                break
                    if all_known:
                        if isinstance(rule.consequent, Symbol):
                            new_facts.add(rule.consequent.name)
            
            if not new_facts - known_facts:
                break
                
            known_facts.update(new_facts)
        
        if isinstance(query, Symbol):
            return query.name in known_facts
        return False

    def backward_chaining(self, knowledge, query):
        """
        Performs backward chaining to determine if knowledge base entails query.
        Returns True if query can be proven, False otherwise.
        """
        def get_rules_for_conclusion(conclusion):
            matching_rules = []
            def check_sentence(sentence):
                if isinstance(sentence, And):
                    for conjunct in sentence.conjuncts:
                        check_sentence(conjunct)
                elif isinstance(sentence, Implication):
                    if isinstance(sentence.consequent, Symbol) and sentence.consequent.name == conclusion:
                        matching_rules.append(sentence)
            
            check_sentence(knowledge)
            return matching_rules
        
        def prove(goal, visited=None):
            if visited is None:
                visited = set()
                
            if goal in visited:
                return False
            visited.add(goal)
            
            def is_fact(sentence):
                if isinstance(sentence, Symbol):
                    return sentence.name == goal
                elif isinstance(sentence, And):
                    return any(is_fact(conjunct) for conjunct in sentence.conjuncts)
                return False
            
            if is_fact(knowledge):
                return True
                
            rules = get_rules_for_conclusion(goal)
            
            for rule in rules:
                if isinstance(rule.antecedent, Symbol):
                    if prove(rule.antecedent.name, visited.copy()):
                        return True
                elif isinstance(rule.antecedent, And):
                    all_proven = True
                    for conjunct in rule.antecedent.conjuncts:
                        if isinstance(conjunct, Symbol):
                            if not prove(conjunct.name, visited.copy()):
                                all_proven = False
                                break
                    if all_proven:
                        return True
                        
            return False
        
        if isinstance(query, Symbol):
            return prove(query.name)
        return False

    def to_cnf(self, sentence):
        """Convert a sentence to Conjunctive Normal Form (CNF)"""
        def distribute_or(s1, s2):
            if isinstance(s1, And):
                return And(*[distribute_or(c, s2) for c in s1.conjuncts])
            elif isinstance(s2, And):
                return And(*[distribute_or(s1, c) for c in s2.conjuncts])
            return Or(s1, s2)

        def eliminate_implications(sentence):
            if isinstance(sentence, Symbol):
                return sentence
            elif isinstance(sentence, Not):
                return Not(eliminate_implications(sentence.operand))
            elif isinstance(sentence, And):
                return And(*[eliminate_implications(c) for c in sentence.conjuncts])
            elif isinstance(sentence, Or):
                return Or(*[eliminate_implications(d) for d in sentence.disjuncts])
            elif isinstance(sentence, Implication):
                return Or(Not(eliminate_implications(sentence.antecedent)),
                         eliminate_implications(sentence.consequent))
            elif isinstance(sentence, Biconditional):
                s1 = eliminate_implications(sentence.left)
                s2 = eliminate_implications(sentence.right)
                return And(Or(Not(s1), s2), Or(Not(s2), s1))

        def move_not_inwards(sentence):
            if isinstance(sentence, Symbol):
                return sentence
            elif isinstance(sentence, Not):
                if isinstance(sentence.operand, Not):
                    return move_not_inwards(sentence.operand.operand)
                elif isinstance(sentence.operand, And):
                    return Or(*[move_not_inwards(Not(c)) for c in sentence.operand.conjuncts])
                elif isinstance(sentence.operand, Or):
                    return And(*[move_not_inwards(Not(d)) for d in sentence.operand.disjuncts])
                return sentence
            elif isinstance(sentence, And):
                return And(*[move_not_inwards(c) for c in sentence.conjuncts])
            elif isinstance(sentence, Or):
                return Or(*[move_not_inwards(d) for d in sentence.disjuncts])
            return sentence

        sentence = eliminate_implications(sentence)
        sentence = move_not_inwards(sentence)
        return sentence

    def get_clauses(self, sentence):
        """Convert CNF sentence to set of clauses"""
        if isinstance(sentence, And):
            clauses = set()
            for conjunct in sentence.conjuncts:
                clauses.update(self.get_clauses(conjunct))
            return clauses
        else:
            return {sentence}

    def resolve(self, ci, cj):
        """Perform resolution on two clauses"""
        clauses = set()
        
        if isinstance(ci, Symbol):
            ci_lits = {ci}
        elif isinstance(ci, Not):
            ci_lits = {ci}
        elif isinstance(ci, Or):
            ci_lits = set(ci.disjuncts)
        else:
            ci_lits = {ci}
            
        if isinstance(cj, Symbol):
            cj_lits = {cj}
        elif isinstance(cj, Not):
            cj_lits = {cj}
        elif isinstance(cj, Or):
            cj_lits = set(cj.disjuncts)
        else:
            cj_lits = {cj}

        for lit_i in ci_lits:
            for lit_j in cj_lits:
                if (isinstance(lit_i, Not) and lit_i.operand == lit_j) or \
                   (isinstance(lit_j, Not) and lit_j.operand == lit_i):
                    new_lits = (ci_lits | cj_lits) - {lit_i, lit_j}
                    if new_lits:
                        if len(new_lits) == 1:
                            clauses.add(new_lits.pop())
                        else:
                            clauses.add(Or(*new_lits))
                    else:
                        clauses.add(None)
        
        return clauses

    def resolution(self, knowledge_base, query):
        """
        Use resolution to determine if knowledge base entails query.
        Returns True if KB entails query (i.e., contradiction found), False otherwise.
        """
        clauses = self.get_clauses(self.to_cnf(knowledge_base))
        clauses.update(self.get_clauses(self.to_cnf(Not(query))))

        new = set()
        while True:
            pairs = [(ci, cj) for ci in clauses for cj in clauses if ci != cj]
            for ci, cj in pairs:
                resolvents = self.resolve(ci, cj)
                
                if any(resolvent is None for resolvent in resolvents):  
                    return True
                
                new.update(resolvents)

            if new.issubset(clauses):
                return False

            clauses.update(new)

    def solve_problem(self, problem_type, knowledge_base, query):
        """
        Solve logical reasoning problems using specified method
        problem_type: 'forward', 'backward', or 'resolution'
        """
        if problem_type == 'forward':
            return self.forward_chaining(knowledge_base, query)
        elif problem_type == 'backward':
            return self.backward_chaining(knowledge_base, query)
        elif problem_type == 'resolution':
            return self.resolution(knowledge_base, query)
        else:
            raise ValueError("Invalid problem type. Use 'forward', 'backward', or 'resolution'")
