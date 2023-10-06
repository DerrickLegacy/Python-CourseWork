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


def dfs_graph_search(graph, start):
    # stack node represented as (state, [current path])
    stack = [(start, [start])]
    visited = set()  # Initialize an empty set to keep track of visited nodes

    while stack:
        if not stack:
            print("No solution")
        else:
            (node, path) = stack.pop()

            if node == 'G':
                return path  # in iteration 1 path = [s]

            if node not in visited:  # Check if the node has not been visited
                # Mark and add the node in the visited list eg in first iteration list has s
                visited.add(node)

                # node neighbour will now be {'A': 3, 'B': 1} in iteration
                neighbors = graph[node]

                for neighbor, cost in neighbors.items():
                    if neighbor not in path:
                        # New paths in stack: [('A', ['S', 'A']), ('B', ['S', 'B'])]
                        stack.append((neighbor, path + [neighbor]))

    return None


# Calling the DFS function with 'S' as the starting node
result = dfs_graph_search(graph, 'S')

if result is not None:
    print("Depth first Graph Search Path found:", result)
else:
    print("No solution found.")


"""
EXPLANATION
Initialization:

Start node: 'S'
Stack: [('S', ['S'])] (Current node is 'S', path is just 'S')
Visited set: set()
Iteration 1:

Pop node 'S' from the stack.
Check if 'S' is the goal node. It's not.
'S' is added to the visited set.
Expand neighbors of 'S': {'A': 3, 'B': 1}
New paths in stack: [('A', ['S', 'A']), ('B', ['S', 'B'])]
Visited set: {'S'}
Iteration 2:

Pop node 'B' from the stack.
Check if 'B' is the goal node. It's not.
'B' is added to the visited set.
Expand neighbors of 'B': {'S': 1, 'A': 2, 'C': 3}
New paths in stack: [('A', ['S', 'A']), ('A', ['S', 'B', 'A']), ('C', ['S', 'B', 'C'])]
Visited set: {'S', 'B'}
Iteration 3:

Pop node 'C' from the stack.
Check if 'C' is the goal node. It's not.
'C' is added to the visited set.
Expand neighbors of 'C': {'A': 2, 'B': 3, 'D': 3, 'G': 4}
New paths in stack: [('A', ['S', 'A']), ('A', ['S', 'B', 'A']), ('D', ['S', 'B', 'C', 'D']), ('G', ['S', 'B', 'C', 'G'])]
Visited set: {'S', 'B', 'C'}
Iteration 4:

Pop node 'G' from the stack.
Check if 'G' is the goal node. It is.
Path 'S -> B -> C -> G' is the solution.
Result:

Path found: ['S', 'B', 'C', 'G']
In this example, the algorithm starts at 'S', explores its neighbors 'A' and 'B', then continues to explore 'A' and 'C'. It eventually finds the goal node 'G'. The visited set ensures that nodes are not revisited, preventing infinite loops in cyclic graphs.
"""
