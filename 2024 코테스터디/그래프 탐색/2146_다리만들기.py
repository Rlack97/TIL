import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

# BFS 기반 이중리스트 탐색
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 표시

# 섬 구분을 위한 라벨링
def labeling(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    board[x][y] = label  # 처음 방문한 좌표에 라벨 부여

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                board[nx][ny] = label  # 인접한 좌표에 라벨 부여
                queue.append((nx, ny))
      
# 각 가장자리에서 BFS를 통해 다른 섬에 도달 시의 길이 기록
def shortest_bridge(v):
  q = deque()
  # 방문처리과 거리 기록을 동시에 함
  dist = [[-1]*N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      if board[i][j] == v:
        dist[i][j] = 0
        q.append((i,j))
        # 가장자리 구분 안해도 어차피 내륙은 걸러짐 

  while q:
    x,y = q.popleft()
    for dx,dy in directions:
      nx,ny = x+dx,y+dy
      if 0<=nx<N and 0<=ny<N:
        # 다른 섬과 만남
        if board[nx][ny] and board[nx][ny] != v:
          return dist[x][y]
        # 바다(0) 이면 거리 증가하면서 방문기록
        elif not board[nx][ny] and dist[nx][ny] == -1:
          dist[nx][ny] = dist[x][y]+1
          q.append((nx,ny))
  
  # 적절한 값이 없어도 min 비교를 위한 int반환
  return int(1e9)


visited = [[False] * N for _ in range(N)]
label = 1
answer = int(1e9)

for i in range(N):
  for j in range(N):
    if board[i][j] == 1 and not visited[i][j]:
      labeling(i,j)
      label += 1

for v in range(1,label):
  answer = min(answer, shortest_bridge(v))

print(answer)