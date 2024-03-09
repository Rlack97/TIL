# 우선순위 큐
# deque을 쓰는 문제가 아니니 기억해두자

import heapq
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
cards = []

# for _ in range(N):
#     k = int(input())
#     heapq.heappush(cards, k)

# total = 0

# while len(cards) > 1:
#     a = heapq.heappop(cards)
#     b = heapq.heappop(cards)
#     ab = a+b

#     total += ab
#     heapq.heappush(cards, ab)

# print(total)

cards_2 = []
for _ in range(N):
    k = int(input())
    cards_2.append(k)

cards_2.sort()

card_deque = deque(cards_2)
total_2 = 0
while len(card_deque) > 1:
    a = card_deque.popleft()
    b = card_deque.popleft()
    ab = a+b

    total_2 += ab
    card_deque.appendleft(ab)

print(total_2)
