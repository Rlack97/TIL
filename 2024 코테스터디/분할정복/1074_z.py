import sys
input = sys.stdin.readline

N,r,c = map(int,input().split())
answer = 0

def DQ(size,x,y):
  global answer 
  if x == r and y == c:
    print(answer)
    exit()

  # 분할하여 사이즈가 1이 되었을 때
  if size == 1:
    answer += 1
    return
  
  # 백트레킹
  # 시작위치 x,y와 내부 사각형 크기 size만큼의 범위에서 목표값이 없으면
  # 사각형 크기 값만큼 바로 정답에 더해줌
  if not (x <= r < x+size and y <= c < y+size):
    answer += size * size
    return
  
    # 분할
  nbs = size//2
  # 1
  DQ(nbs, x, y)
  # 2
  DQ(nbs, x, y+nbs)
  # 3
  DQ(nbs, x+nbs, y)
  # 4
  DQ(nbs, x+nbs, y+nbs)


DQ(2**N,0,0)