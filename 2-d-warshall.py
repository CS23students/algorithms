def warshall_algorithm(graph):
    """Compute transitive closure using Warshall's Algorithm."""
    n = len(graph)

    # Applying Warshall's Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])

def print_solution(graph):
    """Prints the transitive closure matrix."""
    print("\nTransitive Closure of the given graph:")
    for row in graph:
        print(' '.join(str(val) for val in row))

# Get user input for the graph
n = int(input("Enter the number of vertices: "))
graph = []

print("Enter the adjacency matrix (0 for no edge, 1 for edge):")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# Run Warshall's Algorithm
warshall_algorithm(graph)

# Print the transitive closure
print_solution(graph)


# OP :
# Enter the number of vertices: 4
# Enter the adjacency matrix (0 for no edge, 1 for edge):
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1
# 1 0 0 0

# Transitive Closure of the given graph:
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
