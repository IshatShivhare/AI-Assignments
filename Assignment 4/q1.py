from logic import *

logic = LogicalReasoning()
print("Question 1:")
P = Symbol("P")
Q = Symbol("Q")
A = Symbol("A")
B = Symbol("B")
M = Symbol("M")
L = Symbol("L")


knowledge = And((Implication(P, Q)), 
                Implication(And(L, M), P),
                Implication(And(A, B), L),
                A,
                B,
                M
)

print(logic.forward_chaining(knowledge, Q))

print("Question 2:")
A = Symbol("A")
B = Symbol("B")
C = Symbol("C")
D = Symbol("D")
E = Symbol("E")
F = Symbol("F")


knowledge = And((Implication(A, B)), 
                Implication(B, C),
                Implication(C, D),
                Implication(And(D, E), F),
                E
)

print(logic.forward_chaining(knowledge, F))