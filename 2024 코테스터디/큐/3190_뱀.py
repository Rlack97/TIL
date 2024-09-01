import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
apples = [tuple(map(int,input().split()))for _ in range(K)]
L = int(input())
move_info = [list(map(str,input().split()))for _ in range(L)]

snake = deque([(1,1)])

t = 0
# 맨 처음엔(1,1)칸에서 오른쪽으로 움직임
# 동, 북, 서, 남
dx = [1,0,-1,0]
dy = [0,-1,0,1]
d = 0

def loop():
    global t
    (heady,headx) = snake[0]
    next = (heady + dy[d], headx + dx[d])


    # 보드 범위를 벗어나거나 자기 몸이랑 부딛히면 강제종료
    # 0,0 보드가 아닌 1,1이 시작지점인 보드이므로 N+1에 도달하면 범위를 벗어남
    if headx < 1 or headx > N or heady < 1 or heady > N:
      print(t)
      exit()
    elif next in snake:
      print(t+1)
      exit()


    if next in apples:
      # 사과를 먹고 길이가 늘어났으므로 꼬리는 그대로
      snake.appendleft(next)
      # 사과를 먹었으므로 사과 삭제!!!!!! 생각도 못했다
      apples.remove(next)
    else:
      # 늘어나지 않았으므로 꼬리를 빼고 다음 칸으로 이동
      snake.pop() 
      snake.appendleft(next)
    
    # 시간 증가
    t += 1


for m in move_info:
  time, direction = int(m[0]), m[1]
  # 방향전환 하기 전까지 전진
  while t < time:
    loop()
  
  # 전진 종료, 방향전환
  if direction == 'L':
    d = (d+1) % 4
  else:
    d = (d+3) % 4

# 방향전환이 완료된 후에도 게임이 끝나지 않은경우를 위한 코드
while True:
  loop()
  
  