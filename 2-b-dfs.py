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
dfs(graph, start_node, set())



#  OP
# Enter number of nodes: 5
# Enter number of edges: 4
# Enter edges:
# A B
# A C
# B D
# C E
# Enter the start node for DFS: A
# DFS Traversal:
# A B D C E
