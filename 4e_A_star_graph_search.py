import heapq

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


def astar_graph_search(graph, heuristic_costs, start, goal):
    open_list = [(heuristic_costs[start], 0, start, [start])]
    visited = set()

    while open_list:
        _, cost, current, path = heapq.heappop(open_list)

        if current == goal:
            return cost, path

        if current in visited:
            continue

        visited.add(current)

        for neighbor, weight in graph[current].items():
            new_cost = cost + weight
            new_path = path + [neighbor]
            priority = new_cost + heuristic_costs[neighbor]
            heapq.heappush(open_list, (priority, new_cost, neighbor, new_path))


# Call the function
start_node = 'S'
goal_node = 'G'
total_cost, path_taken = astar_graph_search(
    graph, heuristic_costs, start_node, goal_node)

# Print the result
print(f"Total Cost from {start_node} to {goal_node}: {total_cost}")
print(f"Path Taken: {' -> '.join(path_taken)}")
