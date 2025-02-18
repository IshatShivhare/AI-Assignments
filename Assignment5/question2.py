'''
    2) Write a program to solve the following Predicate logic with facts and rules using
    Backward Chaining.
    We want to prove that Socrates is mortal.
    Facts:
    ● Human(Socrates)
    Rules:
    ● ∀x (Human(x) → Mortal(x)) (All humans are mortal)
'''

# Facts
facts = {
    "Mortal(Socrates)": True,
}

# Rules
rules = [
    ("Human(x)", "Mortal(x)"),  # ∀x (Human(x) → Mortal(x))
]
0
# Backward Chaining Algorithm
def backward_chaining(goal, facts, rules):
    if goal in facts:
        return True
    for rule in rules:
        premise, conclusion = rule
        if conclusion == goal:
            premise_instance = premise.replace("x", goal.split("(")[1].split(")")[0])
            if backward_chaining(premise_instance, facts, rules):
                return True
    return False

# Run Backward Chaining
goal = "Mortal(Socrates)"
result = backward_chaining(goal, facts, rules)
print("\nBackward Chaining Result:")
print(f"{goal}: {result}")