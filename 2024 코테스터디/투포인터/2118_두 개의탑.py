# 240214
# 투 포인터
# Prifix Sum = 구간합 계산.
# 맨 앞에서부터 누적합을 전부 계산한 배열을 저장함.
# [L:R]구간의 구간합은 P[R]-p[L-1]임.
import sys
input = sys.stdin.readline

N = int(input())
distant = [int(input()) for _ in range(N)]

# 순환구조이기때문에 두 배의 길이 누적합을 구해둔다.
p_dist = [0] * (2*N+1)
for i in range(2*N):
    p_dist[i+1] = p_dist[i] + distant[i % N]

max_distance = 0
max_value, end = sum(distant), 1

# 각 시작지점에 대하여
for start in range(N):

    # 1. 끝나는 지점이 범위 이내에 있고
    # 2. 시계방향의 거리(값)이 반시계방향의 거리(값)보다 크면 ==> 왜???
    # 값을 기록 후 포인터를 이동시켜서 거리를 줄임
    while end < 2*N+1 and p_dist[end] - p_dist[start] <= max_value - p_dist[end] + p_dist[start]:
        max_distance = max(max_distance, p_dist[end]-p_dist[start])
        end += 1


print(max_distance)
