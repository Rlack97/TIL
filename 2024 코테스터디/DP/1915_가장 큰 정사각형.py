import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        # 첫 행, 첫 열은 그대로 옮김
        if i == 0 or j == 0:
            dp[i][j] = board[i][j]
        
        # 값이 0이면 그대로 옮김
        elif board[i][j] == 0:
            dp[i][j] = 0

        # 왼쪽, 위쪽, 대각선 세 개 값 중 가장 작은 값 +1
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        
        #최댓값 (정사각형 크기) 갱신
        answer = max(dp[i][j], answer)

# 넓이 출력
print(answer * answer)