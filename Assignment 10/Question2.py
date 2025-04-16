"""
This script solves the 8-Queens problem using CSP.
Each queen is placed in a unique row, and the column positions are assigned such that
no two queens are in the same column or diagonal.

All valid solutions are written to a text file.
"""

from constraint import Problem, AllDifferentConstraint

def solve_8_queens(file):
    """
    Solves the 8-Queens problem using constraint satisfaction.

    Args:
        file (file object): File object to write the solutions.

    Returns:
        None
    """
    problem = Problem()

    # Define rows and columns for the chessboard
    rows = range(8)  # Rows are numbered 0 to 7
    cols = range(8)  # Columns are numbered 0 to 7

    # Each variable represents a row; its value is the column position of the queen
    problem.addVariables(rows, cols)

    # Constraint: No two queens can be in the same column
    problem.addConstraint(AllDifferentConstraint())

    # Constraint: No two queens can be on the same diagonal
    for r1 in rows:
        for r2 in rows:
            if r1 < r2:
                # Ensure the absolute difference in columns is not equal to the difference in rows
                problem.addConstraint(lambda c1, c2, r1=r1, r2=r2: abs(c1 - c2) != abs(r1 - r2), (r1, r2))

    # Get all valid solutions
    solutions = problem.getSolutions()

    # Write the results to the file
    file.write("=== 8-Queens Problem ===\n")
    file.write(f"Total Solutions: {len(solutions)}\n\n")

    for idx, sol in enumerate(solutions, 1):
        # Write each solution in a readable format
        file.write(f"Solution {idx}:\n")
        for row in sorted(sol):
            file.write(f"  Row {row}: Column {sol[row]}\n")
        file.write("\n")

# Main execution block
if __name__ == "__main__":
    # Open the output file to write solutions
    with open("Assignment 10/Question2sol.txt", "w") as f:
        solve_8_queens(f)

    print("Solutions written to 'Question2sol.txt'")
