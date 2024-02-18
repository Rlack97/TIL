# 240216
# 구현
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(visited):
    global ans

    queue = deque([[0, 0]])
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위체크
            if ny < 0 or ny >= w + 2 or nx < 0 or nx >= h + 2 or building[nx][ny] == '*' or visited[nx][ny] == True:
                continue

            # 문
            if 'A' <= building[nx][ny] <= 'Z':
                if building[nx][ny].lower() not in keys:
                    continue

            # 키
            elif 'a' <= building[nx][ny] <= 'z':
                if building[nx][ny] not in keys:
                    keys.update(building[nx][ny])
                    visited = [[False] * (w+2) for _ in range(h+2)]
            # 문서
            elif building[nx][ny] == '$' and (nx, ny) not in get_doc:
                ans += 1
                get_doc.append((nx, ny))

            visited[nx][ny] = True
            queue.append([nx, ny])


T = int(input())
for t in range(T):
    h, w = map(int, input().split())
    building = ['.' + input()+'.' for _ in range(h)]
    building = ['.' * (w+2)] + building + ['.' * (w+2)]
    visited = [[False] * (w+2) for _ in range(h+2)]
    keys = set(input().rstrip())
    get_doc = []
    ans = 0
    bfs(visited)
    print(ans)
