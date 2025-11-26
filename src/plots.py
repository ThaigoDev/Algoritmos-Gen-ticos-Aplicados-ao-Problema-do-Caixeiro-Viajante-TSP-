import matplotlib.pyplot as plt

def plot_boxplot(df):
    df.boxplot(column="custo", by="valor", figsize=(9, 5))
    plt.title("Boxplot dos custos")
    plt.suptitle("")
    plt.xlabel("Valor do parâmetro")
    plt.ylabel("Custo")
    plt.show()

def plot_evolution(df):
    for v in df["valor"].unique():
        subset = df[df["valor"] == v]

        best = subset.loc[subset["custo"].idxmin()]
        worst = subset.loc[subset["custo"].idxmax()]

        plt.figure(figsize=(10, 5))
        plt.plot(best["hist"], label="Melhor")
        plt.plot(worst["hist"], label="Pior")
        plt.title(f"Evolução (valor={v})")
        plt.xlabel("Geração")
        plt.ylabel("Custo")
        plt.legend()
        plt.show()

def plot_best_path(coords, path):
    xs = coords[path][:, 0]
    ys = coords[path][:, 1]

    plt.figure(figsize=(8, 8))
    plt.scatter(xs, ys)

    for i in range(len(path)):
        x1, y1 = coords[path[i]]
        x2, y2 = coords[path[(i+1) % len(path)]]
        plt.plot([x1, x2], [y1, y2])

    plt.title("Melhor caminho encontrado")
    plt.show()
