import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
power = list(map(int, input().split()))
cables = [list(map(int, input().split())) for _ in range(M)]

cables.sort(key=lambda x: x[2])

# 0번 도시는 없으므로 N+1
parent = [i for i in range(N + 1)]


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


# 발전소끼리 전부 union시켜버리기
for p in power:
    union(power[0], p)

total = 0
for a, b, cost in cables:
    if find(a) != find(b):
        union(a, b)
        total += cost


print(total)
