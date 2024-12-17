from generate_random_graph import generate_random_graph
import time
import numpy as np
from dijkstra import dijkstra
from print_path import print_path
import random

if __name__ == "__main__":
    # generate a random graph of size n
    card_V = 100
    # Each edge weight is set to 1 since the measure is the number of stops.
    graph = generate_random_graph(card_V, 0.08, True, False , True, 1, 1)
    vertices = [f"V{i}" for i in range(card_V)]

    # selecting random start and end vertices
    s = random.randint(0, card_V - 1)
    t = random.randint(0, card_V - 1)
    # ensure that source and target are different
    while t == s:
        t = random.randint(0, card_V - 1)
    
    # algorithm time measurement
    s1 = time.perf_counter()
    # calculating all shortest path from source
    d, pi = dijkstra(graph, s)
    
    path = print_path(pi, s, t, lambda v: vertices[v])
    
    if path is None:
        print(f"No path found from {vertices[s]} to {vertices[t]}")
    else:
        print(f"Shortest path from {vertices[s]} to {vertices[t]}: {' -> '.join(path)}")
        print(f'Total stops: {d[t]} stops')
    s2 = time.perf_counter()

    t1 = s2 - s1

    print(t1)
    
