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

def bfs_tree_search(graph, start):
    # Step 1: Start with a queue frontier that contains initial state
    queue = [(start, [start])]  # [(current_node, current_path)]

    while queue:
        # Step 2: If frontier is empty, then no solution
        if not queue:
            print("No solution")
        else:
            # step3: Dequeue or remove the front node and its path
            (node, path) = queue.pop(0)  # Pop the first element (front) from the queue

            # step 4: Check if we've reached the goal node
            if node == 'G':
                return path

            # step 5: Else expand to neighbors(the children) of the current node
            neighbors = graph[node]

            # a) Iterate through children of the current node
            for neighbor, cost in neighbors.items():
                if neighbor not in path:
                    # b) Expand the node and add resulting nodes to the frontier
                    # c) Enqueue neighbor and its path
                    queue.append((neighbor, path + [neighbor]))
        
    # Step 2: If no solution is found, return None
    print("No solution found.")

# Calling the BFS function with 'S' as the starting node
result = bfs_tree_search(graph, 'S')

# Print the final path
if result is not None:
    print("Breadth first Tree Search Path found:", result)  # Print the last element of the result (which is 'G')
else:
    print("No solution found.")

