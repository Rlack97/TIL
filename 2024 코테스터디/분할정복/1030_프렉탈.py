import sys
input = sys.stdin.readline

s, N, K, R1, R2, C1, C2 = map(int,input().split())
# 한 변의 길이
length = N ** s

def black_chk(i, point):
  x,y = point
  # 길이를 N으로 나눈 것 (검정칸)
  # ex) 27 // 3 = 9
  center = i // N
  
  # i, 즉 범위가 1이면 분할이 불가능하므로 흰색
  if i == 1:
    return 0
  
  # 가운데의 K 범위 안에 들어가있으면 검은색
  if center * (N-K)//2 <= x < center * (N+K)//2 and center * (N-K)//2 <= y < center * (N+K)//2:
        return 1

  # 한 변의 길이를 N으로 나눠서 재호출
  # x와 y도 해당 범위에 맞게 좌표가 변경
  x %= center
  y %= center

  return black_chk(i//N, [x,y])

# 주어진 출력범위가 검은색인지 아닌지 확인해서 바로 출력 (메모리)
for i in range(R1,R2+1):
    for j in range(C1,C2+1):
        print(black_chk(length,[i,j]), end="")
    print()