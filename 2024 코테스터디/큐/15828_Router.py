import sys
from collections import deque
input = sys.stdin.readline

#버퍼 -> 선입선출
#꽉 차거나 넘칠 경우 공간 여유가 생길때까지 추가되는 패킷은 전부 버려짐

N = int(input())
packets = deque([])
while True:
    p = int(input())
    
    # 입력종료
    if p == -1:
        break
    
    #작업완료, 선입선출이므로 가장 왼쪽값 제거
    elif p == 0:
        packets.popleft()


    #패킷이 꽉 차지 않았다면 패킷에 삽입
    elif len(packets) < N:
        packets.append(p)

if packets:
    print(*packets)
else:
    print('empty')