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


def astar_tree_search(graph, heuristic_costs, start, goal):
    open_list = [(0 + heuristic_costs[start], 0, start)]
    while open_list:
        _, cost, current = heapq.heappop(open_list)
        if current == goal:
            return cost
        for neighbor, weight in graph[current].items():
            new_cost = cost + weight
            heapq.heappush(
                open_list, (new_cost + heuristic_costs[neighbor], new_cost, neighbor))


# Call the function
start_node = 'S'
goal_node = 'G'
total_cost = astar_tree_search(graph, heuristic_costs, start_node, goal_node)

# Print the result
print(f"Total Cost from {start_node} to {goal_node}: {total_cost}")
