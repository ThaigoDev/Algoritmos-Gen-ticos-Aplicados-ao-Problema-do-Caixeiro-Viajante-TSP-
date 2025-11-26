import numpy as np
from math import sqrt

def read_tsp(file_path):
    coords = []
    edge_type = None

    with open(file_path, "r") as f:
        start = False
        for line in f:
            line = line.strip()

            if line.startswith("EDGE_WEIGHT_TYPE"):
                edge_type = line.split(":")[1].strip()

            if "NODE_COORD_SECTION" in line:
                start = True
                continue

            if "EOF" in line or line == "":
                break

            if start:
                parts = line.split()
                if len(parts) >= 3:
                    _, x, y = parts
                    coords.append((float(x), float(y)))

    coords = np.array(coords)
    n = len(coords)
    dist = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            xd = coords[i][0] - coords[j][0]
            yd = coords[i][1] - coords[j][1]

            if edge_type == "EUC_2D":
                dij = int(sqrt(xd*xd + yd*yd) + 0.5)  # nint()

            elif edge_type == "ATT":
                rij = sqrt((xd*xd + yd*yd) / 10.0)
                tij = int(rij + 0.5)  # nint
                dij = tij + 1 if tij < rij else tij

            else:
                raise ValueError(f"EDGE_WEIGHT_TYPE desconhecido: {edge_type}")

            dist[i][j] = dij

    return coords, dist
