#0229
import sys
input = sys.stdin.readline
# 크루스칼 알고리즘 (find-union)
# 가장 적은 비용으로, 사이클 없이, 모든 정점을 연결


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

N, M = map(int, input().split())

edges = []
parent = list(range(N + 1))
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

# 가중치 (유지비) 기준으로 정렬
edges.sort(key=lambda x: x[2])

answer = 0
last_edge = 0

for a, b, c in edges:
    # a,b 두 집의 부모가 노드가 같지 않다면 = 같은 사이클 내에 없다면
    if find(a) != find(b):
        # 두 노드를 최소 신장 트리에 더해주고
        union(a, b)
        answer += c # 유지비를 더함 (MST이므로 최소값이 됨)
        last_edge = c # 마지막의, 가장 유지비가 큰 길의 값

# 최소신장 트리에서 유지비가 가장 큰 간선을 지워 집 하나를 분리 = 마을 두 개가 됨.
print(answer - last_edge)