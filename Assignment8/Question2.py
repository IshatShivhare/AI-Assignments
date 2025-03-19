import random
import math
import numpy as np  
import matplotlib.pyplot as plt

"""
Simulated Annealing Algorithm Example
Scenario: Finding the maximum value of a mathematical function
Function: Combination of multiple normal distributions
The goal is to find the value of x that maximizes the function.

Algorithm Steps:
1. Start with an initial guess (x0) and an initial temperature.
2. Evaluate the function at the current point.
3. Move to a neighboring point with a probability that depends on the temperature and the change in function value.
4. Gradually decrease the temperature and repeat steps 2-3 until the temperature is sufficiently low.

Inputs:
- Initial guess (x0)
- Initial temperature
- Cooling rate
- Maximum number of iterations
"""

def simulated_annealing(function, initial_guess, initial_temp, cooling_rate, max_iterations):
    current_point = initial_guess
    current_value = function(current_point)
    temperature = initial_temp

    for _ in range(max_iterations):
        if temperature <= 0:
            break

        # Generate a neighboring point
        next_point = current_point + random.uniform(-1, 1)
        next_value = function(next_point)

        # Calculate the acceptance probability
        delta_value = next_value - current_value
        acceptance_probability = math.exp(delta_value / temperature) if delta_value < 0 else 1

        # Decide whether to move to the neighboring point
        if random.random() < acceptance_probability:
            current_point, current_value = next_point, next_value

        # Cool down the temperature
        temperature *= cooling_rate

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
    initial_temp = 1000
    cooling_rate = 0.99
    max_iterations = 1000

    optimal_point, optimal_value = simulated_annealing(multi_normal_function, initial_guess, initial_temp, cooling_rate, max_iterations)
    print(f"Optimal point: {optimal_point}")
    print(f"Optimal value: {optimal_value}")

    plot_function()
