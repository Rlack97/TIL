# 240307
# 백트래킹, 2차원좌표
import sys
input = sys.stdin.readline

# 상하좌우 탐색을 위한 좌표그래프
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def play(turn):
    global mincnt, minturn
    pin = []
    for i in range(5):
        for j in range(9):
            if board[i][j] == 'o':
                pin.append((j, i))
    # 순환하면서 핀 위치 기록

    # 최소갯수보다 더 적다면 턴과 핀 갯수를 기록
    if len(pin) < mincnt:
        minturn = turn
        mincnt = len(pin)

    for x, y in pin:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 뛰어넘은 다음 칸을 고려
            if -1 < nx+dx[i] < 9 and -1 < ny+dy[i] < 5:
                if board[ny][nx] == 'o' and board[ny+dy[i]][nx+dx[i]] == '.':
                    board[ny][nx] = '.'
                    board[ny+dy[i]][nx+dx[i]] = 'o'
                    board[y][x] = '.'
                    play(turn+1)  # 턴 진행
                    # 다른 경우도 살펴보기 위해 핀을 제거 이전상태로 되돌려준다.
                    board[ny][nx] = 'o'
                    board[ny+dy[i]][nx+dx[i]] = '.'
                    board[y][x] = 'o'


N = int(input())
for _ in range(N):
    mincnt = 10
    minturn = 10
    board = [list(input().rstrip()) for i in range(5)]
    input()
    play(0)
    print(mincnt, minturn)
