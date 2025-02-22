import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    lst = [0] + list(map(int, input().split()))

    # 누적합 리스트
    s_lst = [0 for _ in range(k + 1)]

    for i in range(1, k + 1):
        s_lst[i] = s_lst[i - 1] + lst[i]

    # 이중 dp
    dp = [[0 for i in range(k + 1)] for j in range(k + 1)]

    for i in range(2, k + 1):
        for j in range(1, k + 2 - i):
            dp[j][j + i - 1] = min(
                [dp[j][j + q] + dp[j + q + 1][j + i - 1] for q in range(i - 1)]
            ) + (s_lst[j + i - 1] - s_lst[j - 1])

    print(dp[1][k])
