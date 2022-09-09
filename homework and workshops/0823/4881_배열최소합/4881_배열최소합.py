# 4881_배열최소합 풀이
# 2022-08-23

import sys
sys.stdin = open('input.txt', 'r')


def one_sum(i, n_sum):
    global ruler

    if n_sum > ruler:
        return

    if i == N:
        if n_sum < ruler:
            ruler = n_sum
            return

    for col in range(N):
        if not bit[col]:
            bit[col] = 1
            one_sum(i+1, n_sum + mapping[i][col])
            bit[col] = 0




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mapping = [list(map(int, input().split())) for _ in range(N)]
    ruler = 100000

    bit = [0]*N
    one_sum(0,0)

    print('#{} {}'.format(tc, ruler))

