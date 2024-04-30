import sys
import heapq
input = sys.stdin.readline

N = int(input())
min_heap = []  # 최소 힙
max_heap = []  # 최대 힙


for _ in range(N):
    k = int(input())
    # 최대힙이 없거나 최대힙의 -보다 값이 작을 때
    if not max_heap or k <= -max_heap[0]:
        heapq.heappush(max_heap, -k)
    else:
        heapq.heappush(min_heap, k)

    # 힙의 크기를 맞추기 위해 조정합니다.
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))


    # 힙 길이가 같음 = 입력 수가 짝수
    # 가장 가까운 두 값 중 작은 값 출력
    if len(max_heap) == len(min_heap):
        print(min(-max_heap[0],min_heap[0]))
    else:
        print(-max_heap[0])