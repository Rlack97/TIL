import sys
input = sys.stdin.readline
from collections import deque

M, t, N = map(int,input().split())
left = deque()
right = deque()
boat = []
marina = {
    'l' : left,
    'r' : right
}

for i in range(N):
    time, arr = input().split()
    time = int(time)

    if arr == 'left':
        left.append((i, time, 'l'))
    else:
        right.append((i, time, 'r'))
        
def boarding(side : deque, time_now: int):
    boarding_people = 0
    while boarding_people<M and side:
        customer_id, arrv_time, l_or_r = side.popleft()
        if arrv_time > time_now:
            side.appendleft((customer_id, arrv_time, l_or_r))
            break
        else: 
            boarding_people += 1
            arrived_status.append((customer_id, time_now + t))
            
def opposite(position:str):
    return 'r' if position == 'l' else 'l'
         
arrived_status = []
time_now = 0
status = 'l'

while left or right: 
    if left and right:
        id, min_arrv_time, position = min(left, right, key = lambda x:x[0][1])[0]
        if left[0][1] == right[0][1]:
        # 둘 다 min_arrv_time 같으면 status와 position 같은쪽 우선
            id, min_arrv_time, position = marina[position][0]
    elif left: ### cuz out of range idx err
        id, min_arrv_time, position = left[0]
    elif right:
        id, min_arrv_time, position = right[0]


    ## main_flow
    time_now = max(time_now, min_arrv_time) ## 기다려야 하는 경우 처리
     
    if status != position: # 현재 배 상태와 반대쪽에 손님이 먼저 올 경우
        boarding(marina[status], time_now) # 일단 태울 수 있는 사람 다 태워서 출발
        time_now += t # 이동시간 추가
        status = position 
        
    boarding(marina[position], time_now) 
    time_now += t
    status = opposite(status) 
        

for i in sorted(arrived_status, key = lambda x : x[0]):
    print(i[1])