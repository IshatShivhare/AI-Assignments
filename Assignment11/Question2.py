from collections import deque

# Initial domains
domains = {
    'A': {1, 2, 3},
    'B': {2, 3, 4},
    'C': {3, 4, 5},
    'D': {1, 3, 5},
    'E': {2, 4, 6}
}

# Constraints as functions
def constraint_A_B(a, b):
    return a < b

def constraint_B_C(b, c):
    return b != c

def constraint_C_D(c, d):
    return c == d + 2

def constraint_D_E(d, e):
    return d < e

def constraint_A_E(a, e):
    return a + e == 6

# Arc format: (Xi, Xj, constraint_function)
constraints = [
    ('A', 'B', constraint_A_B),
    ('B', 'A', lambda b, a: constraint_A_B(a, b)),
    ('B', 'C', constraint_B_C),
    ('C', 'B', constraint_B_C),
    ('C', 'D', lambda c, d: constraint_C_D(c, d)),
    ('D', 'C', lambda d, c: constraint_C_D(c, d)),
    ('D', 'E', constraint_D_E),
    ('E', 'D', lambda e, d: constraint_D_E(d, e)),
    ('A', 'E', constraint_A_E),
    ('E', 'A', lambda e, a: constraint_A_E(a, e))
]

def revise(xi, xj, constraint_fn):
    revised = False
    to_remove = set()
    for x in domains[xi]:
        if not any(constraint_fn(x, y) for y in domains[xj]):
            to_remove.add(x)
            revised = True
    if revised:
        domains[xi] -= to_remove
    return revised

def ac3():
    queue = deque(constraints)
    while queue:
        xi, xj, constraint_fn = queue.popleft()
        if revise(xi, xj, constraint_fn):
            if not domains[xi]:
                return False  # Inconsistency found
            for (xk, _, cf) in constraints:
                if xk != xi and (xk, xi, cf) in constraints:
                    queue.append((xk, xi, cf))
    return True

# Run AC-3
if ac3():
    print("AC-3 completed successfully.")
    print("Final domains:")
    for var in sorted(domains):
        print(f"{var}: {domains[var]}")
else:
    print("Inconsistent CSP: no solution exists.")

# Attempt to find one valid assignment (brute-force within reduced domains)
from itertools import product

print("\nOne possible solution:")
for A, B, C, D, E in product(domains['A'], domains['B'], domains['C'], domains['D'], domains['E']):
    if (A < B and B != C and C == D + 2 and D < E and A + E == 6):
        print(f"A={A}, B={B}, C={C}, D={D}, E={E}")
        break
else:
    print("No solution found.")
