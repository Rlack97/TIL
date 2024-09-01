from collections import deque
import sys

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y, dir):
    # 시작점을 큐에 삽입
    q.append([x, y, dir])
    # 방문리스트 기록
    visited[x][y][dir] = 1
    ans = []

    while q:
        x, y, dir = q.popleft()
        # 동일 방향으로 진행
        nx = x + dx[dir]
        ny = y + dy[dir]

        # 범위 조건 만족
        if 0 <= nx < n and 0 <= ny < n:
            
            # 방문하지 않았거나, 현재 경로로 갈 때 더 적은 거울을 사용하는 경우
            if not visited[nx][ny][dir] or visited[nx][ny][dir] > visited[x][y][dir]:
                # 벽이 아니라면
                if a[nx][ny] != '*':
                    
                    # 방문처리
                    visited[nx][ny][dir] = visited[x][y][dir]

                    # 문에 도달한 경우
                    if nx == fx and ny == fy:
                        # 사용한 거울 정보를 기록 
                        ans.append(visited[nx][ny][dir])
                        continue
                    
                    q.append([nx, ny, dir])

                    # 거울일 경우 별도 함수
                    if a[nx][ny] == '!':
                        turn(nx, ny, dir)

    print(min(ans)-1)

def turn(x, y, dir):
    # 반사 가능한 방향 두 개
    ndir = [(dir+1) % 4, (dir+3) % 4]
    # 각 방향에 대해서
    for d in ndir:
        # 방문하지 않았거나, 현재의 거울을 사용해도 더 적은 수의 거울일 때
        if not visited[x][y][d] or visited[x][y][d] > visited[x][y][dir] + 1:
            # 거울 사용 수 기록 (방문처리)
            visited[x][y][d] = visited[x][y][dir] + 1
            q.append([x, y, d])

n = int(input())
q = deque()
visited = [[[0]*4 for _ in range(n)] for _ in range(n)]

a, temp = [], []
for i in range(n):
    row = list(input().strip())
    a.append(row)
    for j in range(n):
        if row[j] == '#':
            temp.extend([i, j])
# 문 위치 기록
sx, sy, fx, fy = temp

for i in range(4):
    nx = sx + dx[i]
    ny = sy + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
        if a[nx][ny] != '*':
            dir = i
            break

bfs(sx, sy, dir)