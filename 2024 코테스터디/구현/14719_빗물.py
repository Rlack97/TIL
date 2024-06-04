# import sys
# input = sys.stdin.readline

# H, W = map(int, input().split())
# world = list(map(int, input().split()))


# # 왼쪽에서 오른쪽으로 탐사
# # 자신보다 낮은 칸이 나오면 높이를 저장해두고 기록 시작

# # 물이 고이는 규칙
# # 1.시작지점 = 다음칸에 자신보다 낮은 값이 나오는 곳
# # 2.시작지점과 같거나 높은 기둥이 나오면 끝남. 또는 배열의 끝부분.
# # 3. 양 끝 지점 중 낮은 쪽을 기준으로 물 양이 계산됨

# # * 배열의 끝 값이 0이라면 해당 부분은 물이 고이지 않음

# start = 0
# end = 0
# pos = []
# total_water = 0


# def get_water(start, end, emp):
#     value = 0
#     stan = min(start, end)
#     for liq in emp:
#         value += stan - liq
#         # 기준점을 뺀만큼의 값이 고인다
#     return value


# for w in range(W):
#     # 이전보다 값이 낮아짐  = 물이 고일 수 있음
#     # 기준값은 아직 모르므로 값만 저장해두자
#     if world[w] < start:
#         if w == W-1 and pos:  # 그런데 리스트 마지막이다?
#             # pos에 저장된 값들 중 현위치보다 낮은 값들에는 물이 고인다
#             total_water += get_water(start, world[w], pos)
#         pos.append(world[w])
#         continue

#     elif world[w] >= start:  # 기준점과 같거나 높은 값이 나왔을 때
#         if pos:  # 물이 고이는 배열이 존재한다면
#             total_water += get_water(start, world[w], pos)
#             # 시작점 초기화
#             start = world[w]
#             # 리스트 초기화
#             pos = []
#         else:
#             start = world[w]

# print(total_water)


import sys
input = sys.stdin.readline

H, W = map(int, input().split())
world = list(map(int, input().split()))

total_water = 0

# 왼쪽에서 오른쪽으로 탐사
for w in range(1, W - 1):  # 첫 칸과 마지막 칸은 고려하지 않음
    left_max = max(world[:w])  # 현재 위치의 왼쪽 최대 높이
    right_max = max(world[w + 1:])  # 현재 위치의 오른쪽 최대 높이

    # 현재 위치가 좁은 골짜기라면 물이 고일 수 있음
    if world[w] < left_max and world[w] < right_max:
        # 좌우 최대 높이 중 작은 것을 기준으로 물이 고일 수 있는 양을 계산
        min_height = min(left_max, right_max)
        total_water += max(0, min_height - world[w])

print(total_water)
