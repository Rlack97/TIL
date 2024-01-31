# 2169 240129
# DP


import sys

N, M = map(int, sys.stdin.readline().split())

dp = []

for _ in range(N):
    dp.append(list(map(int, sys.stdin.readline().split())))
# 첫 번째 줄에서는 오른쪽으로만 이동할 수 있으므로
# 값을 더해주면 해당 경로까지의 최댓값이 된다

for j in range(1, M):
    dp[0][j] += dp[0][j-1]

# 이후 두 번째 줄부터는 오른쪽으로 진행한 값과
# 왼쪽으로 진행한 값을 비교하는 것으로 최댓값을 알 수 있음.
for i in range(1, N):
    # 값을 적어둘 임시배열 생성 (비참조 배열복사)
    left_to_right = dp[i][:]
    right_to_left = dp[i][:]

    # 왼쪽에서 오른쪽으로 가는 경우
    for j in range(M):
        # 첫 칸의 값은 위에서 내려오는 경우밖에 없음
        if (j == 0):
            left_to_right[j] += dp[i-1][j]
        # 위에서 내려오는 값과 왼쪽에서 오는 값 중 큰 값으로 진행
        else:
            left_to_right[j] += max(dp[i-1][j], left_to_right[j-1])

    # 오른쪽에서 왼쪽으로 가는 경우
    # 거꾸로 한칸식 가야하므로 두, 세번째 인자로 -1을 넣어준다
    for j in range(M-1, -1, -1):

        # 마지막 칸에서는 위에서밖에 내려올 수 없다.
        if (j == M-1):
            right_to_left[j] += dp[i-1][j]
        else:
            right_to_left[j] += max(dp[i-1][j], right_to_left[j+1])

    # 두 배열을 비교해, 각 좌표값을 최대로 업데이트
    for j in range(M):
        dp[i][j] = max(left_to_right[j], right_to_left[j])


print(dp[N-1][M-1])
