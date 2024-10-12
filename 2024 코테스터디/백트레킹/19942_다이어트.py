import sys

input = sys.stdin.readline

N = int(input())
mp, mf, ms, mv = map(int, input().split())

ingredients = [list(map(int, input().split())) for _ in range(N)]

min_cost = float("inf")
combi = []
final_com = []


def dfs(p, f, s, v, c, idx):
    global min_cost, final_com

    # 현재 비용이 이미 최소 비용보다 크면 더 이상 탐색하지 않음 (Pruning)
    if c >= min_cost:
        return

    # 모든 영양소 기준을 충족했을 때
    if p >= mp and f >= mf and s >= ms and v >= mv:
        if c < min_cost:
            min_cost = c
            final_com = combi[:]
        return

    # 현재 인덱스 이후로 식재료 탐색 (idx를 사용하여 방문한 재료를 다시 방문하지 않음)
    for n in range(idx, N):
        combi.append(n + 1)
        np, nf, ns, nv, nc = ingredients[n]
        dfs(p + np, f + nf, s + ns, v + nv, c + nc, n + 1)
        combi.pop()


dfs(0, 0, 0, 0, 0, 0)

if min_cost == float("inf"):
    print(-1)
else:
    print(min_cost)
    print(*final_com)
