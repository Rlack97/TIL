import sys

input = sys.stdin.readline

from collections import defaultdict, deque


def floyd_warshall(n, graph):
    # 모든 노드 간의 최단 거리를 무한대로 초기화
    dist = [[float("inf")] * n for _ in range(n)]

    # 자기 자신으로의 거리는 0으로 설정
    for i in range(n):
        dist[i][i] = 0

    # 그래프 간선에 따라 초기 거리 설정
    for u in graph:
        for v in graph[u]:
            dist[u - 1][v - 1] = 1
            dist[v - 1][u - 1] = 1

    # 플로이드-워셜 알고리즘으로 모든 쌍의 최단 거리 계산
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def find_representatives(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    committees = []

    # bfs를 통해 위원회 구분하기
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        component = []

        while queue:
            node = queue.popleft()
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return component

    # 각 사람(번호)를 확인하면서 각 위원회(리스트)를 기록
    for i in range(1, n + 1):
        if not visited[i]:
            component = bfs(i)
            committees.append(component)

    # 모든 쌍의 최단 거리 계산
    dist = floyd_warshall(n, graph)

    representatives = []

    # 대표를 선정
    for committee in committees:
        min_max_distance = float("inf")
        representative = -1
        for member in committee:
            max_distance = max(dist[member - 1][m - 1] for m in committee)
            if max_distance < min_max_distance:
                min_max_distance = max_distance
                representative = member
        representatives.append(representative)

    representatives.sort()

    return len(committees), representatives


# 입력 처리
n = int(input())
m = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# 위원회 수와 대표 리스트 출력
committee_count, representatives = find_representatives(n, edges)
print(committee_count)
for rep in representatives:
    print(rep)
