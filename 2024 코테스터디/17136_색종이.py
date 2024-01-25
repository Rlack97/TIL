#17136 색종이 20240125
# 백트레킹/dfs
import sys

input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(10)]
papers = [0 for _ in range(5)]
result = 26

# 재귀함수
def dfs(x,y,cnt):
  global result

  # x가 10을 넘었을 때 최솟값 계산 후 반환
  if x >= 10:
    result = min(result,cnt)
    return
  
  # y가 10을 넘었을 때 다음 x축으로 이동
  if y >= 10:
    dfs(x+1,0,cnt)
    return
  
  # 방문한 칸에 1이 있을 경우
  if board[x][y] == 1:

    #각 사이즈별 종이에 대하여
    for k in range(5):
      # 해당 사이즈의 종이를 다 썼거나
      if papers[k] >= 5:
        continue
      
      # 종이를 사용했을 때 보드 밖으로 넘어가 버릴 경우는 제외
      if x+k < 0 or x+k >= 10 or y+k <0 or y+k>=10:
        continue
      
      # 플래그 설정
      ok=True

      # 사용할 종이 사이즈 내부를 순회하면서
      for cx in range(x,x+k+1):
        for cy in range(y,y+k+1):
          # 내부에 0이 있으면 플래그 비활성화 후 탈출
          if board[cx][cy] == 0:
            ok =False
            break
      
        # 플래그가 비활성화 되어있으면 탈출. 해당 사이즈의 색종이를 사용하지 못함.
        if not ok:
          break
      
      #플래그가 살아있다면 (=해당 사이즈의 종이를 사용할 수 있다면)
      #색종이로 덮은 부분을 0으로 치환
      if ok:
        for cx in range(x,x+k+1):
          for cy in range(y,y+k+1):
            board[cx][cy]=0

        # 용지 사용 기록 
        papers[k] += 1
        # 카운트를 늘린 후 재귀
        dfs(x,y+k+1,cnt+1)

        # 재귀에서 돌아왔을 경우 값 초기화 
        papers[k] -= 1

        # 색종이로 채운 곳을 다시 1로 표기
        for cx in range(x,x+k+1):
          for cy in range(y,y+k+1):
            board[cx][cy] = 1

  # 다음 칸으로 이동
  else:
    dfs(x,y+1,cnt)
    
# 함수 실행
dfs(0,0,0)

# 결과값이 26이면 모두 덮는 것이 불가능함.
if result == 26:
  result = -1

print(result)

