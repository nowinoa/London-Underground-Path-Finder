# London Tube Network

This project contains different files to achieve various tasks related to simulating the London Tube Network:

- **Task 1a**: Generates a network graph with 5 stations and uses Dijkstra’s algorithm to find the shortest path. It then prints the path and the time it takes to travel along this path.

- **Task 1b**: Generates a random graph and measures the time it takes for the algorithm from Task 1a to run on this new graph.

- **Task 2a**: Performs the same task as Task 1a but sets all distances equal to 1, focusing on measuring the number of stops from the source station to the target station.

- **Task 2b**: Performs the same task as Task 1b, but measures the time the algorithm takes to return the number of stops instead of the travel time.

- **Task 3a**: Analyzes the London Underground Network by processing an Excel dataset to extract train lines, stations, and connections with their distances. It normalizes station names, constructs a graph with stations as vertices and connections as weighted edges, and uses Dijkstra’s algorithm to compute shortest paths between all station pairs. The longest journey in terms of travel time is identified, with its duration and path printed. A histogram is generated to visualize the distribution of all valid journey durations, providing insights into the range of travel times across the network.

- **Task 3b**: it is similar to Task 3a but focuses on analyzing the London Underground Network in terms of the number of stops between stations rather than travel time. It processes an Excel dataset to extract station connections and normalizes station names. Connections are treated as unweighted, assigning each a uniform distance of 1 to represent a single stop. Using Dijkstra's algorithm, it calculates the shortest path in terms of stops between all station pairs, identifies the journey with the most stops, and prints its details. A histogram visualizes the distribution of the number of stops for all journeys, offering insights into stop frequency across the network.

- **Task 4**: Calculates the essential connections and potential closures in the London Underground Network by utilizing Kruskal's algorithm to derive a Minimum Spanning Tree (MST). It processes an Excel dataset of stations, connections, and distances to construct a graph and identifies redundant connections that can be closed without losing network connectivity. The remaining essential connections form the MST. Dijkstra's algorithm is then applied to determine the longest journey (in terms of travel time) across the revised network. The results include a list of closed connections, the longest journey details, and a histogram visualizing the distribution of journey times between station pairs.

## Project Structure

```plaintext
.
├── adjacency_list_graph.py
├── adjacency_matrix_graph.py
├── bellman_ford.py
├── bfs.py
├── dag_shortest_paths.py
├── database.xlsx
├── dfs.py
├── difference_constraints.py
├── dijkstra.py
├── disjoint_set_forest.py
├── dll_sentinel.py
├── fifo_queue.py
├── generate_random_graph.py
├── heap_priority_queue.py
├── heap.py
├── heapsort.py
├── max_heap_priority_queue.py
├── max_heap.py
├── merge_sort.py
├── min_heap_priority_queue.py
├── min_heap.py
├── mst.py
├── print_path.py
├── README.md
├── single_source_shortest_paths.py
├── task_1a.py
├── task_1b.py
├── task_2a.py
├── task_2b.py
├── task_3a.py
├── task_3b.py
└── task_4.py
```
## Installation

1. Download the code from GitHub or clone the repo using Git:
    ```bash
         git clone https://github.com/nowinoa/London-Underground-Path-Finder.git
    ```

2. Install all dependencies:

    ``` pip install time random numpy openpyxl re matplotlib ```

3. Make shure all dependencies are included on the repository

## Usage

You can run each code by calling the name of the file, for example: 

``` python task_1a.py ```

- **Task 1a**: Outputs the shortest path and travel time between two stations using Dijkstra’s algorithm.
- **Task 1b**: Outputs the time taken for Dijkstra’s algorithm to run on a random graph.
- **Task 2a**: Outputs the shortest path in terms of the number of stops between two stations.
- **Task 2b**: Outputs the time taken for Dijkstra’s algorithm to calculate the shortest path based on the number of stops.
- **Task 3a**: Outputs the longest journey in terms of time and a histogram of journey durations across the network.
- **Task 3b**: Outputs the longest journey in terms of stops and a histogram of stop frequencies across the network.
- **Task 4**: Outputs the Minimum Spanning Tree (MST), the longest journey in the revised network, and a histogram of journey times after removing redundant connections.


## Credits
This project was created by <a href="https://github.com/nowinoa">Ainhoa Prada</a> under the supervision of the <a href="https://www.gre.ac.uk/">University of Greenwich</a>. 

## License
This project is under MIT license.
        
## Questions
For any questions or issues feel free to contact me at: apt.code14@gmail.com

To explore more about my projects visit my profile :point_right: <a href="https://github.com/nowinoa">:computer:</a>

© 2024 Ainhoa Prada. Confidential and Proprietary. All Rights Reserved.
