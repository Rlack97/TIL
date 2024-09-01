import sys
import copy
input =sys.stdin.readline

L = int(input())
N = int(input())
rotate = []

for _ in range(N):
  R, D = map(str,input().split())
  R = int(R)
  rotate.append((R,D))
# R초 뒤에 D 방향으로 회전한다
# 범위 밖으로 나가거나 자기 몸에 부딪히면 죽음
# 시작은 0,0 즉 board[L][L]에서 오른쪽으로 시작
# 몸을 늘린 후에 회전, 회전에는 시간이 소요되지 않음

snake = [[0,0]]
# 뱀 몸 저장소. 새 칸으로 나아갈 때마다 중복 확인 + 기록
# 방향을 저장. 1 = 오른쪽, 2 = 아래, 3 = 왼쪽, 4 = 위쪽
d = 1
# 변동시간, 최종시간을 기록
t = 0 
# 회전정보를 볼 포인터
p = 0

while True:
  head = copy.deepcopy(snake[-1])
  t += 1

  if d == 1:
    head[0] += 1
    if head[0] > L or head in snake:
      print(head)
      print(snake)
      break
    else:
      snake.append(head)
  elif d == 2:
    head[1] -= 1
    if head[1] < -L or head in snake:
      break
    else:
      snake.append(head)
  elif d == 3:
    head[0] -= 1
    if head[0] < -L or head in snake:
      break
    else:
      snake.append(head)
  else:
    head[1] += 1
    if head[1] > L or head in snake:
      break
    else:
      snake.append(head)
  
  if t == rotate[p][0]:
    if rotate[p][1] == 'R':
      d = (d % 4) + 1
    else:
      # 빼기 모듈러 연산. 이건 생각해내기 좀 어려울 듯?
      d = (d - 2) % 4 + 1
    t = 0
    p += 1 


print(len(snake))


# 시간초과라 이거지...? 
# 점이 아닌 선을 기준으로 풀이해야 함

import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
L = int(input())
N = int(input())
MAX = L*2+1

next_dir = { 'L' : 1, 'R' : -1, 'S' : 0 }

rotate_list = [input().split() for _ in range(N)]
rotate_list.append((MAX, 'S'))
line_list = [(-L-1, -L-1, L+1, -L-1, 0),
            (-L-1, L+1, L+1, L+1, 0),
            (-L-1, -L-1, -L-1, L+1, 1),
            (L+1, -L-1, L+1, L+1, 1)]

def find_crash(x, y, ax, ay, r) :
  _line_list = line_list if len(line_list) == 4 else line_list[1:]
  result = MAX
  for idx, (sx, sy, ex, ey, dir) in enumerate(_line_list) :
    if r % 2 == dir % 2:
      if x == ax == sx :
        min_y, max_y = min(sy, ey), max(sy, ey)
        if min_y <= ay <= max_y or min(y, ay) <= min_y < max(y, ay):
          dist = min_y - y if y < ay else y - max_y
          result = min(result, dist)
      elif y == ay == sy :
        min_x, max_x = min(sx, ex), max(sx, ex)
        if min_x <= ax <= max_x or min(x, ax) <= min_x <= max(x, ax):
          dist = min_x - x if x < ax else x - max_x
          result = min(result, dist)
    else :
      if sx == ex :
        min_x, max_x = min(x, ax), max(x, ax)
        min_y, max_y = min(sy, ey), max(sy, ey)
        if min_x <= sx <= max_x and min_y <= y <= max_y :
          result = min(result, abs(x - sx))
      elif sy == ey :
        min_y, max_y = min(y, ay), max(y, ay)
        min_x, max_x = min(sx, ex), max(sx, ex)
        if min_y <= sy <= max_y and min_x <= x <= max_x :
          result = min(result, abs(y - sy))
          
  return result if result < MAX else 0
    
def solve() :
  cnt = 0
  x, y, r = 0, 0, 0
  for t, dir in rotate_list :
    t = int(t)
    ax, ay = x + dx[r]*t, y + dy[r]*t
    is_crash = find_crash(x, y, ax, ay, r)

    if is_crash :
      cnt += is_crash
      return cnt
    
    cnt += t
    line_list.insert(0, (x, y, ax, ay, r))
    x, y, r = ax, ay, ( r + next_dir[dir] ) % 4

  return cnt

print(solve())
