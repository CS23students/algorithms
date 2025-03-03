from collections import deque

def bfs(graph, start):
    """Performs Breadth-First Search on a graph starting from the given node."""
    visited = set()  # To track visited nodes
    queue = deque([start])  # Initialize queue with the start node

    while queue:
        node = queue.popleft()  # Dequeue front node
        if node not in visited:
            print(node, end=" ")  # Print node
            visited.add(node)  # Mark as visited
            queue.extend(graph[node] - visited)  # Add unvisited neighbors to queue

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

start_node = input("Enter the start node for BFS: ")

print("\nBFS Traversal:")
bfs(graph, start_node)



# OP :
# Enter number of nodes: 5
# Enter number of edges: 4
# Enter edges:
# A B
# A C
# B D
# C E
# Enter the start node for BFS: A
# BFS Traversal:
# A B C D E
