# 0311
# dp?

import sys
input = sys.stdin.readline

N = int(input()) # 30이하
weights = list(map(int,input().split()))
num = int(input())
marbles = list(map(int,input().split()))

# 구슬의 무게를 확인하는 법
# 1. 추와 무게가 같거나
# 2. 추끼리 더한 값과 같거나
# 3. 추끼리 뺀 값과 같거나
# 추들로 확인할 수 있는 값의 리스트를 만들고
# 구슬의 무게가 그 안에 있는지 확인하면 됨.

dp = [0]

for w in weights:
    tmp = []
    for i in dp:
        tmp.append(i+w)
        tmp.append(abs(i-w))
        # dp에 기록된 모든 값에 추와의 합 / 차를 기록
    dp = list(set((dp + tmp)))
    # dp리스트 갱신

for m in marbles:
    print('Y' if m in dp else 'N', end=' ')

