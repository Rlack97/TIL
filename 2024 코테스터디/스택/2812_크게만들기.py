import sys
input = sys.stdin.readline

# N자리 숫자에서 K개를 지워서 얻을 수 있는 가장 큰 수

N, K = map(int,input().split())
number =  input().strip()

cnt = K
stack = []

for n in number:
  # 숫자를 지우는 조건
  # 1. 지울 수 있는 횟수가 남아있고
  # 2. 지울 숫자가 스택에 쌓여 있으며
  # 3. 스택 맨 마지막 자릿수보다 삽입하려는 값이 클 때

  # 즉, 큰 값이 나오면 그 값보다 작은 스택 앞의 값들을 지우면서
  # 지운 수를 기록
  while cnt > 0 and stack and stack[-1] < n:
    stack.pop()
    cnt -= 1

  # 스택에 숫자 기록
  stack.append(n)

answer = stack[:N-K]
print(''.join(answer))