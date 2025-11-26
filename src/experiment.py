import pandas as pd
from src.ga import genetic_algorithm

def run_experiments(
        tsp_file,
        param_name="mutation_rate",
        values=[0.0, 0.1, 0.2, 0.3],
        M=4, N=5):

    results = []

    for value in values:
        for exec_id in range(N):

            best, cost, hist, coords = genetic_algorithm(
                tsp_file, mutation_rate=value
            )

            results.append({
                "parametro": param_name,
                "valor": value,
                "execucao": exec_id,
                "custo": cost,
                "hist": hist,
                "caminho": best
            })

    df = pd.DataFrame(results)
    df.to_csv("results/dataframe.csv", index=False)

    return df
