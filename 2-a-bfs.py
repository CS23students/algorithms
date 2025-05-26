from collections import deque
import time

def bfs(graph, start):
    """Performs Breadth-First Search on a graph starting from the given node."""
    visited = set()
    queue = deque([start])

    start_time = time.perf_counter()  # Start timing

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node] - visited)

    end_time = time.perf_counter()  # End timing
    time_taken = end_time - start_time
    print(f"\nTime taken for BFS traversal: {time_taken:.6f} seconds")
    print("Time Complexity of BFS: O(V + E)")

# Input
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
    graph[v].add(u)

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
# Time taken for BFS traversal: 0.000045 seconds
# Time Complexity of BFS: O(V + E)
