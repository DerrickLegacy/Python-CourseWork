import heapq

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

def uniform_cost_graph_search(graph, start):
    priority_queue = [(0, (start, [start]))]
    visited = set()  # Initialize an empty set to keep track of visited nodes
    least_cost = float('inf')  # Initialize least_cost with infinity

    while priority_queue:
        if not priority_queue:
            print("No solution, Frontier is empty !")
        else:
            (priority, (node, path)) = heapq.heappop(priority_queue)

            if node == 'G':
                if priority < least_cost:
                    least_cost = priority
                    least_cost_path = path

            if node not in visited:
                visited.add(node)

                neighbors = graph[node]

                for neighbor, cost in neighbors.items():
                    if neighbor not in path:
                        new_cost = priority + cost
                        heapq.heappush(priority_queue, (new_cost, (neighbor, path + [neighbor])))

    if least_cost != float('inf'):
        print(f"Least Uniform Cost: {least_cost}")
        return least_cost_path

# Calling the Uniform Cost Graph Search function with 'S' as the starting node
result = uniform_cost_graph_search(graph, 'S')

# Print the final path
if result is not None:
    print("Uniform Cost Graph Search Path found:", result)
else:
    print("No solution found.")
