import sys

input = sys.stdin.readline

N = int(input())
sequence = list(map(int, input().split()))

prev = [-1] * N
dp = [1] * N

# 두 번째 요소부터 살펴본다
for i in range(1, N):
    for j in range(i):
        # j값(앞부분)에 비해 i값 (뒷부분)이 증가했다면
        # 리스트의 길이 증가
        if sequence[i] > sequence[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j  # 앞부분 원소를 기록

answer = max(dp)
last_idx = dp.index(answer)

answer_list = []
while last_idx != -1:
    answer_list.append(sequence[last_idx])
    last_idx = prev[last_idx]

print(max(dp))
print(*answer_list[::-1])
