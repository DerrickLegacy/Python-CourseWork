import heapq

graph = {
    'S': {'A': 3, 'B': 1},
    'B': {'S': 1, 'A': 2, 'C': 3},
    'A': {'S': 3, 'B': 2, 'C': 2},
    'C': {'A': 2, 'B': 3, 'D': 3, 'G': 4},
    'D': {'C': 4, 'G': 1},
    'G': {'C': 4, 'D': 1}
}


def uniform_cost_search(graph, start, goal):
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

# Perform uniform cost search
path = uniform_cost_search(graph, start_node, goal_node)

# Print results
print(f"Order of States Expanded: {path}")
print(f"Path Returned by Uniform Cost Search: {path}")
print(f"States that are Not Expanded: {set(graph.keys()) - set(path)}")


"""
Explanation:
Iteration 1:

node = 'S'
path = ['S']
neighbors = {'A': 3, 'B': 1}
For each neighbor:

neighbor = 'A'

neighbor_cost = 3

cost = 0 + 3 = 3

new_path = ['S', 'A']

priority_queue: [(3, 'A', ['S', 'A'])]

neighbor = 'B'

neighbor_cost = 1

cost = 0 + 1 = 1

new_path = ['S', 'B']

priority_queue: [(1, 'B', ['S', 'B']), (3, 'A', ['S', 'A'])]

Iteration 2:

node = 'B'
path = ['S', 'B']
neighbors = {'S': 1, 'A': 2, 'C': 3}
For each neighbor:

neighbor = 'S'

neighbor_cost = 1

cost = 1 + 1 = 2

new_path = ['S', 'B', 'S']

priority_queue: [(2, 'S', ['S', 'B', 'S']), (3, 'A', ['S', 'A'])]

neighbor = 'A'

neighbor_cost = 2

cost = 1 + 2 = 3

new_path = ['S', 'B', 'A']

priority_queue: [(2, 'S', ['S', 'B', 'S']), (3, 'A', ['S', 'A']), (3, 'A', ['S', 'B', 'A'])]

neighbor = 'C'

neighbor_cost = 3

cost = 1 + 3 = 4

new_path = ['S', 'B', 'C']

priority_queue: [(2, 'S', ['S', 'B', 'S']), (3, 'A', ['S', 'A']), (3, 'A', ['S', 'B', 'A']), (4, 'C', ['S', 'B', 'C'])]

Iteration 3:

node = 'A'
path = ['S', 'B', 'A']
neighbors = {'S': 3, 'B': 2, 'C': 2}
For each neighbor:

neighbor = 'S'

neighbor_cost = 3

cost = 3 + 3 = 6

new_path = ['S', 'B', 'A', 'S']

priority_queue: [(2, 'S', ['S', 'B', 'S']), (3, 'A', ['S', 'A']), (3, 'A', ['S', 'B', 'A']), (4, 'C', ['S', 'B', 'C']), (6, 'S', ['S', 'B', 'A', 'S'])]

neighbor = 'B'

neighbor_cost = 2

cost = 3 + 2 = 5

new_path = ['S', 'B', 'A', 'B']

priority_queue: [(2, 'S', ['S', 'B', 'S']), (3, 'A', ['S', 'A']), (3, 'A', ['S', 'B', 'A']), (4, 'C', ['S', 'B', 'C']), (5, 'B', ['S', 'B', 'A', 'B']), (6, 'S', ['S', 'B', 'A', 'S'])]

neighbor = 'C'

neighbor_cost = 2

cost = 3 + 2 = 5

new_path = ['S', 'B', 'A', 'C']

priority_queue: [(2, 'S', ['S', 'B', 'S']), (3, 'A', ['S', 'A']), (3, 'A', ['S', 'B', 'A']), (4, 'C', ['S', 'B', 'C']), (5, 'B', ['S', 'B', 'A', 'B']), (5, 'C', ['S', 'B', 'A', 'C']), (6, 'S', ['S', 'B', 'A', 'S'])]

Iteration 4:

node = 'C'
path = ['S', 'B', 'A', 'C']
neighbors = {'A': 2, 'B': 3, 'D': 3, 'G': 4}
For each neighbor:

neighbor = 'A'

neighbor_cost = 2

cost = 5 + 2 = 7

new_path = ['S', 'B', 'A', 'C', 'A']

priority_queue: [(2, 'S', ['S', 'B', 'S']), (3, 'A', ['S', 'A']), (3, 'A', ['S', 'B', 'A']), (4, 'C', ['S', 'B', 'C']), (5, 'B', ['S', 'B', 'A', 'B']), (5, 'C', ['S', 'B', 'A', 'C']), (6, 'S', ['S', 'B', 'A', 'S']), (7, 'A', ['S', 'B', 'A', 'C', 'A'])]

neighbor = 'B'

neighbor_cost = 3

cost = 5 + 3 = 8

new_path = ['S', 'B', 'A', 'C', 'B']

priority_queue: [(2, 'S', ['S', 'B', 'S']), (3, 'A', ['S', 'A']), (3, 'A', ['S', 'B', 'A']), (4, 'C', ['S', 'B', 'C']), (5, 'B', ['S', 'B', 'A', 'B']), (5, 'C', ['S', 'B', 'A', 'C']), (6, 'S', ['S', 'B', 'A', 'S']), (7, 'A', ['S', 'B', 'A', 'C', 'A']), (8, 'B', ['S', 'B', 'A', 'C', 'B'])]

Iteration 5:

node = 'G'
Goal node reached, returns the path ['S', 'B', 'A', 'C', 'G'].
This explains how the priority queue is managed and how the algorithm selects the next node to explore based on the accumulated cost.    
"""
