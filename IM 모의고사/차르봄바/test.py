import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, P = map(int, input().split())
    virus = [list(map(int, input().split())) for _ in range(N)]
    max_terminated = 0

    for i in range(N):
        for j in range(N):
            # 1. 가로 세로 범위
            summed = 0
            for k in range(1, P+1):
                if i + k < N:
                    summed += virus[i + k][j]
                if j + k < N:
                    summed += virus[i][j + k]
                if i - k >= 0:
                    summed += virus[i - k][j]
                if j - k >= 0:
                    summed += virus[i][j - k]
            summed += virus[i][j]

            if summed > max_terminated:
                max_terminated = summed

            # 2. 대각선 범위
            cross_sum = 0
            for t in range(1, P+1):
                if i + t < N and j + t < N:
                    cross_sum += virus[i + t][j + t]
                if i + t < N and j - t >= 0:
                    cross_sum += virus[i + t][j - t]
                if i - t >= 0 and j - t >= 0:
                    cross_sum += virus[i - t][j - t]
                if i - t >= 0 and j + t < N:
                    cross_sum += virus[i - t][j + t]
            cross_sum += virus[i][j]

            if cross_sum > max_terminated:
                max_terminated = cross_sum

    print('#'+str(tc)+' '+str(max_terminated))
