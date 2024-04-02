# import sys
# from collections import deque
# input = sys.stdin.readline

# L = int(input())
# Ml, Mk = map(int, input().split())
# C = int(input())
# # zombies = [int(input()) for l in range(L)]
# zombies = deque()
# for l in range(L):
#     zombies.append(int(input()))

# while True:
#     # deque 내부 값에 0 이상인 값이 없다면 생존
#     if all(zom <= 0 for zom in zombies):
#         print('YES')
#         break
#     # 바로 앞에 좀비가 있고, 살상력보다 높은 체력이 있다면 지뢰 사용
#     if zombies[0] > Mk and C > 0:
#         C -= 1
#         zombies[0] = 0

#     # 아니라면 기관총 사용
#     else:
#         zombies = deque([num - Mk for num in list(zombies)
#                         [:Ml]] + list(zombies)[Ml:])

#     # 모든 좀비 한 칸 전진 (popleft())
#     next = zombies.popleft()
#     if next > 0:
#         print('NO')
#         break
#       # pop 한 값이 0 이상이라면 사망

# 시간초과

from collections import deque
import sys

input = sys.stdin.readline
L = int(input())						# 기관총 진지 앞쪽의 길이
ML, MK = map(int, input().split())		# 기관총의 유효 사거리 ML, 기관총의 1m당 살상력 MK
C = int(input())						# 수평 세열 지향성 지뢰의 개수


def solution(C):

    attack = [0]  # 누적합
    flag = False

    for idx in range(1, L+1):
        zombie = int(input())   # 좀비

        if flag:
            continue

        ml = max(0, idx - ML)
        damage = attack[idx-1] - attack[ml]

        if zombie <= damage + MK:
            attack.append(attack[idx-1] + MK)
        else:
            if C > 0:
                C -= 1
                attack.append(attack[idx-1])
            else:
                flag = True

    if flag:
        return "NO"
    else:
        return "YES"


print(solution(C))
