import heapq

def prims_algorithm(graph, start):
    """Finds the Minimum Cost Spanning Tree (MST) using Prim's algorithm."""
    min_heap = [(0, start)]  # Priority queue: (weight, node)
    visited = set()  # Track visited nodes
    mst = []  # Store the MST edges
    total_cost = 0  # Total cost of MST

    while min_heap:
        weight, node = heapq.heappop(min_heap)  # Get the edge with the smallest weight
        if node in visited:
            continue  # Skip already visited nodes

        visited.add(node)  # Mark node as visited
        total_cost += weight  # Add weight to MST cost

        # Add neighbors to heap if not visited
        for neighbor, edge_weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor))
                mst.append((node, neighbor, edge_weight))  # Store MST edges

    return mst, total_cost  # Return MST and total cost

# Get user input for the graph
graph = {}
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

print("Enter edges with weights (node1 node2 weight):")
for _ in range(e):
    u, v, w = input().split()
    w = int(w)
    if u not in graph:
        graph[u] = {}
    if v not in graph:
        graph[v] = {}
    graph[u][v] = w
    graph[v][u] = w  # Since it's an undirected graph

start_node = input("Enter the start node: ")

# Run Prim's algorithm
mst, cost = prims_algorithm(graph, start_node)

# Print the Minimum Spanning Tree (MST)
print("\nMinimum Cost Spanning Tree:")
for u, v, w in mst:
    print(f"{u} -- {v}  ({w})")

print("\nTotal Cost of MST:", cost)


#  OP:
# Enter number of nodes: 5
# Enter number of edges: 7
# Enter edges with weights:
# A B 2
# A C 3
# B C 1
# B D 5
# C D 4
# C E 6
# D E 7
# Enter the start node: A
# Minimum Cost Spanning Tree:
# A -- B  (2)
# B -- C  (1)
# A -- C  (3)
# C -- D  (4)

# Total Cost of MST: 10
