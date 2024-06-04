import sys
import heapq
from collections import deque
input = sys.stdin.readline

# 가방이 담을 수 있는 모든 보석 중 가장 가치 있는 보석을 선택
# 작은 가방부터 탐색
N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
jewels.sort(key=lambda x: x[0])
backpacks = [int(input()) for _ in range(K)]
backpacks.sort()
total_cost = 0
heap = []
jewels = deque(jewels)

for back in backpacks:
    while jewels:
        weight, cost = jewels[0]
        if weight <= back:
            # 가방에 들어가는 보석
            heapq.heappush(heap, -cost)
            # 값을 음수화해서 넣어야 가장 큰 값이 heappop으로 나오기 때문
            jewels.popleft()
            # 보석 30만개인데 popleft?
            # 그래서 deque 사용
        else:
            # 이후 보석들은 전부 안들어감
            break

    if heap:
        total_cost += - heapq.heappop(heap)
print(total_cost)
