import sys
input = sys.stdin.readline

n, E, W, S, N = map(int, input().split())

# N 번 임의대로 움직일 때, 단순한(같은 곳을 두번이상 방문하지 않은) 경로의 확률

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
percents = [E, W, S, N]

# (N,N이 한가운데인 그래프 생성)

board = [[0]*(2*n+1) for _ in range(2*n+1)]

answer = 0


def dfs(x, y, percent, cnt):
    global answer
    # 이동횟수를 다 채웠을 때의 확률끼리 더해준다
    if cnt == n:
        answer += percent
        return

    now_percent = percent
    board[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        # 보드 범위 이내
        if 0 <= nx < (2*n+1) and 0 <= ny < (2*n+1):
            # 이미 방문했다면 계속
            if board[nx][ny] == 1:
                continue

            # 방문 안했으면 DFS재귀
            else:
                # 지금까지의 확률 * 해당 방향으로 이동했을 확률
                dfs(nx, ny, now_percent*(percents[i]/100), cnt+1)
                # 방문처리 해제
                board[nx][ny] = 0


dfs(n, n, 1, 0)

print(answer)
