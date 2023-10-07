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


def bfs_tree_search(graph, start):
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
expanded_states, path = bfs_tree_search(graph, 'S')

# Print the results
print(f"Order of States Expanded: {expanded_states}")
print(f"Path Returned by Tree Search: {path}")
print(f"States that are Not Expanded: {set(graph.keys()) - expanded_states}")


"""
Explanation for each iteration:

Iteration 1:

Expanded: S
Queue: [(A, [S]), (B, [S])]
Expanded States: {S}
Iteration 2:

Expanded: A
Queue: [(B, [S]), (B, [A]), (C, [A])]
Expanded States: {S, A}
Iteration 3:

Expanded: B
Queue: [(B, [A]), (C, [A]), (C, [B])]
Expanded States: {S, A, B}
Iteration 4:

Expanded: C
Queue: [(C, [A]), (C, [B]), (D, [C]), (G, [C])]
Expanded States: {S, A, B, C}
Iteration 5:

Expanded: D
Queue: [(C, [B]), (G, [C]), (G, [D])]
Expanded States: {S, A, B, C, D}
Iteration 6:

Expanded: G
Queue: [(C, [B]), (G, [D])]
Expanded States: {S, A, B, C, D, G}
Iteration 7:

Expanded: G (again, but ignored as it's already expanded)
Queue: [(C, [B])]
Final Results:

Order of States Expanded: {S, A, B, C, D, G}
Path Returned by Tree Search: ['S', 'B', 'C', 'G']
States that are Not Expanded: {} (All states are expanded)
So, the final path from 'S' to 'G' is ['S', 'B', 'C', 'G']. All states have been expanded, and there are no states left unexpanded.
"""
