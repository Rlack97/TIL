import sys
from collections import Counter

input = sys.stdin.readline

# 입력 처리
N, K = map(int, input().split())
jumps = list(map(int, input().split()))
Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]

# jump 값의 빈도수를 계산 (Counter를 사용)
jump_counter = Counter(jumps)

# 배열 초기화
a = [0] * (N + 1)  # N+1 크기로 만들어 마지막 위치의 갱신을 쉽게 처리

# something 함수의 구현
for j, count in jump_counter.items():
    for i in range(0, N, j):
        a[i] += count

# 누적 합 계산
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

# 쿼리 처리
output = []
for l, r in queries:
    output.append(str(prefix_sum[r + 1] - prefix_sum[l]))

# 결과 출력
sys.stdout.write("\n".join(output) + "\n")
