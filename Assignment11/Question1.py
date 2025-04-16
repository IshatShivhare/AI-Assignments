from collections import deque

# Variables and domains
variables = ['A', 'B', 'C']
domains = {
    'A': {'Red', 'Green', 'Blue'},
    'B': {'Red', 'Green', 'Blue'},
    'C': {'Red', 'Green', 'Blue'}
}

# Constraints: adjacency (i.e., inequality)
constraints = {
    ('A', 'B'),
    ('B', 'A'),
    ('B', 'C'),
    ('C', 'B'),
    ('A', 'C'),
    ('C', 'A')
}

def revise(xi, xj):
    revised = False
    to_remove = set()
    for x in domains[xi]:
        if not any(x != y for y in domains[xj]):
            to_remove.add(x)
            revised = True
    domains[xi] -= to_remove
    return revised

def ac3():
    queue = deque(constraints)
    while queue:
        (xi, xj) = queue.popleft()
        if revise(xi, xj):
            if not domains[xi]:
                return False  # Domain wiped out => inconsistency
            for xk in variables:
                if xk != xi and (xk, xi) in constraints:
                    queue.append((xk, xi))
    return True

# Run the AC-3 algorithm
if ac3():
    print("AC-3 completed successfully. Final domains:")
    for var in variables:
        print(f"{var}: {domains[var]}")
else:
    print("AC-3 found an inconsistency. No solution exists.")
