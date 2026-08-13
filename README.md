# Dijkstra's Shortest Path Algorithm

An efficient Python implementation of Dijkstra's algorithm for finding shortest paths in graphs with non-negative edge weights. This project uses a priority queue (heap) for optimal performance and includes comprehensive graph generation and visualization tools.

## Why Dijkstra?

Dijkstra's algorithm is the go-to solution for shortest path problems in networks with non-negative weights. It's the backbone of GPS navigation systems, network routing protocols, and countless optimization problems. When you need efficiency and guaranteed optimal paths, Dijkstra delivers.

## How it works

The algorithm maintains a priority queue of vertices to explore, always selecting the vertex with the smallest known distance. It uses a greedy approach - once a vertex is extracted from the queue with its minimum distance, that distance is final. This implementation uses Python's `heapq` module for efficient priority queue operations.

## Performance

- **Time Complexity:** O((V + E) log V) with binary heap
- **Space Complexity:** O(V)

The logarithmic factor comes from heap operations, making this significantly faster than Bellman-Ford for graphs without negative weights.

## Getting Started

### Installation

```bash
pip install -r requirements.txt
```

### Running the implementation

```bash
python dijkstra.py
```

### What's included

The program supports various graph structures for testing:

- **Random undirected graphs** - standard test cases
- **Complete graphs** - maximum connectivity
- **Random directed graphs** - asymmetric edge relationships
- **Trees** - minimal connected graphs

After graph creation, you can:
- Find the optimal path between two specific vertices
- Compute shortest paths from every vertex to all others
- Visualize the graph structure with edge weights

## Example Usage

### Interactive Mode

```bash
python dijkstra.py
```

```
Choose graph type:
1 - random
2 - complete
3 - directed
4 - tree
Your choice: 1

Enter number of vertices: 5
Enter number of edges (max 10): 7

Generated graph:
0: {4: 5, 1: 2, 7: 8, 5: 5, 8: 6, 2: 8}
1: {7: 4, 0: 2, 8: 3, 6: 9, 4: 8, 3: 2}
2: {7: 5, 5: 5, 8: 5, 4: 4, 0: 8}
3: {5: 6, 7: 1, 4: 3, 8: 9, 6: 1, 1: 2}
4: {0: 5, 6: 3, 1: 8, 5: 6, 3: 3, 2: 4, 7: 6, 8: 3}
5: {6: 3, 0: 5, 3: 6, 2: 5, 7: 5, 4: 6, 8: 3}
6: {5: 3, 7: 9, 8: 6, 1: 9, 4: 3, 3: 1}
7: {8: 2, 1: 4, 2: 5, 0: 8, 6: 9, 5: 5, 3: 1, 4: 6}
8: {7: 2, 0: 6, 1: 3, 6: 6, 5: 3, 2: 5, 3: 9, 4: 3}

What would you like to do?
1 - Shortest path between two vertices
2 - Shortest paths for all pairs (all-to-all)
Your choice: 1

Enter start vertex (0-4): 0
Enter end vertex (0-4): 4
Dijkstra algorithm result:
Shortest path: [0, 4] cost=5
Algorithm execution time: 0.000234 seconds
```

### Programmatic Usage

```python
from dijkstra import dijkstra, dijkstra_all_pairs, generate_random_graph

# Generate a random graph
graph = generate_random_graph(n=5, m=7)

# Find shortest path between two vertices
dijkstra(graph, src=0, dest=4)

# Compute all-pairs shortest paths
dijkstra_all_pairs(graph)
```

### Using with Custom Graphs

```python
# Define your own graph structure
custom_graph = {
    0: {1: 4, 2: 2},
    1: {2: 1, 3: 5},
    2: {1: 1, 3: 8, 4: 10},
    3: {4: 2},
    4: {}
}

# Find shortest path
dijkstra(custom_graph, src=0, dest=4)
# Output: Shortest path: [0, 2, 1, 3, 4] cost=8
```

### Different Graph Types

**Random Undirected Graph:**
```bash
Your choice: 1
Enter number of vertices: 8
Enter number of edges (max 28): 15
```

**Complete Graph:**
```bash
Your choice: 2
Enter number of vertices: 4
# All possible edges between all vertices
```

**Tree Structure:**
```bash
Your choice: 4
Enter number of vertices: 6
# Generates a tree with exactly 5 edges
```

**Directed Graph:**
```bash
Your choice: 3
Enter number of vertices: 7
Enter number of edges (max 42): 20
# Asymmetric edge relationships
```

## Key Components

- `dijkstra()` - core algorithm using heapq for efficiency
- `dijkstra_all_pairs()` - computes paths from every source vertex
- Graph generators: `generate_random_graph()`, `generate_complete_graph()`, `generate_directed_graph()`, `generate_tree()`
- `draw_graph()` - networkx/matplotlib visualization

## License

MIT License - see LICENSE file for details