#240304

import sys
input = sys.stdin.readline

N = int(input())

skyline = []
building = 0

for _ in range(N):
  x,y = map(int,input().split())
  skyline.append(y)
skyline.append(0)

stack = [0]
# 높이 기록과는 별도의 stack. 
# 비어있지 않아야 하므로 0을 넣어둬야 한다.

for s in skyline:
  past = s
  # 이전 건물 기록

  while stack[-1] > s:
    #건물 높이가 낮아졌을때
    if stack[-1] != past:
      # 이전 건물 기록과 같지 않다면
      building += 1
      # 빌딩 추가
      past = stack[-1]
      # 추가된 빌딩의 높이 기록
    stack.pop()
    # 추가된 빌딩의 기록 삭제

  stack.append(s)


print(building)
