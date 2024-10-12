import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M)]
# 건물 번호 a, b 코스트 c
# 가중치 기준 정렬
graph.sort(key=lambda x: x[2])
# 모든 건물이 연결되도록 최소 비용의 도로를 사용
parent = [i for i in range(N + 1)]
answer = 0
connect = N


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


total = 0
for a, b, cost in graph:
    total += cost
    if find(a) != find(b):
        union(a, b)
        answer += cost
        connect -= 1

if connect > 1:
    print(-1)
else:
    print(total - answer)
