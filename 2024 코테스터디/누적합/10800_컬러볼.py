# 0316

# import sys
# input = sys.stdin.readline
# N = int(input())

# color = [0] * (N)
# size = [0] * (N)
# can_eat = [0] * (N)

# for i in range(N):
#     C, S = map(int, input().split())
#     color[i] = C
#     size[i] = S
#     for j in range(i):
#         # 색이 다르고
#         if C != color[j]:
#             # 어느 한쪽이 더 크면 해당 번호의 공의 값으로 추가
#             if S < size[j]:
#                 can_eat[j] += S
#             if S > size[j]:
#                 can_eat[i] += size[j]


# for value in can_eat:
#     print(value)

# 2중 for 문이라서 시간초과

# ************************************************#

import sys
input = sys.stdin.readline
N = int(input())

balls = [0] * N

for i in range(N):
    C, S = map(int, input().split())
    # 크기, 색, 번호를 저장
    balls[i] = (S, C, i)

# 크기순 오름차순 정렬
balls.sort()
s = 0
j = 0
colors = [0] * (N+1)
answer = [0] * N

for i in range(N):
    a = balls[i]
    b = balls[j]

    # 현재 값(a)보다 작은 모든 공들
    while b[0] < a[0]:
        s += b[0]

        # 색상값의 인덱스에 해당 색상의 값을 저장
        colors[b[1]] += b[0]

        # 다음 공을 확인하기 위한 값 증가
        j += 1
        b = balls[j]

    # 자신보다 작은 공들의 값의 합 - 같은 색의 공들 값의 합
    answer[a[2]] = s-colors[a[1]]

for value in answer:
    print(value)
