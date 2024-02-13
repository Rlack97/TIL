# 240212
# DP
import sys
input = sys.stdin.readline
N = int(input())
houses = [list(map(int, input().split())) for _ in range(N)]
result = I = 1e9

# 첫 번째 집의 색이 3가지가 가능하므로 3번 순환
for i in range(3):
    dp = [[I, I, I] for _ in range(N)]
    dp[0][i] = houses[0][i]

    # 이후의 집들을 각각 R,G,B로 색칠했을 때의 최소값을 계산하며 기록
    # 첫번째와 N번째를 제외하고는 앞뒤로만 색이 다르면 되므로,
    # dp[j-1][다른색1] 과 dp[j-1][다른색2] 중 작은 값을 구해 더한다.
    for j in range(1, N):
        dp[j][0] = houses[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = houses[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = houses[j][2] + min(dp[j-1][0], dp[j-1][1])

    # 이렇게 되면 dp의 마지막 값은 마지막 집을 R,G,B로 칠하는 경우마다
    # 각각의 최소비용이 계산되어 저장된다.
    for c in range(3):
        # 첫 번째 집의 색(i)와 다른 값만 사용해서 최솟값을 계산한다.
        if i != c:
            result = min(result, dp[-1][c])

print(result)
