# 입 퇴장 기록이 있을 때, 가장 많이 있는 시간대와 몇 개? 있는지
# 21억??? 리스트 쓰면 안된다는건 알겠다.
# == defaultdict 쓰기

from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
history = defaultdict(int)

# 딕셔너리에 입퇴장시간을 키로 하여 변동값을 기록해준다.
for _ in range(N):
  start, end = map(int,input().split())
  history[start] += 1
  history[end] -= 1

# 시간순 정렬
times = sorted(history.keys())

mos = 0
max_mos = -1
start = 0
end = 0
# 기록된 모든 시간의 출입 수치를 전부 합쳐준다.
# 그 중 가장 큰값을 기록
for t in times:
  mos += history[t]
  if mos > max_mos:
    max_mos = mos
    start = t
    flag = 1
  elif mos < max_mos and flag:
    end = t
    flag = False

print(max_mos)
print(start,end)
