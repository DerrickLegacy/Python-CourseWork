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

def dfs_graph_search(graph, start, goal):
    visited = set()
    stack = [(start, [start])]

    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            neighbors = graph[node]
            # Sort neighbors alphabetically
            for neighbor in sorted(neighbors.keys(), reverse=True):  # Reverse to maintain the same order as the original DFS
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return []

# Start and goal nodes
start_node = 'S'
goal_node = 'G'

# Perform graph search DFS
path = dfs_graph_search(graph, start_node, goal_node)

# Print results
print(f"Order of States Expanded: {path}")
print(f"Path Returned by Graph Search: {path}")
print(f"States that are Not Expanded: {set(graph.keys()) - set(path)}")
