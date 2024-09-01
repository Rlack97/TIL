import sys

# 입력 받기
input = sys.stdin.readline
N, M = map(int, input().split())
course = list(map(int, input().split()))
costs = [list(map(int, input().split())) for _ in range(N - 1)]

# 각 구간을 몇 번 사용하는지 계산하기
usage_count = [0] * (N - 1)
for i in range(M - 1):
    start = min(course[i], course[i + 1]) - 1
    end = max(course[i], course[i + 1]) - 1
    for j in range(start, end):
        usage_count[j] += 1

# 각 구간별 최소 비용 계산
total_cost = 0
ic_card_purchased = [False] * (N - 1)

for i in range(N - 1):
    A, B, C = costs[i]
    if usage_count[i] == 0:
        continue
    # IC카드를 구매한 후, 사용하는 것이 더 저렴한 경우
    if C + usage_count[i] * B < usage_count[i] * A:
        total_cost += C + usage_count[i] * B
        ic_card_purchased[i] = True
    else:
        total_cost += usage_count[i] * A

# 결과 출력
print(total_cost)
