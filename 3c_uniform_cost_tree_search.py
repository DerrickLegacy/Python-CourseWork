import heapq

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


def uniform_cost_tree_search(graph, start):
    # Step 1: Start with a priority queue frontier that contains initial state and its cost
    # [(priority, (current_node, current_path))]
    priority_queue = [(0, (start, [start]))]

    least_cost = float('inf')  # Initialize least_cost with infinity

    while priority_queue:
        # Step 2: If frontier is empty, then no solution
        if not priority_queue:
            print("No solution, Frontier is empty !")
        else:
            # step3: Pop the node with the lowest cost from the priority queue
            (priority, (node, path)) = heapq.heappop(priority_queue)

            # step 4: Check if we've reached the goal node
            if node == 'G':
                if priority < least_cost:
                    least_cost = priority  # Update least_cost if a lower cost path is found
                    least_cost_path = path  # Also keep track of the corresponding path

            # step 5: Else expand to neighbors(the children) of the current node
            neighbors = graph[node]
            # print(graph[node])
            # print(neighbors.items())
            # a) Iterate through children of the current node and add them to the queue
            for neighbor, cost in neighbors.items():
                if neighbor not in path:
                    # print(neighbor)
                    # print(neighbor)
                    # b) Calculate the new cost (path cost + edge cost)
                    new_cost = priority + cost
                    # c) Enqueue neighbor and its path with the new cost
                    heapq.heappush(priority_queue, (new_cost,
                                   (neighbor, path + [neighbor])))

    if least_cost != float('inf'):
        print(f"Least Uniform Cost: {least_cost}")
        return least_cost_path


# Calling the Uniform Cost Tree Search function with 'S' as the starting node
result = uniform_cost_tree_search(graph, 'S')

# Print the final path
if result is not None:
    # Print the last element of the result (which is 'G')
    print("Uniform Cost Tree Search Path found:", result)
else:
    print("No solution found.")
