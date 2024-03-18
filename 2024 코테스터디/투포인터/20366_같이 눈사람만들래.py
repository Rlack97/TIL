#0313

import sys
input = sys.stdin.readline

N = int(input())
radius = list(map(int,input().split()))
radius.sort()
# 눈덩이 2개로 만드는 눈사람 2개의 키 차이를 가장 줄일 수 있는 방법
answer = sys.maxsize

# 두 포인터 사이에서 4개를 골라서 최솟값을 갱신
for i in range(N):
  for j in range(i+3,N):
    left, right = i+1, j-1
    while left < right:
      # 크기순대로 정렬했으므로 포인터 범위 내 가장 작은 값+가장 큰 값을 사용해야 차이가 가장 적음.
      tmp = (radius[i]+radius[j]) - (radius[left]+radius[right])
      if abs(answer) > abs(tmp):
        answer = abs(tmp)
      if tmp < 0:
        # i+j값이 더 큰 경우
        # 오른쪽(큰값) 범위를 줄임
        right -=1
      else: 
        # 반대의 경우 왼쪽(작은값) 범위를 줄임
        left+=1
print(answer)