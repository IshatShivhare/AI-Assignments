"""
This script models the map of Australia as a Constraint Satisfaction Problem (CSP),
where each state must be assigned a color such that no two adjacent states share the same color.
It defines the states, their neighbors, and constraints, then finds all valid colorings
using 2 (Black, White), 3 (Red, Green, Blue), and 4 (Cyan, Magenta, Yellow, Black) colors.

The results (all possible solutions for each coloring case) are saved in a text file.
"""

from constraint import Problem

# List of Australian states
states = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

# Dictionary defining neighboring states
neighbors = {
    "WA": ["NT", "SA"],  # Western Australia neighbors
    "NT": ["WA", "SA", "Q"],  # Northern Territory neighbors
    "SA": ["WA", "NT", "Q", "NSW", "V"],  # South Australia neighbors
    "Q": ["NT", "SA", "NSW"],  # Queensland neighbors
    "NSW": ["SA", "Q", "V"],  # New South Wales neighbors
    "V": ["SA", "NSW"],  # Victoria neighbors
    "T": []  # Tasmania has no neighbors
}

def solve_map_coloring(colors, color_names, file):
    """
    Solves the map coloring problem for the given number of colors.

    Args:
        colors (list): List of integers representing color indices.
        color_names (list): List of color names corresponding to the indices.
        file (file object): File object to write the solutions.

    Returns:
        None
    """
    problem = Problem()
    # Add variables for each state with the possible color indices
    problem.addVariables(states, colors)

    # Add constraints: adjacent states must have different colors
    for state, adj in neighbors.items():
        for neighbor in adj:
            # Constraint to ensure adjacent states have different colors
            problem.addConstraint(lambda a, b: a != b, (state, neighbor))

    # Get all possible solutions
    solutions = problem.getSolutions()

    # Write the results to the file
    file.write(f"\n{'='*20} {len(colors)} Colors: {', '.join(color_names)} {'='*20}\n")
    file.write(f"Total Solutions: {len(solutions)}\n\n")

    for i, sol in enumerate(solutions, 1):
        # Convert solution indices to readable color names
        readable = {k: color_names[v] for k, v in sol.items()}
        file.write(f"Solution {i}:\n")
        for state in sorted(states):
            file.write(f"  {state}: {readable[state]}\n")
        file.write("\n")

# Main execution block
if __name__ == "__main__":
    # Open the output file to write solutions
    with open("Assignment 10/Question1sol.txt", "w") as f:
        # Solve for 2 colors
        solve_map_coloring([0, 1], ["Black", "White"], f)
        # Solve for 3 colors
        solve_map_coloring([0, 1, 2], ["Red", "Green", "Blue"], f)
        # Solve for 4 colors
        solve_map_coloring([0, 1, 2, 3], ["Cyan", "Magenta", "Yellow", "Black"], f)

    print("Solutions written to 'Question1sol.txt'")