def DFS(graph, node, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            DFS(graph, neighbor, visited)

N = int(input())
M = int(input())

graph = {i: [] for i in range(1,N+1)}

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (N+1)
DFS(graph, 1, visited)

infected_count = sum (visited) - 1