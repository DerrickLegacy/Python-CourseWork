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
    expanded_states = set()

    while queue:
        if not queue:
            break
        else:
            node, path = queue.pop(0)
            if node not in expanded_states:
                expanded_states.add(node)
                neighbors = graph[node]
                # Sort neighbors alphabetically
                for neighbor, cost in sorted(neighbors.items()):
                    if neighbor not in path:
                        queue.append((neighbor, path + [neighbor]))

    return expanded_states, path

# Calling the BFS function with 'S' as the starting node
expanded_states, path = bfs_graph_search(graph, 'S')

# Print the results
print(f"Order of States Expanded: {expanded_states}")
print(f"Path Returned by Graph Search: {path}")
print(f"States that are Not Expanded: {set(graph.keys()) - expanded_states}")
