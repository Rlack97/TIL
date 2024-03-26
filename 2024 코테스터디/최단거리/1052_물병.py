# 0326

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# 초기 물병 수를 이진수로 변환 -> 2^N승들의 합 = 전부 합했을 때의 물병들의 개수

count = 0

while bin(N).count('1') > K:
    N = N+1
    count = count + 1

print(count)
