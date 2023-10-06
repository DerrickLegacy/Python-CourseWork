# Graph representation - using lists (sets and dictionaries)
graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'S': 3, 'B': 2, 'C': 2},
    'B': {'S': 1, 'A': 2, 'C': 3},
    'C': {'A': 2, 'B': 3, 'D': 3, 'G': 4},
    'D': {'C': 4, 'G': 1},
    'G': {'C': 4, 'D': 1}
}

heuristic_costs = {
    'S': 7,
    'A': 5,
    'B': 7,
    'C': 4,
    'D': 1,
    'G': 0
}

def bfs_graph_search(graph, start):
    queue = [(start, [start])]
    visited = set()  # Initialize an empty set to keep track of visited nodes

    while queue:
        if not queue:
            print("No solution")
        else:
            (node, path) = queue.pop(0)

            if node == 'G':
                return path

            if node not in visited:
                visited.add(node)

                neighbors = graph[node]

                for neighbor, cost in neighbors.items():
                    if neighbor not in path:
                        queue.append((neighbor, path + [neighbor]))
        
    print("No solution found.")

# Calling the BFS function with 'S' as the starting node
result = bfs_graph_search(graph, 'S')

# Print the final path
if result is not None:
    print("Breadth first Graph Search Path found:", result)  
else:
    print("No solution found.")