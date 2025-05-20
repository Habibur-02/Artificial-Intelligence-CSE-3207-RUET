def a_star(graph, start, goal, heuristic):
    visited = set()
    pq = [(heuristic[start], 0, start)]
    
    while pq:
        f, g, node = heapq.heappop(pq)
        if node == goal:
            return g
        if node not in visited:
            visited.add(node)
            for neighbor, cost in graph[node]:
                heapq.heappush(pq, (g + cost + heuristic[neighbor], g + cost, neighbor))
    return float('inf')
