import numpy as np

def ox_crossover(p1, p2):
    n = len(p1)
    a, b = sorted(np.random.choice(n, 2, replace=False))

    child = [-1] * n
    child[a:b] = p1[a:b]

    p2_seq = [x for x in p2 if x not in child]

    idx = 0
    for i in range(n):
        if child[i] == -1:
            child[i] = p2_seq[idx]
            idx += 1

    return np.array(child)
