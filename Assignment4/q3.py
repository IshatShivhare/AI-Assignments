from logic import *
logic = LogicalReasoning()

P = Symbol("P")
Q = Symbol("Q")
R = Symbol("R")
S = Symbol("S")

# Problem A
print("\nProblem A:")

knowledge_a = And(
    Or(P, Q),
    Implication(P, R),
    Implication(Q, S),
    Implication(R, S)
)
    
print(logic.solve_problem('resolution', knowledge_a, S))

# Problem B    
print("\nProblem B:")

knowledge_b = And(
    Implication(P, Q),
    Implication(Q, R),
    Implication(S, Not(R)),
    P
)
    
print(logic.solve_problem('resolution', knowledge_b, S))