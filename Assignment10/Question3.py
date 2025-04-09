"""
Cryptarithmetic Puzzle Solver using Constraint Satisfaction Problem (CSP) techniques.

Description:
-------------
This program solves cryptarithmetic puzzles of the form:

   WORD1
 + WORD2
 ---------
  RESULT

Each letter in the puzzle represents a unique digit (0-9), and no two letters can
represent the same digit. Additionally, no word can start with a zero.

The program uses the `python-constraint` library to solve the puzzle using CSP techniques.

Features:
- Takes user input for WORD1, WORD2, and RESULT.
- Automatically extracts unique letters.
- Applies CSP constraints: all letters must map to distinct digits, and leading letters cannot be zero.
- Uses backtracking search internally via the `python-constraint` solver.
"""

from constraint import Problem, AllDifferentConstraint

def solve_cryptarithmetic(word1, word2, result):
    """
    Solves a 2-word addition cryptarithmetic puzzle using CSP.

    Parameters:
    -----------
    word1 : str
        The first operand word
    word2 : str
        The second operand word
    result : str
        The result word

    Returns:
    --------
    None. Prints valid digit mappings that solve the puzzle.
    """

    # Normalize input
    word1, word2, result = word1.upper(), word2.upper(), result.upper()

    # Collect unique letters
    unique_letters = sorted(set(word1 + word2 + result))
    if len(unique_letters) > 10:
        raise ValueError("Too many unique letters! Cryptarithmetic puzzles must use 10 or fewer letters.")

    # Set up the constraint problem
    problem = Problem()

    # Add variables with domain 0–9
    problem.addVariables(unique_letters, range(10))

    # Ensure all letters are assigned different digits
    problem.addConstraint(AllDifferentConstraint(), unique_letters)

    # Add constraints: leading letters cannot be 0
    for word in [word1, word2, result]:
        problem.addConstraint(lambda l: l != 0, [word[0]])

    # Main arithmetic constraint
    def crypt_constraint(*args):
        letter_map = dict(zip(unique_letters, args))

        def word_to_number(word):
            return int(''.join(str(letter_map[c]) for c in word))

        num1 = word_to_number(word1)
        num2 = word_to_number(word2)
        total = word_to_number(result)

        return num1 + num2 == total

    # Add arithmetic constraint
    problem.addConstraint(crypt_constraint, unique_letters)

    # Solve the CSP
    solutions = problem.getSolutions()
    seen = set()

    if not solutions:
        print("❌ No solution found.")
        return

    print("\n✅ Solutions found:\n" + "-"*50)
    for sol in solutions:
        num1 = int(''.join(str(sol[c]) for c in word1))
        num2 = int(''.join(str(sol[c]) for c in word2))
        total = int(''.join(str(sol[c]) for c in result))
        if (num1, num2, total) not in seen:
            seen.add((num1, num2, total))
            print(f"{word1}: {num1}, {word2}: {num2}, {result}: {total} | Mapping: {sol}")
    print("-" * 50)

if __name__ == "__main__":
    print("🔢 Cryptarithmetic Puzzle Solver (Addition Only)")
    print("Enter three words for the equation: WORD1 + WORD2 = RESULT")
    
    word1 = input("Enter WORD1: ").strip()
    word2 = input("Enter WORD2: ").strip()
    result = input("Enter RESULT: ").strip()

    try:
        solve_cryptarithmetic(word1, word2, result)
    except Exception as e:
        print(f"Error: {e}")
