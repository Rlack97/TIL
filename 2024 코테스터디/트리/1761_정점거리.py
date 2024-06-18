# (LCA)최소 공통 조상 + 조상까지의 거리
# x = Parent[x]를 반복
# 깊이가 다르면 계산에 문제가 생김 => 깊이를 맞춰줘야...
# 부모 배열을 2차원화
# parent[x][k] = '노드 x의 2의 k제곱번째의 조상 노드'
# parent[x][k] = parent[parent[x][k - 1]][k - 1]
# 두 정점 거리 계산은 루트 노드 기준으로 a노드거리 + b노드거리 -2(조상노드거리)

import math
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
LOG = math.ceil(math.log2(N))
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

depth = [-1] * (N+1)
parent = [[-1]*LOG for _ in range(N+1)]
# 부모는 2의 제곱수 갯수만큼만 보면 되서 LOG값을 사용하나?
dist = [0] * (N+1)
# 루트에서부터의 거리

# 부모, 깊이 기록을 위한 DFS


def dfs(cur, d):
    # 현재깊이 기록
    depth[cur] = d

    # 해당 노드가 갖고있는 연결정보를 순회
    for next, cost in graph[cur]:
        # 깊이가 기록되지 않은 노드가 있다면 (방문 이전)
        if depth[next] == -1:

            # 현재 노드를 부모노드로 기록
            parent[next][0] = cur
            # 거리정보에 현재 거리를 추가
            dist[next] = dist[cur] + cost
            # 재귀
            dfs(next, d+1)


# 루트노드 1, 깊이 0으로 재귀 시작
dfs(1, 0)

for i in range(1, LOG):
    # 2의 제곱수의 갯수(로그)만큼 순회
    for j in range(1, N+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]
        # j의 2^k제곱수 부모 노드 배열은
        # 각 2^k-1제곱수 부모 노드와 겹친다
        # 13의 1,2,4번째 부모노드가 9,5,1이라면
        # 5는 9의 1번째 부모노드
        # 1은 5의 2번째 부모노드와 같다


def LCA(a, b):
    # 뒷 수가 더 깊은 곳에 있도록 정렬
    if depth[a] > depth[b]:
        a, b = b, a

    need = depth[b] - depth[a]
    for i in range(LOG-1, -1, -1):
        if need >= (1 << i):
            b = parent[b][i]
            need -= 1 << i

    if a == b:
        return a

    for i in range(LOG-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]


answer = []
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    answer.append(dist[a] + dist[b] - 2 * dist[LCA(a, b)])

print(*answer, sep='\n')
