# 240216
# MST (최소 스패닝 트리)
# find - union
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# 가중치 기준으로 정렬
costs = [list(map(int, input().split()))for _ in range(M)]
costs.sort(key=lambda x: x[2])

# 자기 자신을 조상으로 초기화
parent = [i for i in range(N+1)]
answer = 0


def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for a, b, cost in costs:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += cost

print(answer)
