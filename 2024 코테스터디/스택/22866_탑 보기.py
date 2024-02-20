#240219

import sys
input = sys.stdin.readline

N = int(input())
height = list(map(int,input().split()))
# 시간초과. 이중 for문이라서 그런가 보다.
            
# highest = 0
# visible = []

# for n in range(N):
#   front_stack = []
#   back_stack = []
#   # 앞뒤로 탐색하면서 자신보다 높은 건물을 찾음.
#   # 스택에 저장해 둔 건물보다 낮은 건물이 나올 경우, 보이지 않음.
#   for i in range(n,0,-1):
#     if front_stack and height[i] <= front_stack[-1][0]:
#       continue

#     if height[n] < height[i]:
#       front_stack.append([height[i],i+1])
    

#   for i in range(n,N):
#     if back_stack and height[i] <= back_stack[-1][0]:
#       continue

#     if height[n] < height[i]:
#       back_stack.append([height[i],i+1])
  
#   if not front_stack and not back_stack:
#     visible.append(0)

#   else:
#     num = len(front_stack) + len(back_stack)
#     if len(front_stack) == 0:
#       close = back_stack.pop()[1]
#     elif len(back_stack) == 0:
#       close = front_stack.pop()[1]
#     else:
#       close = min(front_stack[0][1], back_stack[0][1])
#     visible.append([num,close])

# for v in visible:
#     print(*v) if isinstance(v, list) else print(v)


building_count = [0] * N
near_building = [1e9] * N

# 왼쪽 -> 오른쪽으로 탐색하면서 현재 빌딩보다 큰 빌딩을 담는다
left_stack = [] 
for i, h in enumerate(height):
  #자기 자신보다 낮은 빌딩 전부 제거 
  #이후의 탐색에서 i번째 빌딩에 가려져서 보이지 않는다
  while left_stack and height[left_stack[-1]] <= h:
    left_stack.pop()

  building_count[i] += len(left_stack)

  # 어차피 최대값을 저장해 두었으므로 그냥 할당만 하면 됨.
  if left_stack:
      near_building[i] = left_stack[-1]

  left_stack.append(i)


# 반대로도 하기
# N-1에서부터 0까지
right_stack = []
for i in range(N-1,-1,-1): 
  h = height[i]

  while right_stack and height[right_stack[-1]] <= h:
    right_stack.pop()

  building_count[i]+=len(right_stack)

  # 왼쪽 탐색값이 있다면 그것보다 작은지 확인,
  # 없다면 1e9보다 당연히 작으므로 값이 저장됨.
  if right_stack:
    if abs(i-right_stack[-1]) < abs(near_building[i]-i):
      near_building[i] = right_stack[-1]

  right_stack.append(i)

for i in range(N):
  if building_count[i]:
    print(building_count[i], near_building[i]+1)

  else:
    print(0)
