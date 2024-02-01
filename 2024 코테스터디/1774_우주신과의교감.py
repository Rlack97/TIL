# 240201
# 크루스칼 알고리즘 = 최소 간선 트리
'''
 1. 간선 정보를 오름차순 정렬
 2. 간선 정보를 확인하면서 사이클 발생 유무 확인
     노드들의 부모 노드가 같다면 사이클이 발생.
 3. 사이클이 발생하지 않으면 최소 신장 트리에 포함
 4. 1~3의 과정을 모든 간선에 대해 수행

 서로소 집합 자료구조: 노드들 간의 부모-자식 관계를 가정,
 값이 작은쪽이 부모.
 부모 리스트를 전부 갱신했을때 값이 다르면 두 집합은 서로소 (공유되는 값이 없다)
'''

import sys
input = sys.stdin.readline

# find 연산
# 부모 노드를 알아내는 연산


def find(parent, x):
    # 부모 노드가 자기 자신이 아님 == 별도의 부모노드 존재
    if x != parent[x]:
        # 해당 부모노드의 부모노드를 재귀탐색
        parent[x] = find(parent, parent[x])

    # 부모노드가 자기 자신이라면 그대로 리턴
    return parent[x]

# union 연산


def union(parent, a, b):
    # 두 노드의 부모노드를 탐색
    a = find(parent, a)
    b = find(parent, b)

    # 각 부모노드를 비교한 후 값이 작은 쪽을 부모 노드라고 가정하고 기록한다.
    if a < b:
        parent[b] = a

    else:
        parent[a] = b

# 두 좌표간 거리를 구하는 함수


def get_dist(loc1, loc2):
    x1, y1, x2, y2 = loc1[0], loc1[1], loc2[0], loc2[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


N, M = map(int, input().split())

# 부모노드를 기록할 리스트. 초기화 시에는 자기 자신만 기록되어 있어야 함.
parent = list(range(N+1))

# 우주신들의 좌표 기록
edges = [0] * (N+1)
for i in range(1, N+1):
    edges[i] = list(map(int, input().split()))

# 각 우주신들의 연결정보. union함수를 이용해 부모노드를 기록.
for _ in range(M):
    a, b = map(int, input().split())
    union(parent, a, b)

# 각 우주신들 간의 거리를 구한다 [거리, 노드1, 노드2] 형태로 기록
possible = []
for i in range(1, len(edges)-1):
    for j in range(i+1, len(edges)):
        possible.append([get_dist(edges[i], edges[j]), i, j])

# 거리가 가장 짧은 순대로 기록한다.
possible.sort()
ans = 0

# 기록한 거리 정보에서,
for p in possible:
    cost, x, y = p[0], p[1], p[2]

    # 이미 존재하고 있는 연결이 아니라면
    if find(parent, x) != find(parent, y):

        # 부모 노드 기록을 갱신하고
        union(parent, x, y)

        # 값을 추가한다.
        ans += cost

print("{:.2f}".format(ans))
