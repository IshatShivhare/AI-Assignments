import random
import numpy as np
import matplotlib.pyplot as plt

"""
Hill Climbing Algorithm Example
Scenario: Finding the maximum value of a mathematical function
Function: Combination of multiple normal distributions

Algorithm Steps:
1. Start with an initial guess (x0).
2. Evaluate the function at the current point.
3. Move to a neighboring point with a higher function value.
4. Repeat steps 2-3 until no higher neighboring point is found.
"""

def hill_climbing(function, initial_guess, step_size, max_iterations):
    current_point = initial_guess
    current_value = function(current_point)
    
    for _ in range(max_iterations):
        neighbors = [current_point + step_size, current_point - step_size]
        next_point = max(neighbors, key=function)
        next_value = function(next_point)
        
        if next_value <= current_value:
            break
        
        current_point, current_value = next_point, next_value
    
    return current_point, current_value

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
    initial_guess = random.uniform(-3, 3)
    step_size = 0.1
    max_iterations = 1000
    
    optimal_point, optimal_value = hill_climbing(multi_normal_function, initial_guess, step_size, max_iterations)
    print(f"Optimal point: {optimal_point}")
    print(f"Optimal value: {optimal_value}")

    plot_function()
