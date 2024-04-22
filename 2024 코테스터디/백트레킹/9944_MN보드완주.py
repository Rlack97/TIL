import sys
input = sys.stdin.readline

# 탐색 종료 검증


def check():
    for i in range(N):
        for j in range(M):
            if board[i][j] == ".":
                return False
    return True


def bfs(x, y, cnt):
    global minimum
    if check():  # 모든 좌표를 탐색한 경우
        minimum = min(minimum, cnt)

    if cnt < minimum:  # 현재까지 탐색한 경로의 수가 answer보다 작을 경우만 탐색
        for i in range(4):
            tmp = []  # 지나온 좌표를 담을 배열
            ax = x
            ay = y
            while True:
                ax += dx[i]
                ay += dy[i]
                # 장애물, 보드의 경계, 이미 공이 지나갔던 칸이 아니라면
                if 0 <= ax < N and 0 <= ay < M and board[ax][ay] == ".":
                    tmp.append([ax, ay])
                    board[ax][ay] = "*"
                else:
                    break
            if tmp:
                bfs(ax-dx[i], ay-dy[i], cnt+1)

            for a, b in tmp:
                board[a][b] = "."
        board[x][y] = "."


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

case = 1
while True:
    try:
        N, M = map(int, input().split())
        board = [list(input().strip()) for _ in range(N)]
        minimum = 1000000
        for n in range(N):
            for m in range(M):
                if board[n][m] == '.':
                    board[n][m] = '*'
                    bfs(n, m, 0)

        if minimum == 1000000:
            minimum = -1
        print("Case {}: {}".format(case, minimum))
        case += 1
    except:
        break
