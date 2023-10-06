# Define the graph and heuristic_costs
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


def greedy_graph_search(graph, heuristic_costs, start):
    path = []
    total_cost = 0
    visited = set()  # Initialize an empty set to keep track of visited nodes

    current_node = start
    while True:
        path.append(current_node)

        if current_node == 'G':
            break

        neighbors = graph[current_node]
        next_node = None
        min_cost = float('inf')

        for neighbor, cost in neighbors.items():
            if heuristic_costs[neighbor] < min_cost and neighbor not in visited:
                min_cost = heuristic_costs[neighbor]
                next_node = neighbor

        if next_node is None:
            break

        total_cost += graph[current_node][next_node]
        current_node = next_node
        visited.add(current_node)

    return path, total_cost


# Call the function
start_node = 'S'
(path, total_cost) = greedy_graph_search(graph, heuristic_costs, start_node)

# Print the result
print(f"Path: {' -> '.join(path)}")
print(f"Total Cost: {total_cost}")
