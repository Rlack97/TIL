import sys
input = sys.stdin.readline

A = int(input())
numbers = list(map(int,input().split()))
dp = [1 for i in range(A)]
# dp[a] = 인덱스 a까지의 '가장 긴 감소하는 수열 길이'

for a in range(A):
  # 수열 내 숫자 numbers[a]에 대해
  for b in range(a):
    # 인덱스가 a보다 작은 숫자들을 탐색
    if numbers[b] > numbers[a]:
      # 숫자가 감소할 때 계산
      dp[a] = max(dp[a],dp[b+1])

print(max(dp))