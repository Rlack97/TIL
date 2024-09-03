# 도착순으로 들어가지만, 예약된 사람의 시간이 맞을 경우 그 사람 먼저
# 이중 힙 문제.

import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

N = int(input())

# 예약시간, 도착한 시간
schedule = [list(map(int, input().split())) + [n] for n in range(N)]

# 도착한 순으로 정렬
schedule.sort(key=lambda x:x[1])

# 예약 힙과 도착 힙을 별도로 선언
reservation = []
arrival = []

# 기록용 변수들
# 최대 대기시간, 현재 시간, 받은 손님 수, 입장한 손님 index
answer = 0
now = 0
complete = 0
index = 0
enter_done = defaultdict(bool)


while complete < N:
    table = False
    
    # 도착한 사람들을 힙에 추가
    while index < N and schedule[index][1] <= now:
        # 예약시간으로 최소힙 구성
        heapq.heappush(reservation,(schedule[index][0], schedule[index][1], schedule[index][2]))
        
        # 도착시간으로도 구성
        heapq.heappush(arrival,(schedule[index][1], schedule[index][0], schedule[index][2]))

        index += 1

    

    # 예약한 손님이 있으면 해당 손님 입장
    while reservation and reservation[0][0] <= now:
        reser, ariv, id =heapq.heappop(reservation)

        # 이미 들어간 사람이거나, 예약 시간이 정확하지 않다면 다음손님 확인
        if enter_done[id] or reser != now:
            continue
        
        enter_done[id] = True

        # 기다린 시간 기록
        answer = max(answer, now-ariv)
        complete += 1
        table = True


        break

    
    # 예약 손님 없으면 온 순서대로 입장
    while not table and arrival and arrival[0][0] <= now:
        ariv, reser, id =heapq.heappop(arrival)

        # 이미 들어갔던 손님일 경우 다음손님 확인
        if enter_done[id]:
            continue
        
        else:
            enter_done[id] = True

            # 기다린 시간 기록
            answer = max(answer, now-ariv)
            complete += 1

            break

    now += 1


print(answer)
