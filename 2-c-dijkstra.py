import heapq

def dijkstra(graph, start):
    """Finds shortest paths from the start node to all other nodes using Dijkstra's algorithm."""
    shortest_distances = {node: float('inf') for node in graph}  # Initialize distances to infinity
    shortest_distances[start] = 0  # Distance to start node is 0
    pq = [(0, start)]  # Priority queue: (distance, node)
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)  # Get the node with the smallest distance
        
        if current_distance > shortest_distances[current_node]:
            continue  # Ignore outdated entries

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight  # Calculate new distance
            if distance < shortest_distances[neighbor]:  # Update if shorter path found
                shortest_distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))  # Push updated distance into queue
    
    return shortest_distances  # Return the shortest distances

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

# Run Dijkstra's algorithm
shortest_paths = dijkstra(graph, start_node)

# Print the shortest path to all nodes
print("\nShortest paths from node", start_node)
for node, distance in shortest_paths.items():
    print(f"To {node}: {distance}")



# OP :
# Enter number of nodes: 5
# Enter number of edges: 6
# Enter edges with weights:
# A B 2
# A C 4
# B C 1
# B D 7
# C E 3
# D E 2
# Enter the start node: A
# Shortest paths from node A:
# To A: 0
# To B: 2
# To C: 3
# To D: 9
# To E: 6

