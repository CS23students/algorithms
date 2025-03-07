INF = float('inf')

def floyd_warshall(graph):
    """Finds shortest paths between all pairs using Floyd's algorithm."""
    n = len(graph)
    
    # Applying Floyd's Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

def print_solution(graph):
    """Prints the shortest path matrix."""
    n = len(graph)
    print("\nShortest Distance Matrix:")
    for i in range(n):
        for j in range(n):
            if graph[i][j] == INF:
                print("INF", end=" ")
            else:
                print(graph[i][j], end="  ")
        print()

# Get user input for the graph
n = int(input("Enter the number of vertices: "))
graph = []

print("Enter the adjacency matrix (use INF for no direct edge):")
for i in range(n):
    row = list(map(str, input().split()))
    for j in range(n):
        if row[j].upper() == "INF":  # Convert 'INF' input to float('inf')
            row[j] = INF
        else:
            row[j] = int(row[j])
    graph.append(row)

# Run Floyd Warshall Algorithm
floyd_warshall(graph)

# Print the shortest paths matrix
print_solution(graph)

# OP :
# Enter the number of vertices: 4
# Enter the adjacency matrix (use INF for no direct edge):
# 0 3 INF 7
# 8 0 2 INF
# 5 INF 0 1
# 2 INF INF 0

# Shortest Distance Matrix:
# 0  3  5  6  
# 5  0  2  3  
# 3  6  0  1  
# 2  5  7  0  

