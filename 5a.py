def dfs_tree_search(graph, start, goal):
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
            for neighbor in sorted(neighbors.keys()):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return []


# Given data
graph = {
    'S': {'A': 3, 'B': 1},
    'B': {'S': 1, 'A': 2, 'C': 3},
    'A': {'S': 3, 'B': 2, 'C': 2},
    'C': {'A': 2, 'B': 3, 'D': 3, 'G': 4},
    'D': {'C': 4, 'G': 1},
    'G': {'C': 4, 'D': 1}
}

# Start and goal nodes
start_node = 'S'
goal_node = 'G'

# Perform tree search DFS
path = dfs_tree_search(graph, start_node, goal_node)

# Print results
print(f"Order of States Expanded: {path}")
print(f"Path Returned by Tree Search: {path}")
print(f"States that are Not Expanded: {set(graph.keys()) - set(path)}")
