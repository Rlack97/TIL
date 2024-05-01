import sys
input = sys.stdin.readline

N = int(input())
male = list(map(int,input().split()))
female =  list(map(int,input().split()))

male.sort()
female.sort(reverse=True)

# 양수 = 자신보다 키가 큰 사람
# 음수 = 자신보다 키가 작은 사람

# 음수와 양수만 짝이 될 수 있고
# 음수의 절댓값이 더 커야 한다.
m, f = 0,0
answer = 0

while m < N and f < N: # 포인터가 범위 이내인 동안에 반복한다
  # 한쪽만 음수인 경우
  if male[m] * female[f] < 0 :
    if male[m] > 0 and male[m] < abs(female[f]):
      answer += 1
      m += 1
      f += 1
    elif male[m] < 0 and abs(male[m]) > female[f]:
      answer += 1
      m += 1  
      f += 1  
    # 양수 쪽 절댓값이 더 크면? 
    # 내림차순 기준 양수 쪽 포인터를 이동시킨다 (양수의 절댓값 저하)
    # 오름차순 기준 음수 쪽 포인터를 이동시킨다 (음수의 절댓값 저하)
    elif male[m] > 0 and male[m] >= abs(female[f]):
      f += 1
    elif male[m] < 0 and abs(male[m]) <= female[f]:
      f += 1
  else: 
    # 둘 다 음수거나 둘 다 양수라면?
    # 포인터를 진행시키면 반대가 되는 쪽을 진행시켜야..
    # 양수 -> 음수 (내림차순)
    # 음수 -> 양수 (오름차순)
    if male[m] > 0:
      f += 1
    else:
      m += 1

print(answer)
