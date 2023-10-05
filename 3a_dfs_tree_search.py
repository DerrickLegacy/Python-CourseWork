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


def dfs_tree_search(graph, start):
    # Step 1: Start with a stack frontier that contains initial state
    # Each element in the stack is a tuple containing the current node and a list of visited nodes
    stack = [(start, [start])]  # [(current_node, current_path)]

    while stack:
        # Step 2: If frontier is empty, then no solution
        if not stack:
            print("No solution")
        else:
            # step3: Pop or remove the top node and its path
            # pop() - Will remove the last item from the list incase we dont provide the index at wic to remove.
            (node, path) = stack.pop()

            # step 4: Check if we've reached the goal node
            if node == 'G':
                return path

            # step 5: Else expand to neighbors(the children) of the current node
            neighbors = graph[node]

            # a) Iterate through children of the current node
            for neighbor, cost in neighbors.items():
                if neighbor not in path:
                    # b) Expand the node and add resulting nodes to the frontier
                    # c) Push neighbor and its path to the stack
                    stack.append((neighbor, path + [neighbor]))
    # If no solution is found, return None
    return None


# Calling the DFS function with 'S' as the starting node
result = dfs_tree_search(graph, 'S')

if result is not None:
    print("Depth first Tree Search Path found:", result)
else:
    print("No solution found.")
