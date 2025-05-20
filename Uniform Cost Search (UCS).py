import heapq

def ucs(graph, start, goal):
    visited = set()
    pq = [(0, start)]
    
    while pq:
        cost, node = heapq.heappop(pq)
        if node == goal:
            return cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                heapq.heappush(pq, (cost + weight, neighbor))
    return float('inf')
