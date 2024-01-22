#2024-01-22
# stack 문제

N = int(input()) # 탑의 개수
top_list = list(map(int,input().split())) # 탑 높이 리스트

# 각각의 탑이 발송한 신호를 수신한 탑의 위치를 기록. 없으면 0
# 즉, '앞에서 나온 자신보다 큰 값 중 자신과 가장 가까운 값의 index값'

stack = [] # 스택 리스트. [index값, 탑의 높이 값] 형태로 기록.
answer = [] # 정답 리스트

for i in range(N):
  # 스택이 있는 경우
  # 자신 앞에 타워가 있음
  while stack: 
    # 가장 최근의 스택의 값이 현재 타워의 값보다 큰 경우
    # 정답 리스트에 해당 타워의 index값을 입력 (+1을 보정해주어야 함)
    # 이후 반복문 탈출
    if stack[-1][1] > top_list[i]: 
      answer.append(stack[-1][0]+1)
      break
    
    # 현재 타워의 값이 더 큰 경우
    # 최근 기록을 스택에서 제거 후 while 반복
    else:
      stack.pop()
  
  # 스택이 비어 있는 경우
  # 앞에 자신보다 큰 타워가 없는 상황이므로 0 기록
  if not stack:
    answer.append(0)
  
  # 해당 타워의 정보를 스택에 저장
  stack.append([i,top_list[i]])

# 정답 리스트 출력
print(" ".join(map(str, answer)))
  