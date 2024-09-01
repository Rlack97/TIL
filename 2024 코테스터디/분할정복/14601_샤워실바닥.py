import sys

input = sys.stdin.readline


def check(i, j, l):
    for r in range(i, i + l):
        for c in range(j, j + l):
            if board[r][c]:
                return 0
    return 1


# 재귀함수
def tile(i, j, l):
    global label
    label += 1

    if check(i, j, l):
        board[i + l - 1][j + l - 1] = label
    if check(i, j + l, l):
        board[i + l - 1][j + l] = label
    if check(i + l, j, l):
        board[i + l][j + l - 1] = label
    if check(i + l, j + l, l):
        board[i + l][j + l] = label

    if l == 1:
        return

    nl = l // 2
    tile(i, j, nl)
    tile(i, j + l, nl)
    tile(i + l, j, nl)
    tile(i + l, j + l, nl)


K = int(input())
N = 2**K

x, y = map(int, input().split())

board = [[0] * N for _ in range(N)]
board[N - y][x - 1] = -1

label = 0

tile(0, 0, N // 2)

for b in board:
    print(*b)
