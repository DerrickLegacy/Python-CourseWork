import heapq

graph = {
    'S': {'A': 3, 'B': 1},
    'B': {'S': 1, 'A': 2, 'C': 3},
    'A': {'S': 3, 'B': 2, 'C': 2},
    'C': {'A': 2, 'B': 3, 'D': 3, 'G': 4},
    'D': {'C': 4, 'G': 1},
    'G': {'C': 4, 'D': 1}
}

def uniform_cost_graph_search(graph, start, goal):
    visited = set()
    priority_queue = [(0, start, [start])]

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            neighbors = graph[node]
            for neighbor, neighbor_cost in neighbors.items():
                if neighbor not in visited:
                    heapq.heappush(
                        priority_queue, (cost + neighbor_cost, neighbor, path + [neighbor]))
    return []


# Start and goal nodes
start_node = 'S'
goal_node = 'G'

# Perform graph search UCS
path = uniform_cost_graph_search(graph, start_node, goal_node)

# Print results
print(f"Order of States Expanded: {path}")
print(f"Path Returned by Uniform Cost Search: {path}")
print(f"States that are Not Expanded: {set(graph.keys()) - set(path)}")
