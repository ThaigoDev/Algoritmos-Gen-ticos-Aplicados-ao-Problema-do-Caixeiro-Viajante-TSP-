import numpy as np
from src.reader import read_tsp
from src.fitness import fitness
from src.selection import *
from src.crossover import ox_crossover
from src.mutation import swap_mutation

def create_individual(n):
    return np.random.permutation(n)

def genetic_algorithm(
    tsp_file,
    pop_size=100,
    generations=200,
    selection_method="tournament",
    crossover_rate=0.8,
    mutation_rate=0.1,
    elitism_pct=0.1,
    k=3):

    coords, dist_matrix = read_tsp(tsp_file)
    n = len(coords)

    pop = np.array([create_individual(n) for _ in range(pop_size)])

    history_best = []

    for gen in range(generations):
        fitnesses = np.array([fitness(ind, dist_matrix) for ind in pop])
        history_best.append(fitnesses.min())

        new_pop = []

        if selection_method == "elitism":
            elite = elitism(pop, fitnesses, elitism_pct)
            new_pop.extend(elite)

        while len(new_pop) < pop_size:

            if selection_method == "tournament":
                p1 = tournament_selection(pop, fitnesses, k)
                p2 = tournament_selection(pop, fitnesses, k)
            elif selection_method == "roulette":
                p1 = roulette_selection(pop, fitnesses)
                p2 = roulette_selection(pop, fitnesses)
            else:
                p1 = tournament_selection(pop, fitnesses, k)
                p2 = tournament_selection(pop, fitnesses, k)

            if np.random.rand() < crossover_rate:
                child = ox_crossover(p1, p2)
            else:
                child = p1.copy()

            child = swap_mutation(child, mutation_rate)
            new_pop.append(child)

        pop = np.array(new_pop)

    final_fit = np.array([fitness(ind, dist_matrix) for ind in pop])
    best = pop[np.argmin(final_fit)]

    return best, min(final_fit), history_best, coords
