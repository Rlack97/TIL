# 240210
# DFS 재귀
import sys
input = sys.stdin.readline

# 입력받기
R, C = map(int, input().split())
board = [list(str(input().rstrip())) for _ in range(R)]

max_cnt = 0
words = set(board[0][0])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def DFS(x, y, cnt):
    global max_cnt

    # 횟수 최대치 갱신
    max_cnt = max(cnt, max_cnt)

    # 조건에 맞춰 상하좌우로 이동
    # (리스트 범위 내인가? + 없는 알파벳인가?)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not board[nx][ny] in words:
            words.add(board[nx][ny])
            DFS(nx, ny, cnt+1)
            words.remove(board[nx][ny])


DFS(0, 0, 1)
print(max_cnt)
