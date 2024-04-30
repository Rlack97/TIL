# roads = 간선리스트
# sourece = 시작점
# destination = 목적지
# heapq 기반 다익스트라?
from collections import deque


def solution(n, roads, sources, destination):
    answer = []
    # 인접리스트
    graph = [[] for _ in range(n + 1)]

    # 거리값 리스트
    costs = [-1 for _ in range(n + 1)]

    # 목적지이지만 출발점이어도 상관없음. 고로 시작지점 = 0
    costs[destination] = 0
    queue = deque([destination])

    # 인접리스트에 값 추가
    for n1, n2 in roads:
        graph[n1].append(n2)
        graph[n2].append(n1)

    while queue:
        x = queue.popleft()
        # 인접 노드들에 대해
        for node in graph[x]:
            # 거리값이 측정되지 않았다면
            if costs[node] == -1:
                # 인접노드를 대기열에 추가하고
                queue.append(node)
                # 해당 노드까지 가는 비용(1 고정)을 추가해서 기록함
                costs[node] = costs[x] + 1

    # 출발점 ( 사실 도착점 ) 까지 걸리는 코스트를 기록 후 출력
    for s in sources:
        answer.append(costs[s])
    return answer
