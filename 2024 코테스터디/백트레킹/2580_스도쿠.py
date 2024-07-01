import sys

def check_row(i,n):
  for j in range(9):
    if n == board[i][j]:
      return False
  return True

def check_col(j,n):
  for i in range(9):
    if n == board[i][j]:
      return False
  return True

def check_sqr(a,b,n):
  for i in range(3):
    for j in range(3):
      # 스도쿠 영역 나누기:
      # x,y좌표가 어느 위치의 사각형인가?
      # x // 3 * 3 + 1~3
      # 3으로 나눈 나머지 * 3 = 0,3,6이므로 각각 사각형의 시작위치
      # +1~3으로 해당 사각형 내부 영역을 탐색 가능
      if n == board[a//3 * 3 +i][b//3*3+j]:
        return False
  return True

def find(n):
  if len(required) == n:
    for i in board:
      # 리스트 내부 요소들을 띄어쓰기 하나로 풀어서 출력
      print(*i)
    exit()
  
  a = required[n][0]
  b = required[n][1]
  for i in range(1,10):
    
    if check_col(b,i) and check_row(a,i) and check_sqr(a,b,i):
      board[a][b] = i
      find(n+1)
      board[a][b] = 0

input = sys.stdin.readline
board = [list(map(int,input().split()))for _ in range(9)]
required = []
for i in range(9):
  for j in range(9):
    if board[i][j] == 0:
      required.append((i,j))

find(0)