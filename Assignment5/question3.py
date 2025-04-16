'''
    3) Write a program to solve the following Predicate logic with facts and rules using the
    method Resolution and proof of refutation/contradiction.
    We need to prove whether John is happy.
    Facts:
    ● Loves(John,Mary)
    ● Loves(Mary,John)
    ● ∀x (Kind(x)→Loves(x,Everyone)) (If someone is kind, they love everyone.)
    ● Kind(John) (John is kind.)
    Rules:
    ● ∀x∀y(Loves(x,y)→Happy(x)) (If someone loves someone, that person is
    happy.)
    ● ∀x (Happy(x)→Smiles(x)) (If someone is happy, they smile.)
    ● ∀x (Smiles(x)→Friendly(x)) (If someone smiles, they are friendly.)
    ● ∀x (Friendly(x)→¬Sad(x)) (If someone is friendly, they are not sad.)
    ● ∀x (Sad(x)→¬Happy(x)) (If someone is sad, they are not happy.)
'''

# Facts and Rules in CNF (Conjunctive Normal Form)
clauses = [
    {"Loves(John,Mary)"},
    {"Loves(Mary,John)"},
    {"¬Kind(x)", "Loves(x,Everyone)"},
    {"Kind(John)"},
    {"¬Loves(x,y)", "Happy(x)"},
    {"¬Happy(x)", "Smiles(x)"},
    {"¬Smiles(x)", "Friendly(x)"},
    {"¬Friendly(x)", "¬Sad(x)"},
    {"¬Sad(x)", "¬Happy(x)"},
]

# Resolution Algorithm
def resolve(c1, c2):
    resolvents = set()
    for literal1 in c1:
        for literal2 in c2:
            if literal1 == "¬" + literal2 or "¬" + literal1 == literal2:
                resolvent = (c1 - {literal1}) | (c2 - {literal2})
                resolvents.add(frozenset(resolvent))
    return resolvents

def resolution(clauses, goal):
    clauses = [frozenset(clause) for clause in clauses]
    neg_goal = frozenset({f"¬{goal}"})
    clauses.append(neg_goal)
    new_clauses = set(clauses)
    while True:
        new = set()
        for c1 in new_clauses:
            for c2 in new_clauses:
                if c1 != c2:
                    resolvents = resolve(c1, c2)
                    if frozenset() in resolvents:
                        return True
                    new.update(resolvents)
        if new.issubset(new_clauses):
            return False
        new_clauses.update(new)

# Run Resolution
goal = "Happy(John)"
result = resolution(clauses, goal)
print("\nResolution Result:")
print(f"{goal}: {result}")