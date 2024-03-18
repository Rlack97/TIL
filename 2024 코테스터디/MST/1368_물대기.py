# 0315

# 우물 제작이 가장 싼 곳에 우물 생성
# 최소 스패닝 트리를 통해 낭비 없이 모든 논을 연결
# 만약 옆과 연결하는것보다 만드는게 더 싸면 연결하지 않음

# 수정 ) 0번째의 새로운 노드 생성, 해당 노드와의 연결비용 = 우물제작 비용
# 연결보다 생성을 먼저 검토해야 하므로 루트노드인 0번째 노드로 둬야함

import sys
input = sys.stdin.readline


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


N = int(input())
parent = list(range(N+1))
edges = []

# edges (간선리스트)에 0번째 노드 = 우물파기 가격을 기록
for i in range(N):
    edges.append((i, 0, int(input())))

# 추가 간선정보를 받음. 0번 노드는 사용중이므로 1번부터
for i in range(1, N+1):
    P = list(map(int, input().split()))
    for j in range(i+1, N+1):
        edges.append((i, j, P[j-1]))

# 비용 기준으로 정렬
edges.sort(key=lambda x: x[2])
answer = 0

for (a, b, c) in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c


print(answer)
