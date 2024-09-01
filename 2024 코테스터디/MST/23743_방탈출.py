import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hq = []
for _ in range(M):
    a, b, c = list(map(int, input().split()))
    heapq.heappush(hq, (c, a, b))

# 출구 = 0번노드, 비상탈출구 = 0번노드로의 워프
exit_time = list(map(int, input().split()))
for i in range(N):
    heapq.heappush(hq, (exit_time[i], 0, i+1))

parents = [i for i in range(N+1)]


def find(x):
    if x == parents[x]:
        return x

    else:
        parents[x] = find(parents[x])
        return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False
    else:
        parents[b] = a
        return True


total = 0
edge_cnt = 0
while hq:
    cost, node1, node2 = heapq.heappop(hq)
    if union(node1, node2):
        total += cost
        edge_cnt += 1
        if edge_cnt == N:
            break

print(total)
