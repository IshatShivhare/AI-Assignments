import random

def generate_random_alignment(seq1, seq2, length):
    """Generates a random alignment by introducing gaps randomly."""
    aligned1 = list(seq1.ljust(length, '-'))
    aligned2 = list(seq2.ljust(length, '-'))
    random.shuffle(aligned1)
    random.shuffle(aligned2)
    return ''.join(aligned1), ''.join(aligned2)

def fitness(alignment1, alignment2):
    """Calculates fitness based on match/mismatch/gap scoring."""
    score = 0
    for a, b in zip(alignment1, alignment2):
        if a == b:
            score += 1
        elif a == '-' or b == '-':
            score -= 2
        else:
            score -= 1
    return score

def crossover(parent1, parent2):
    """Performs crossover by swapping a random part of two alignments."""
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(alignment):
    """Randomly introduces a mutation by changing a character."""
    alignment = list(alignment)
    index = random.randint(0, len(alignment) - 1)
    if alignment[index] != '-':
        alignment[index] = random.choice('ACGT-')
    return ''.join(alignment)

def genetic_algorithm(seq1, seq2, population_size=10, generations=100):
    """Runs the Genetic Algorithm to find the best alignment."""
    length = max(len(seq1), len(seq2)) + 5
    population = [generate_random_alignment(seq1, seq2, length) for _ in range(population_size)]
    
    for _ in range(generations):
        population = sorted(population, key=lambda x: fitness(x[0], x[1]), reverse=True)
        new_population = population[:2]
        
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population[:5], 2)
            child1, child2 = crossover(parent1[0], parent2[0]), crossover(parent1[1], parent2[1])
            new_population.extend([(mutate(child1[0]), mutate(child2[1]))])
        
        population = new_population
    
    best_alignment = max(population, key=lambda x: fitness(x[0], x[1]))
    return best_alignment

seq1 = "ACGTGCA"
seq2 = "AGTACG"

best_alignment = genetic_algorithm(seq1, seq2)
print("Best Alignment:")
print(best_alignment[0])
print(best_alignment[1])