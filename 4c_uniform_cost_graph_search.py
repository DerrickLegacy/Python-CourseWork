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
                        heapq.heappush(
                            priority_queue, (new_cost, (neighbor, path + [neighbor])))

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


"""
 EXPLANATION
Certainly! Let's walk through the modified uniform cost graph search step by step using the provided graph:

python
Copy code
graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'S': 3, 'B': 2, 'C': 2},
    'B': {'S': 1, 'A': 2, 'C': 3},
    'C': {'A': 2, 'B': 3, 'D': 3, 'G': 4},
    'D': {'C': 4, 'G': 1},
    'G': {'C': 4, 'D': 1}
}
Let's start the execution:

Initialization:

Start node: 'S'
Priority queue: [(0, ('S', ['S']))]
Visited set: set()
Least cost initialized as infinity.
Iteration 1:

Pop node 'S' from the priority queue.
Check if 'S' is the goal node. It's not.
'S' is added to the visited set.
Expand neighbors of 'S': {'A': 3, 'B': 1}
New paths in priority queue: [(3, ('A', ['S', 'A'])), (1, ('B', ['S', 'B']))]
Visited set: {'S'}
Iteration 2:

Pop node 'B' from the priority queue.
Check if 'B' is the goal node. It's not.
'B' is added to the visited set.
Expand neighbors of 'B': {'S': 1, 'A': 2, 'C': 3}
New paths in priority queue: [(3, ('A', ['S', 'A'])), (2, ('A', ['S', 'B', 'A'])), (4, ('C', ['S', 'B', 'C']))]
Visited set: {'S', 'B'}
Iteration 3:

Pop node 'A' from the priority queue.
Check if 'A' is the goal node. It's not.
'A' is added to the visited set.
Expand neighbors of 'A': {'S': 3, 'B': 2, 'C': 2}
New paths in priority queue: [(2, ('B', ['S', 'B'])), (5, ('C', ['S', 'A', 'C']))]
Visited set: {'S', 'B', 'A'}
Iteration 4:

Pop node 'B' from the priority queue.
Check if 'B' is the goal node. It's not.
'B' is already in the visited set, so it's skipped.
No new paths are added to the priority queue.
Iteration 5:

Pop node 'C' from the priority queue.
Check if 'C' is the goal node. It's not.
'C' is added to the visited set.
Expand neighbors of 'C': {'A': 2, 'B': 3, 'D': 3, 'G': 4}
New paths in priority queue: [(5, ('D', ['S', 'A', 'C', 'D'])), (6, ('G', ['S', 'A', 'C', 'G']))]
Visited set: {'S', 'B', 'A', 'C'}
Iteration 6:

Pop node 'D' from the priority queue.
Check if 'D' is the goal node. It's not.
'D' is added to the visited set.
Expand neighbors of 'D': {'C': 4, 'G': 1}
New paths in priority queue: [(9, ('G', ['S', 'A', 'C', 'D', 'G']))]
Visited set: {'S', 'B', 'A', 'C', 'D'}
Iteration 7:

Pop node 'G' from the priority queue.
Check if 'G' is the goal node. It is.
Path 'S -> A -> C -> G' is the solution.
Result:

Least Uniform Cost: 9
Path found: ['S', 'A', 'C', 'G']
"""
