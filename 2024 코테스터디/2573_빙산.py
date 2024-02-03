# # 240202 빙산

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())

# # 빙산 배열
# ices = [[] for n in range(N)]

# for n in range(N):
#     row = list(map(int, input().split()))
#     ices[n] = row


# def count_zero(a, b):
#     # 상하좌우 칸의 0의 갯수를 세는 함수
#     cnt = 0
#     if a != 0 and a != N-1:
#         if ices[a-1][b] == 0:
#             cnt += 1
#         if ices[a+1][b] == 0:
#             cnt += 1

#     if b != 0 and b != M-1:
#         if ices[a][b-1] == 0:
#             cnt += 1
#         if ices[a][b+1] == 0:
#             cnt += 1

#     return cnt


# # 각 칸의 값이 0이 아니라면, 자신의 상/하/좌/우에 0이 있는 만큼 값이 감소한 배열을 반환하는 함수
# def melt(before):
#     after = [[0 for _ in range(M)] for n in range(N)]

#     for n in range(N):
#         for m in range(M):
#             if before[n][m] != 0:
#                 num_zero = count_zero(n, m)
#                 after[n][m] = before[n][m] - num_zero
#                 if before[n][m] - num_zero < 0:
#                     after[n][m] = 0

#     return after


# # 빙산의 덩어리를 세는 함수
# def cluster_count(map):
#     visited = [[0 for _ in range(M)] for n in range(N)]
#     cnt = 0
#     for n in range(N):
#         for m in range(M):
#             if map[n][m] and not visited[n][m]:
#                 cnt += 1
#                 visited[n][m] = 1

# =========
# bfs / 시간 메모리 이슈로 인해 pypy 제출 필요.

import collections

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = collections.deque()
day = 0
check = False


def bfs(a, b):
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif graph[nx][ny] == 0:
                    count[x][y] += 1
    return 1


while True:
    visited = [[False]*m for _ in range(n)]
    count = [[0]*m for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i, j))

    for i in range(n):
        for j in range(m):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    if len(result) == 0:
        break
    if len(result) >= 2:
        check = True
        break
    day += 1

if check:
    print(day)
else:
    print(0)
