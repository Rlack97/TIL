import sys
from collections import deque

input = sys.stdin.readline

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 4개 연속으로 붙어있는 것 찾기
def bfs(x, y, color):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    puyo = [(x, y)]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny]:
                # 지정해둔 색과 같은 색일 경우 큐에 더함
                # 큐에서 뽑아서 탐색을 진행해야 하므로 별도 리스트에도 저장
                if field[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    puyo.append((nx, ny))

    if len(puyo) >= 4:
        return puyo
    else:
        return []


# 낙하 과정
def drop_puyos():
    for j in range(6):
        empty = deque()
        # 아래에서부터 위로
        for i in range(11, -1, -1):
            # 빈칸을 기억
            if field[i][j] == ".":
                empty.append(i)

            # 뿌요를 위에서 만나고, 아래에 기억된 빈칸이 있을 경우
            elif field[i][j] != "." and empty:
                # 빈칸에 기억된 좌표 추출 후 두 곳의 값을 변경
                ni = empty.popleft()
                field[ni][j], field[i][j] = field[i][j], "."

                # 원래 뿌요가 있던 곳(위)가 빈칸이 됨
                empty.append(i)


field = [list(input().strip()) for _ in range(12)]
chain = 0

while True:
    # 방문 초기화
    visited = [[False] * 6 for _ in range(12)]
    to_pop = []

    for i in range(12):
        for j in range(6):
            if field[i][j] != "." and not visited[i][j]:
                result = bfs(i, j, field[i][j])
                if result:
                    to_pop.extend(result)

    if not to_pop:
        break

    for x, y in to_pop:
        field[x][y] = "."

    drop_puyos()
    chain += 1

print(chain)
