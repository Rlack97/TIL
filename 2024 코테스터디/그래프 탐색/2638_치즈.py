import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(start_points, visited, board, n, m):
    queue = deque(start_points)

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if board[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    # visited = 외부공기 여부
    return visited


def melt_cheese(board, visited, n, m):
    cheese_to_melt = []

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                air_count = 0
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                        air_count += 1
                if air_count >= 2:
                    cheese_to_melt.append((i, j))
    for x, y in cheese_to_melt:
        board[x][y] = 0
    return len(cheese_to_melt) > 0


time = 0
while True:
    visited = [[False] * m for _ in range(n)]
    visited = bfs([(0, 0)], visited, board, n, m)
    if not melt_cheese(board, visited, n, m):
        break
    time += 1

print(time)
