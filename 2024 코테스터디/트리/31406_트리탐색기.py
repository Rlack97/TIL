import sys
sys.setrecursionlimit(10**4)
r = sys.stdin.readline

N, Q = map(int, r().split())

graph = [[] for _ in range(N+1)]
toggle = [0]*(N+1)
toggle[1] = 1

depth = [0]*(N+1)
order = []


def dfs(n, d):
    order.append(n)
    depth[n] = d
    for e in graph[n]:
        dfs(e, d+1)


for i in range(1, N+1):
    a = list(map(int, r().split()))
    if a[0] == 0:
        continue
    for j in range(a[0]):
        graph[i].append(a[j+1])

dfs(1, 0)


def forward(k, cursor):
    i = 0
    d = 2001
    tmpCursor = cursor
    while i < k:
        if tmpCursor == N-1:
            break
        if not toggle[order[tmpCursor]] and d == 2001:
            d = depth[order[tmpCursor]]
        tmpCursor += 1
        if depth[order[tmpCursor]] > d:
            continue
        d = 2001
        i += 1
        cursor = tmpCursor
    return cursor


def getLocFromTop(target):
    loc = 0
    d = 2001
    tmpCursor = 1
    while order[tmpCursor] != target:
        if not toggle[order[tmpCursor]] and d == 2001:
            d = depth[order[tmpCursor]]
        tmpCursor += 1
        if depth[order[tmpCursor]] > d:
            continue
        d = 2001
        loc += 1
    return loc


cursor = 1
for _ in range(Q):
    cmd = r().split()

    if cmd[0] == "toggle":
        toggle[order[cursor]] = not toggle[order[cursor]]
    else:
        k = int(cmd[1])
        if k >= 0:
            cursor = forward(k, cursor)
        else:
            k *= -1
            loc = getLocFromTop(order[cursor])
            cursor = forward(loc-k, 1)
        print(order[cursor])
