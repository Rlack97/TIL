# 0224

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, r = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


ans = [0, 0]


def dfs(u, p, sum, flag):
    # 기가 노드까지의 간선 길이의 합
    if flag == 0:
        ans[0] = sum
    else:
        # 긴 가지의 길이
        ans[1] = max(ans[1], sum)
    # root가 아닌데 인접노드가 2개보다 많으면, 자식이 두개 -> giga
    # root인데 인접 노드가 2개 이상이면 ->  giga
    if flag == 0 and len(graph[u]) > 2 - int(u == r):
        flag, sum = 1, 0

    for v, w in graph[u]:
        if v == p:
            continue
        dfs(v, u, sum+w, flag)


dfs(r, r, 0, 0)

print(ans[0], ans[1])
