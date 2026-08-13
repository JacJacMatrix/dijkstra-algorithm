import random
import time
import heapq
import matplotlib.pyplot as plt
import networkx as nx

def generate_random_graph(n, m, min_weight=1, max_weight=10):
    graph = {i: {} for i in range(n)}
    edges = set()
    while len(edges) < m:
        i, j = random.sample(range(n), 2)
        if (i, j) not in edges and (j, i) not in edges:
            weight = random.randint(min_weight, max_weight)
            graph[i][j] = weight
            graph[j][i] = weight  # Undirected graph
            edges.add((i, j))
    return graph

def generate_complete_graph(n, min_weight=1, max_weight=10):
    graph = {i: {} for i in range(n)}
    for i in range(n):
        for j in range(n):
            if i != j:
                weight = random.randint(min_weight, max_weight)
                graph[i][j] = weight
                graph[j][i] = weight
    return graph

def generate_directed_graph(n, m, min_weight=1, max_weight=10):
    """Generate random directed graph with n vertices and m edges."""
    max_edges = n * (n - 1)
    if m > max_edges:
        m = max_edges
    graph = {i: {} for i in range(n)}
    edges = set()
    while len(edges) < m:
        i, j = random.sample(range(n), 2)
        if (i, j) not in edges:
            weight = random.randint(min_weight, max_weight)
            graph[i][j] = weight
            edges.add((i, j))
    return graph

def generate_tree(n, min_weight=1, max_weight=10):
    """Generate random tree (undirected, connected, acyclic graph with n-1 edges)."""
    graph = {i: {} for i in range(n)}
    nodes = list(range(n))
    random.shuffle(nodes)
    for i in range(1, n):
        a = nodes[i]
        b = nodes[random.randint(0, i-1)]
        weight = random.randint(min_weight, max_weight)
        graph[a][b] = weight
        graph[b][a] = weight
    return graph

def draw_graph(graph):
    # Automatic graph type detection (directed/undirected)
    is_directed = any(i not in graph[j] for j in graph for i in graph[j])
    G = nx.DiGraph() if is_directed else nx.Graph()
    for u in graph:
        for v, w in graph[u].items():
            G.add_edge(u, v, weight=w)
    pos = nx.spring_layout(G, seed=42)  # Fixed layout for reproducibility
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # Drawing parameters
    arrow_style = '-|>'  # classic arrow style
    arrow_size = 20      # arrow size
    width = 2            # edge thickness

    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=800)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    if is_directed:
        nx.draw_networkx_edges(
            G, pos,
            arrowstyle=arrow_style,
            arrowsize=arrow_size,
            width=width,
            connectionstyle='arc3,rad=0.1'  # slightly curved edges for better visibility
        )
    else:
        nx.draw_networkx_edges(G, pos, width=width)

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    plt.title('Graph visualization')
    plt.axis('off')
    plt.show()

def dijkstra(graph, src, dest):
    distances = {v: float('inf') for v in graph}
    distances[src] = 0
    predecessors = {}
    heap = [(0, src)]
    while heap:
        curr_dist, u = heapq.heappop(heap)
        if u == dest:
            break
        for v in graph[u]:
            alt = curr_dist + graph[u][v]
            if alt < distances[v]:
                distances[v] = alt
                predecessors[v] = u
                heapq.heappush(heap, (alt, v))
    if distances[dest] == float('inf'):
        print("No path between given vertices.")
        return
    path = []
    curr = dest
    while curr != src:
        path.append(curr)
        curr = predecessors.get(curr)
        if curr is None:
            print("No path between given vertices.")
            return
    path.append(src)
    print('Shortest path: ' + str(path[::-1]) + " cost=" + str(distances[dest]))

def dijkstra_all_pairs(graph):
    n = len(graph)
    for src in range(n):
        print(f"\nShortest paths from vertex {src}:")
        for dest in range(n):
            if src == dest:
                continue
            print(f"{src} -> {dest}: ", end="")
            try:
                dijkstra(graph, src, dest)
            except Exception as e:
                print(f"Error: {e}")

def main():
    print("Choose graph type:")
    print("1 - random")
    print("2 - complete")
    print("3 - directed")
    print("4 - tree")
    typ = input("Your choice: ")

    n = int(input("Enter number of vertices: "))
    graph = None

    if typ == '1':
        max_edges = n*(n-1)//2
        m = int(input(f"Enter number of edges (max {max_edges}): "))
        if m > max_edges:
            print("Too many edges! Setting to maximum value.")
            m = max_edges
        graph = generate_random_graph(n, m)
    elif typ == '2':
        graph = generate_complete_graph(n)
    elif typ == '3':
        max_edges = n*(n-1)
        m = int(input(f"Enter number of edges (max {max_edges}): "))
        if m > max_edges:
            print("Too many edges! Setting to maximum value.")
            m = max_edges
        graph = generate_directed_graph(n, m)
    elif typ == '4':
        if n < 2:
            print("Tree requires at least 2 vertices.")
            return
        graph = generate_tree(n)
    else:
        print("Unknown graph type.")
        return

    print("Generated graph:")
    for v, edges in graph.items():
        print(f"{v}: {edges}")

    draw_graph(graph)

    print("\nWhat would you like to do?")
    print("1 - Shortest path between two vertices")
    print("2 - Shortest paths for all pairs (all-to-all)")
    wybor = input("Your choice: ")

    if wybor == '1':
        src = int(input(f"Enter start vertex (0-{n-1}): "))
        dest = int(input(f"Enter end vertex (0-{n-1}): "))
        print("Dijkstra algorithm result:")
        start_time = time.time()
        dijkstra(graph, src, dest)
        end_time = time.time()
        print(f"Algorithm execution time: {end_time - start_time:.6f} seconds")
    elif wybor == '2':
        print("Results for all pairs:")
        start_time = time.time()
        dijkstra_all_pairs(graph)
        end_time = time.time()
        print(f"\nAlgorithm execution time for all pairs: {end_time - start_time:.6f} seconds")
    else:
        print("Unknown choice.")

if __name__ == "__main__":
    main()
