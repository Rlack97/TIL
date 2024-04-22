# 다익스트라
import sys
import heapq
input = sys.stdin.readline
# 교차로 / 교차로 이동 거리 정보 기록
# 국왕이 방문한 도로들의 사용 시간 기록
# 다익스트라를 통해 상근의 최단거리(시간) 구하기
# 간선이 사용 중이라면 현재 시간과 비교해서 기다리는 시간을 구함.

N, M = map(int, input().split())
A, B, K, G = map(int, input().split())
godul = list(map(int, input().split()))
godul_time = [0 for _ in range(G-1)]
INF = 1e9
nodes = [[]for _ in range(N+1)]
for _ in range(M):
    # 교차로 간 간선 연결 리스트
    U, V, L = map(int, input().split())
    nodes[U].append([V, L])
    nodes[V].append([U, L])

    # 왕이 연속적으로 방문하는 교차로의 정보일 경우 (U->V로 이동하는 경우)
    if U in godul and V in godul and abs(godul.index(U)-godul.index(V)) == 1:
        # 왕이 교차로 U,V 사이를 이동할 때의 시간
        # = 시간 리스트에서 U,V중 나중에 방문하는 교차로의 index값
        if godul.index(U) > godul.index(V):
            godul_time[godul.index(V)] = L
        else:
            godul_time[godul.index(U)] = L

# 교차로 수만큼 반복
for i in range(1, G-1):
    godul_time[i] += godul_time[i-1]
    # 0초 시작, 국왕이 해당 도로에서 보낸 시간을 구한다. (누적)


def get_GD(cur_cost):
    for i in range(G-1):
        if cur_cost < godul_time[i]:
            return (godul[i], godul[i+1], godul_time[i])
        # 현재 시간에 국왕이 위치한 도로 (노드 번호 두 개로 표시) 및 그곳에서 나올 때까지 걸리는 시간 리턴
    return (-1, -1, -1)

# 다익스트라 알고리즘


def Dijsktra(start, k):
    # 노드 수만큼의 거리 리스트
    distances = [INF for _ in range(N+1)]
    # k분 있다 출발
    distances[start] = K

    # 큐 생성 및 시작 위치, 시간 기록
    pq = []
    heapq.heappush(pq, [K, start])

    # 큐가 사라질때까지 반복
    while pq:
        # 현재 시간, 위치를 큐에서 추출
        cur_cost, cur_node = heapq.heappop(pq)

        # 현재 시간이 기록 시간보다 크면 이후 생략
        if distances[cur_node] < cur_cost:
            continue

        GD_node1, GD_node2, GD_time = get_GD(cur_cost)
        # 현재 시간 국왕의 위치 및 그곳에서 보내는 총 시간

        for next_node, next_cost in nodes[cur_node]:
            wait_cost = 0

            if (GD_node1 == cur_node and GD_node2 == next_node) or (GD_node1 == next_node and GD_node2 == cur_node):
                wait_cost = GD_time - cur_cost
                # 이용 간선이 국왕이 사용 중이라면 현재 시간과 비교, 기다리는 시간을 구한다.

            if distances[next_node] > wait_cost + cur_cost + next_cost:
                distances[next_node] = wait_cost + cur_cost + next_cost
                heapq.heappush(pq, [distances[next_node], next_node])

    return distances[B] - K  # 상근 입장에서 '배달을 마치는' 시간이므로 k 있다 출발한 것을 감산.


print(Dijsktra(A, K))
