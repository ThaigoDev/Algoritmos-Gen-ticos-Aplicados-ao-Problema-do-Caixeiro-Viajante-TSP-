def fitness(individual, dist):
    total = 0
    for i in range(len(individual)-1):
        total += dist[individual[i]][individual[i+1]]
    total += dist[individual[-1]][individual[0]]
    return total
