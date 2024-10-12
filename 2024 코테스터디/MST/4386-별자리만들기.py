import sys, math

input = sys.stdin.readline

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
# x,y 좌표


# 두 좌표 사이의 거리
def cost(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


parent = [i for i in range(n)]


# 유니온 파인드
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


edges = []
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        dist = cost(x1, y1, x2, y2)
        edges.append((dist, i, j))

edges.sort()

answer = 0
for edge in edges:
    dist, a, b = edge
    if find(a) != find(b):
        union(a, b)
        answer += dist


# 소수점 둘째자리까지 출력
print(f"{answer:.2f}")
