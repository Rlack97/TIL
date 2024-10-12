import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
tasks = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)


for day in range(N - 1, -1, -1):  # 역순으로 순회
    if day + tasks[day][0] <= N:
        # 해당 작업을 할 수 있는 경우
        dp[day] = max(dp[day + 1], tasks[day][1] + dp[day + tasks[day][0]])
    else:
        # 해당 작업을 할 수 없는 경우
        dp[day] = dp[day + 1]

print(dp[0])
