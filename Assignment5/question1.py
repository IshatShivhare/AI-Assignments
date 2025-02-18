'''
    1) Write a program to solve the following Predicate logic with facts and rules using Forward
    Chaining.
    We want to reason about mammals, animals, and whether they have fur.
    Facts:
    ● Mammal(Tom)
    ● Mammal(Jerry)
    ● Animal(Tom)
    ● Animal(Jerry)
    Rules:
    ● ∀x (Mammal(x) → HasFur(x)) (All mammals have fur)
    ● ∀x (Animal(x) → Alive(x)) (All animals are alive)
'''

from collections import defaultdict

# Facts
facts = {
    "Mammal(Tom)": True,
    "Mammal(Jerry)": True,
    "Animal(Tom)": True,
    "Animal(Jerry)": True,
}

# Rules
rules = [
    ("Mammal(x)", "HasFur(x)"),  # ∀x (Mammal(x) → HasFur(x))
    ("Animal(x)", "Alive(x)"),   # ∀x (Animal(x) → Alive(x))
]

# Forward Chaining Algorithm
def forward_chaining(facts, rules):
    new_facts = True
    while new_facts:
        new_facts = False
        for rule in rules:
            premise, conclusion = rule
            for fact in list(facts.keys()):
                if premise.replace("x", fact.split("(")[1].split(")")[0]) == fact:
                    new_fact = conclusion.replace("x", fact.split("(")[1].split(")")[0])
                    if new_fact not in facts:
                        facts[new_fact] = True
                        new_facts = True
    return facts

# Run Forward Chaining
updated_facts = forward_chaining(facts, rules)
print("Forward Chaining Results:")
for fact, value in updated_facts.items():
    print(f"{fact}: {value}")