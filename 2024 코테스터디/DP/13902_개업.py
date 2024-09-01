import sys
input = sys.stdin.readline

N,M = map(int,input().split())
woks = list(map(int,input().split()))

# 최소 몇 번을 요리해야 하는가? (한 번에 동시에 2개 사용가능)
# 동전 문제와 크게 다르지 않나?
# (동전가격/웍 크기)만큼 작은 dp + 1 과 현위치 값 중 가장 작은 것.

# 동시에 2개를 사용할 수 있으므로 가능한 웍 사이즈를 별도 리스트로 저장
wok_pos = set(woks)
for i in range(M):
  for j in range(i+1,M):
    wok_pos.add(woks[i] + woks[j])


# dp[x] = 짜장면 x개를 위해 요리해야 하는 횟수
dp = [1e9] * (10001)
dp[0] = 0

for i in range(N):
  for k in wok_pos:
    if i + k > 10000:
      continue
    # i에서 k 값만큼 추가한 경우, i까지 가는 법 + 1과 자신과의 값을 비교
    dp[i+k] = min(dp[i] + 1, dp[i + k])

print(dp[N] if dp[N]!=1e9 else -1)
