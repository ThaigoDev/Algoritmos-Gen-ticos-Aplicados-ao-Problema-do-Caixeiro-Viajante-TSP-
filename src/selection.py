import numpy as np
import random

def tournament_selection(pop, fitnesses, k=3):
    ids = np.random.choice(len(pop), k, replace=False)
    best = ids[np.argmin(fitnesses[ids])]
    return pop[best]

def roulette_selection(pop, fitnesses):
    inv = 1 / (fitnesses + 1e-9)
    prob = inv / inv.sum()
    index = np.random.choice(len(pop), p=prob)
    return pop[index]

def elitism(pop, fitnesses, pct):
    qtd = int(len(pop) * pct)
    idx = np.argsort(fitnesses)
    return pop[idx[:qtd]]
