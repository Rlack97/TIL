# 240131

import sys
from collections import deque

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
maps = [int(input()) for _ in range(n)]


def optimize():
    check = [0] * (d + 1)
    init = 0

    for i in range(0, k):
        num = maps[i]
        if check[num] == 0:
            init += 1
        check[num] += 1

    ans = init
    cnt = init

    for left in range(1, n):
        right = (left + k - 1) % n

        bef = maps[left - 1]
        aft = maps[right]

        check[bef] -= 1
        if check[bef] == 0:
            cnt -= 1

        check[aft] += 1
        if check[aft] == 1:
            cnt += 1

        if check[c] == 0:
            ans = max(ans, cnt + 1)
        else:
            ans = max(ans, cnt)

        if ans == k + 1:
            return ans

    return ans


print(optimize())
