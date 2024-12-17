from adjacency_list_graph import AdjacencyListGraph
from print_path import print_path
from dijkstra import dijkstra

if __name__ == "__main__":

    # Example graph.
    vertices = ['Tottenham', 'Holborn', 'Leicester Square', 'Oxford Circus', 'Green Park', 'Picadilly Circus',
                'Covent Garden']
    edges = [('Tottenham', 'Holborn'), ('Tottenham', 'Leicester Square'), ('Tottenham', 'Oxford Circus'),
             ('Oxford Circus', 'Green Park'), ('Green Park', 'Picadilly Circus'),
             ('Oxford Circus', 'Picadilly Circus'), ('Picadilly Circus', 'Leicester Square'),
             ('Leicester Square', 'Covent Garden'), ('Covent Garden', 'Holborn')]

    # Set each edge weight to 1 to represent a stop.
    graph1 = AdjacencyListGraph(len(vertices), directed=False, weighted=True)
    for edge in edges:
        graph1.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), 1)  # Each stop has a uniform weight of 1

    s = vertices.index('Tottenham')

    # Run Dijkstra's algorithm to find the minimum number of stops
    d, pi = dijkstra(graph1, s)
# identifying closest station from source to all paths
    closest_distance = float('inf')  # Initialize to a very high number
    closest_station = None
    for i in range(len(vertices)):
        # Skip the source station itself
        if i != s and d[i] < closest_distance:
            closest_distance = d[i]
            closest_station = vertices[i]

    cs = vertices.index(closest_station)
    
    # printing path for the closest station
    # predecesors, source and the closest station
    path = print_path(pi, s, cs, lambda v: vertices[v])
    print(f"Shortest path from {vertices[s]}: {' -> '.join(path)}")
    print(f"Total distance: {closest_distance} stops")