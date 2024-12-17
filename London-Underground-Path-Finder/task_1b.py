from generate_random_graph import generate_random_graph
from dijkstra import dijkstra
from print_path import print_path
import time
import random

if __name__ == "__main__": 
    # setting the number of vertices = n
    card_V = 400
    
    # generating a random graph of size n
    graph = generate_random_graph(card_V, 0.08, True, False, True, 1, 5)
    
    # selecting random start and end vertices
    s = random.randint(0, card_V - 1)
    t = random.randint(0, card_V - 1)
    # ensure that source and target are different
    while t == s:
        t = random.randint(0, card_V - 1)
    
    # start time measurement
    s1 = time.perf_counter()
    
    # calculating all shortest paths from source to all stations
    d, pi = dijkstra(graph, s)
    
    # path is an array containing all the stations names in the middle from source to target
    path = print_path(pi, s, t, lambda v: v)
    
    # printing the path from source to a specific target
    if path is None:
        print(f"no path found from vertex {s} to vertex {t}")
    else:
        # `map(str, path)` is used to convert each vertex in the path to a string,
        # allowing them to be joined with ' -> ' 
        print(f"shortest path from vertex {s} to vertex {t}: {' -> '.join(map(str, path))}")
        print(f"total distance: {d[t]} minutes")
    
    # end time measurement
    s2 = time.perf_counter()
    # time calculation
    t1 = s2 - s1
    # print the time the algorithm uses
    print(f'time: {t1} s')

