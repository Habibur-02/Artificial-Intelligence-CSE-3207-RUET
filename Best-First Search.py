import heapq

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = [(heuristic[start], start)]
    
    while pq:
        _, current = heapq.heappop(pq)
        if current == goal:
            return True  # Goal found

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(pq, (heuristic[neighbor], neighbor))
    
    return False  # Goal not found

# Example
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
heuristic = {'A': 3, 'B': 2, 'C': 4, 'D': 0, 'E': 1}

print(best_first_search(graph, 'A', 'D', heuristic))
