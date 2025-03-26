import random

# Parameters
POP_SIZE = 100  # Population size
MUTATION_RATE = 0.1  # Probability of mutation for each gene
GENERATIONS = 200  # Number of generations to run the algorithm
SEQ1 = "AGCTGAC"  # First DNA sequence
SEQ2 = "ACGTC"  # Second DNA sequence

# Generate a random alignment
def random_alignment(seq1, seq2):
    """
    Generates a random alignment for two sequences by randomly inserting gaps ('-').

    Args:
        seq1 (str): The first DNA sequence.
        seq2 (str): The second DNA sequence.

    Returns:
        tuple: Two aligned sequences with random gaps.
    """
    max_len = max(len(seq1), len(seq2))
    return "".join(random.choice(['-', *seq1]) for _ in range(max_len)), \
           "".join(random.choice(['-', *seq2]) for _ in range(max_len))

# Fitness function: Higher score = better alignment
def fitness(alignment1, alignment2):
    """
    Calculates the fitness score of two aligned sequences based on matches, mismatches, and gaps.

    Args:
        alignment1 (str): The first aligned sequence.
        alignment2 (str): The second aligned sequence.

    Returns:
        int: The fitness score of the alignment.
    """
    score = 0
    for a, b in zip(alignment1, alignment2):
        if a == b:
            score += 1  # Match
        elif a == '-' or b == '-':
            score -= 1  # Gap penalty
        else:
            score -= 2  # Mismatch penalty
    return score

# Crossover function
def crossover(parent1, parent2):
    """
    Performs crossover between two parent sequences to produce two child sequences.

    Args:
        parent1 (str): The first parent sequence.
        parent2 (str): The second parent sequence.

    Returns:
        tuple: Two child sequences resulting from the crossover.
    """
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutation function
def mutate(seq):
    """
    Mutates a sequence by randomly changing its characters with a probability defined by MUTATION_RATE.

    Args:
        seq (str): The sequence to mutate.

    Returns:
        str: The mutated sequence.
    """
    seq = list(seq)
    for i in range(len(seq)):
        if random.random() < MUTATION_RATE:
            seq[i] = random.choice(['-', 'A', 'C', 'G', 'T'])
    return ''.join(seq)

# Genetic Algorithm
def genetic_algorithm():
    """
    Runs the genetic algorithm to find the best alignment for two DNA sequences.
    The algorithm uses selection, crossover, and mutation to evolve the population over generations.

    Displays the best fitness score every 10 generations and the final best alignment.
    """
    # Initial population
    population = [random_alignment(SEQ1, SEQ2) for _ in range(POP_SIZE)]

    for gen in range(GENERATIONS):
        population = sorted(population, key=lambda x: fitness(x[0], x[1]), reverse=True)
        next_population = []

        # Selection and crossover
        for i in range(0, POP_SIZE, 2):
            p1, p2 = population[i][0], population[i + 1][1]
            c1, c2 = crossover(p1, p2)
            
            # Mutation
            next_population.append((mutate(c1), mutate(c2)))

        population = next_population

        # Display best score every 10 generations
        if gen % 10 == 0:
            best = max(population, key=lambda x: fitness(x[0], x[1]))
            print(f"Generation {gen} - Best Score: {fitness(best[0], best[1])}")

    # Best result
    best = max(population, key=lambda x: fitness(x[0], x[1]))
    print("\nBest Alignment:")
    print(best[0])
    print(best[1])
    print(f"Final Fitness Score: {fitness(best[0], best[1])}")

# Run the Genetic Algorithm
genetic_algorithm()
