from adjacency_list_graph import AdjacencyListGraph
from print_path import print_path
from dijkstra import dijkstra
    

if __name__ == "__main__":

    # Database: 
    # vertex = stations 
    vertices = ['Tottenham', 'Holborn', 'Leicester Square', 'Oxford Circus', 'Green Park', 'Picadilly Circus', 'Covent Garden']
    # edges = tuples with the connected stations and their distance (station1, station2, distance)
    edges = [('Tottenham', 'Holborn', 2), ('Tottenham', 'Leicester Square', 2), ('Tottenham', 'Oxford Circus', 1), ('Oxford Circus', 'Green Park', 2),
             ('Green Park', 'Picadilly Circus', 2), ('Oxford Circus', 'Picadilly Circus', 2), ('Picadilly Circus', 'Leicester Square', 1),
             ('Leicester Square', 'Covent Garden', 1), ('Covent Garden', 'Holborn', 2)]
    
    # creating a undirected and weighted graph with the stations
    graph1 = AdjacencyListGraph(len(vertices), directed=False, weighted=True)
    # inserting every edge in edges into the graph
    for edge in edges:
        graph1.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), edge[2])

    # selecting source station by its index position
    s = vertices.index('Tottenham')
    # calculating all shotest paths from source to all stations
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
    print(f"Total distance: {closest_distance} minutes")
    

    # # selecting target station by its index position
    # t = vertices.index('Green Park')
    # path2 = print_path(pi, s, t, lambda v: vertices[v])
    # # printing the path from source to a specific target
    # if path2 is None:
    #     print(f"No path found from {vertices[s]} to {vertices[t]}")
    # else:
    #     print(f"Shortest path from {vertices[s]} to {vertices[t]}: {' -> '.join(path2)}")
    #     print(f"Total distance: {d[t]} minutes")
