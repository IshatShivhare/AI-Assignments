import random
import numpy as np
import matplotlib.pyplot as plt

"""
Local Beam Search Algorithm Example
Scenario: Finding the maximum value of a mathematical function
Function: Combination of multiple normal distributions
The goal is to find the value of x that maximizes the function.

Algorithm Steps:
1. Start with K initial random guesses.
2. Evaluate the function at each point.
3. Generate all neighbors of the current K points.
4. Select the K best neighbors.
5. Repeat steps 3-4 until convergence or maximum iterations.

Inputs:
- Number of beams (K)
- Step size for moving to neighboring points
- Maximum number of iterations

Outputs:
- Optimal point: The value of x that maximizes the function.
- Optimal value: The maximum value of the function.
"""

def local_beam_search(function, K, step_size, max_iterations):

    # Initialize K random guesses
    current_points = [random.uniform(-3, 3) for _ in range(K)]
    current_values = [function(point) for point in current_points]

    for _ in range(max_iterations):
        # Generate all neighbors of the current K points
        neighbors = []
        for point in current_points:
            neighbors.append(point + step_size)
            neighbors.append(point - step_size)

        # Evaluate the function at each neighbor
        neighbor_values = [function(neighbor) for neighbor in neighbors]

        # Select the K best neighbors
        combined = list(zip(neighbors, neighbor_values))
        combined.sort(key=lambda x: x[1], reverse=True)
        current_points, current_values = zip(*combined[:K])

    # Return the best point found
    best_index = current_values.index(max(current_values))
    return current_points[best_index], current_values[best_index]

def multi_normal_function(x):
    # Combine multiple normal distributions (peaks and valleys)
    mu1, sigma1 = 1, 0.5  # Mean and standard deviation for the first normal distribution
    mu2, sigma2 = -1, 0.8  # Mean and standard deviation for the second normal distribution
    mu3, sigma3 = 2, 0.3  # Mean and standard deviation for the third normal distribution
    
    # Normal distributions: e^(-(x - mu)^2 / (2 * sigma^2))
    peak1 = np.exp(-(x - mu1)**2 / (2 * sigma1**2))
    peak2 = np.exp(-(x - mu2)**2 / (2 * sigma2**2))
    peak3 = np.exp(-(x - mu3)**2 / (2 * sigma3**2))
    
    # Sum of multiple normal distributions
    return peak1 + peak2 + peak3

def plot_function():
    x = np.linspace(-5, 5, 1000)
    y = np.array([multi_normal_function(xi) for xi in x])
    plt.plot(x, y, label='Combination of Normal Distributions')
    plt.title("Combination of Normal Distributions with Multiple Peaks")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    K = 3
    step_size = 0.1
    max_iterations = 1000

    optimal_point, optimal_value = local_beam_search(multi_normal_function, K, step_size, max_iterations)
    print(f"Optimal point: {optimal_point}")
    print(f"Optimal value: {optimal_value}")

    plot_function()
