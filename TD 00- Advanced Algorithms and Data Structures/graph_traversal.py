import networkx as nx
import matplotlib.pyplot as plt



def bfs(graph, start):
    """
    Perform Breadth-First Search (BFS) on the graph starting from the given node.

    Parameters:
        graph (dict): A dictionary representing an undirected graph where keys are nodes and values are lists of neighbors.
        start (str): The starting node for BFS.

    Returns:
        list: A list of nodes in the order they were visited.
    """
    visited = set()
    queue = [start]  # Using a list as a queue
    result = []

    while queue:
        node = queue.pop(0)  # Dequeue operation
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return result

def dfs_recursive(graph, start, visited=None):
    """
    Perform Depth-First Search (DFS) recursively on the graph starting from the given node.

    Parameters:
        graph (dict): A dictionary representing an undirected graph where keys are nodes and values are lists of neighbors.
        start (str): The starting node for DFS.
        visited (set): A set of visited nodes to track recursion (default is None).

    Returns:
        list: A list of nodes in the order they were visited.
    """
    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result

def dfs_iterative(graph, start):
    """
    Perform Depth-First Search (DFS) iteratively on the graph starting from the given node.

    Parameters:
        graph (dict): A dictionary representing an undirected graph where keys are nodes and values are lists of neighbors.
        start (str): The starting node for DFS.

    Returns:
        list: A list of nodes in the order they were visited.
    """
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()  # Pop from stack
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(neighbor for neighbor in reversed(graph[node]) if neighbor not in visited)

    return result

def is_connected_bfs(graph, start, target):
    """
    Check if two nodes are connected using BFS and find the shortest path.

    Parameters:
        graph (dict): A dictionary representing an undirected graph where keys are nodes and values are lists of neighbors.
        start (str): The starting node.
        target (str): The target node.

    Returns:
        tuple: (bool, list) where bool indicates if the nodes are connected, and list is the shortest path.
    """
    visited = set()
    queue = [(start, [start])]  # Using a list as a queue with path tracking

    while queue:
        node, path = queue.pop(0)  # Dequeue operation
        if node == target:
            return True, path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return False, []


def build_Show_graph (graph):
    """
    Visualize a graph structure using NetworkX and Matplotlib.
        Output:
        A visual representation of the input graph.
    """
    
    G = nx.Graph()
    
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Draw graph
    plt.figure(figsize=(4, 6))  
    pos = nx.spring_layout(G)  # Node position
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=15, font_weight='bold', edge_color='gray')
    plt.title("Graph Visualization", fontsize=20)
    plt.show()

if __name__ == "__main__":
    city_map = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
        'G': ['H'],
        'H': ['G', 'I']
    }
    
    print("Show the graph:")
    build_Show_graph(city_map)
    
    print("BFS Traversal:", bfs(city_map, 'A'))
    print("DFS Recursive Traversal:", dfs_recursive(city_map, 'A'))
    print("DFS Iterative Traversal:", dfs_iterative(city_map, 'A'))

    connected, path = is_connected_bfs(city_map, 'A', 'F')
    print(f"Are 'A' and 'F' connected? {connected}, Path: {path}")

    connected, path = is_connected_bfs(city_map, 'A', 'G')
    print(f"Are 'A' and 'G' connected? {connected}, Path: {path}")


