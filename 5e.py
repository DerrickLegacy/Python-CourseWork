import heapq

def a_star_tree_search(graph, heuristic_costs, start):
    visited = set()
    priority_queue = [(heuristic_costs[start], start, [start])]

    while priority_queue:
        _, node, path = heapq.heappop(priority_queue)
        if node == 'G':
            return path
        if node not in visited:
            visited.add(node)
            neighbors = graph[node]
            for neighbor, cost in neighbors.items():
                if neighbor not in visited:
                    heapq.heappush(
                        priority_queue, (heuristic_costs[neighbor] + cost, neighbor, path + [neighbor]))
    return []


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

# Call the function
start_node = 'S'
path = a_star_tree_search(graph, heuristic_costs, start_node)

# Print the result with the additional information
expanded_states = set(path)
not_expanded_states = set(graph.keys()) - expanded_states

print(f"Order of States Expanded: {expanded_states}")
print(f"Path Returned by A* Tree Search: {path}")
print(f"States that are Not Expanded: {not_expanded_states}")
