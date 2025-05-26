import time

def dfs(graph, node, visited):
    """Performs Depth-First Search on a graph starting from the given node."""
    if node not in visited:
        print(node, end=" ")  # Print node
        visited.add(node)  # Mark as visited
        for neighbor in graph[node]:  # Visit all neighbors
            dfs(graph, neighbor, visited)

# Get user input for the graph
graph = {}
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

print("Enter edges (node1 node2):")
for _ in range(e):
    u, v = input().split()
    if u not in graph:
        graph[u] = set()
    if v not in graph:
        graph[v] = set()
    graph[u].add(v)
    graph[v].add(u)  # Since it's an undirected graph

start_node = input("Enter the start node for DFS: ")

print("\nDFS Traversal:")

# Measure time taken
start_time = time.perf_counter()
dfs(graph, start_node, set())
end_time = time.perf_counter()

# Display timing and complexity
print(f"\nTime taken for DFS traversal: {end_time - start_time:.6f} seconds")
print("Time Complexity of DFS: O(V + E)")




# Enter number of nodes: 5
# Enter number of edges: 4
# Enter edges (node1 node2):
# A B
# A C
# B D
# C E
# Enter the start node for DFS: A

# DFS Traversal:
# A B D C E
# Time taken for DFS traversal: 0.000031 seconds
# Time Complexity of DFS: O(V + E)

