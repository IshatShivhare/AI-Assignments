import random

# Parameters
MATCH_SCORE = 2
MISMATCH_PENALTY = -2
GAP_PENALTY = -1 
POPULATION_SIZE = 100
GENERATIONS = 200
MUTATION_RATE = 0.2

seq1 = "AGTACGCA"
seq2 = "ACTGC"

# Insert gaps into a sequence
def align_sequences(seq1, seq2, gaps1, gaps2):
    s1 = list(seq1)
    s2 = list(seq2)
    for i in sorted(gaps1):
        s1.insert(i, '-')
    for i in sorted(gaps2):
        s2.insert(i, '-')
    while len(s1) < len(s2):
        s1.append('-')
    while len(s2) < len(s1):
        s2.append('-')
    return ''.join(s1), ''.join(s2)

# Fitness function: higher score = better
def fitness(alignment):
    s1, s2 = alignment
    score = 0
    for a, b in zip(s1, s2):
        if a == b and a != '-':
            score += MATCH_SCORE
        elif a == '-' or b == '-':
            score += GAP_PENALTY
        else:
            score += MISMATCH_PENALTY
    return score

# Random gap generator
def random_gaps(seq, min_gaps=1, max_gaps=5):
    return sorted(random.sample(range(len(seq) + max_gaps), random.randint(min_gaps, max_gaps)))

# Mutate gap positions
def mutate(gaps, seq_len, times=2):
    new_gaps = gaps[:]
    for _ in range(times):
        if random.random() < 0.5 and new_gaps:
            new_gaps.pop(random.randint(0, len(new_gaps) - 1))  # remove gap
        else:
            if len(new_gaps) < 6:
                new_gaps.append(random.randint(0, seq_len + len(new_gaps)))  # add gap
    return sorted(new_gaps)

# Crossover gaps
def crossover(g1, g2):
    cut = random.randint(0, len(g1))
    return sorted(g1[:cut] + g2[cut:])

# Genetic Algorithm
def genetic_algorithm():
    population = [(random_gaps(seq1), random_gaps(seq2)) for _ in range(POPULATION_SIZE)]

    for generation in range(GENERATIONS):
        scored_population = []
        for g1, g2 in population:
            alignment = align_sequences(seq1, seq2, g1, g2)
            score = fitness(alignment)
            scored_population.append(((g1, g2), score))

        scored_population.sort(key=lambda x: x[1], reverse=True)
        best_score = scored_population[0][1]
        best_individual = scored_population[0][0]

        if generation % 10 == 0:
            print(f"Generation {generation}, Best Score: {best_score}")

        selected = [x[0] for x in scored_population[:POPULATION_SIZE // 5]]

        new_population = selected[:]
        while len(new_population) < POPULATION_SIZE:
            p1, p2 = random.sample(selected, 2)
            child_g1 = crossover(p1[0], p2[0])
            child_g2 = crossover(p1[1], p2[1])

            if random.random() < MUTATION_RATE:
                child_g1 = mutate(child_g1, len(seq1), times=2)
            if random.random() < MUTATION_RATE:
                child_g2 = mutate(child_g2, len(seq2), times=2)

            new_population.append((child_g1, child_g2))

        population = new_population

    # Final result
    best_alignment = align_sequences(seq1, seq2, *best_individual)
    print("\nBest Alignment:")
    print(best_alignment[0])
    print(best_alignment[1])
    print(f"Final Fitness Score: {fitness(best_alignment)}")

# Run the algorithm
genetic_algorithm()
