from logic import *

logic = LogicalReasoning()

print("Question 1:")
A = Symbol("A")
B = Symbol("B")
P = Symbol("P")
Q = Symbol("Q")
R = Symbol("R")

knowledge = And((Implication(P, Q)),
                Implication(Q, R),
                Implication(A, P),
                Implication(B, R),
                A,
                B
)

print(logic.backward_chaining(knowledge, Q))


print("Question 2:")
A = Symbol("A")
B = Symbol("B")
C = Symbol("C")
D = Symbol("D")
E = Symbol("E")

knowledge = And((Implication(A, B)),
                Implication(And(B, C), D),
                Implication(E, C),
                A,
                E
)

print(logic.backward_chaining(knowledge, D))
