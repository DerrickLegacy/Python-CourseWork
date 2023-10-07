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

def greedy_tree_search(graph, heuristic_costs, start):
    path = []
    total_cost = 0

    current_node = start
    while True:
        path.append(current_node)

        if current_node == 'G':
            break

        neighbors = graph[current_node]
        next_node = None
        min_cost = float('inf')

        for neighbor, cost in neighbors.items():
            if heuristic_costs[neighbor] < min_cost:
                min_cost = heuristic_costs[neighbor]
                next_node = neighbor
            elif heuristic_costs[neighbor] == min_cost and neighbor < next_node:
                next_node = neighbor

        if next_node is None:
            break

        total_cost += graph[current_node][next_node]
        current_node = next_node

    return path, total_cost 




# Call the function
start_node = 'S'
(path, total_cost) = greedy_tree_search(graph, heuristic_costs, start_node)

# Print the result with the additional information
expanded_states = set(path)
not_expanded_states = set(graph.keys()) - expanded_states

print(f"Order of States Expanded: {expanded_states}")
print(f"Path Returned by Greedy Search: {path}")
print(f"States that are Not Expanded: {not_expanded_states}")
