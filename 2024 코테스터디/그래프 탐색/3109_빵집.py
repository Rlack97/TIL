import sys
input = sys.stdin.readline


R, C = map(int, input().split())
map = [list(str(input().rstrip())) for _ in range(R)]

dx = [-1, 0, 1]
dy = 1

visited = [[0]*C for _ in range(R)]
route = 0


def DFS(x, y):
    global route
    if y == C-1:
        # 파이프 길이가 C, 즉 원웅이네 빵집까지 파이프가 연결되었다면
        route += 1
        return True

    for i in range(3):
        nx = x + dx[i]
        ny = y + 1
        # 다음 칸이 건물이거나 방문한 칸이 아니라면 진행
        if 0 <= nx < R and 0 <= ny < C and not map[nx][ny] == 'x' and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            if DFS(nx, ny):
                # 경로가 완성되었다면 끝
                return True


for i in range(R):
    DFS(i, 0)
print(route)
