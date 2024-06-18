import sys
input = sys.stdin.readline

# 산성 = 양수
# 알칼리 = 음수
# 두 개를 합쳐서 특성값이 0에 가까운 용액을 만들어라
# 오름차순으로 입력됨
N = int(input())
liquids = list(map(int,input().split()))

# 포인터
alcal = 0
acid = N-1

# 정답 기록용 변수
answer = abs(liquids[alcal] + liquids[acid])
left = alcal
right = acid

# 포인터 위치 : 알칼리<산성
while alcal < acid:

  # 현 포인터 위치간 합
  tmp = liquids[alcal] + liquids[acid]

  # 기록보다 작은 값이 나왔을 때 기록
  if abs(tmp) < answer:
    left = alcal
    right = acid
    answer = abs(tmp)
    
    if answer == 0:
      break
  
  # 합이 음수면 왼쪽 포인터 진행 (음수값이 작아짐)
  if tmp < 0:
    alcal += 1
  
  # 양수면 오른쪽 포인터 진행 (양수값이 작아짐)
  else:
    acid -= 1

print(liquids[left], liquids[right])
