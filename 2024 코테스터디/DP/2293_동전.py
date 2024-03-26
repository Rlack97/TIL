# 0325
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k+1)

dp[0] = 1
for c in coins:
    for i in range(k+1):
        # 목표치 k 이하의 값들 i
        if i-c >= 0:
            # 목표치에서 현재 코인값을 뺐을 때, 0이상이면
            dp[i] += dp[i-c]
            # 목표치 i의 경우의 수는 i-c의 경우의 수만큼 늘어난다

print(dp[k])
