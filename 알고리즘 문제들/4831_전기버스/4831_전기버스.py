# 4831-전기버스 풀이
# 2022-08-09

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    K, N, M = map(int,input().split()) 
    # 각각 한번으로 갈 수 있는 정류장 수, 정류장 종점(길이), 설치된 충전기 수

    Mlist = list(map(int,input().split()))
    Bus_Nosun = [0]*(N+1)
    for m in Mlist:
        Bus_Nosun[m] = 1
    # 일차원 리스트를 통해 충전기가 있는 부분을 1로 표시
    
    i = 0
    charge = 0
    # 버스의 출발지점 i, 충전횟수 charge를 선언

    while True:
        station = list(Bus_Nosun[i:i+K+1])
        # 버스가 갈 수 있는 K만큼의 거리 안에 있는 일차원 리스트의 요소들을 불러옴

        if 1 not in station[1:] :
            charge = 0
            break
        # 자기 자신을 제외한 범위 안에 1, 즉 충전소가 없으면 진행 불가능이므로 charge에 0을 저장하면서 반복문 종료

        for a in range(1,K+1):
            if station[a] == 1:
                id = a
        # 해당 범위 안에 충전소가 있다면 인덱스값을 기록 (가장 마지막 충전소의 인덱스 덧씌워짐)

        i += id
        # 충전소의 위치로 출발 위치를 변경

        charge += 1
        # 충전에 성공했으므로 충전횟수를 1회 늘림

        if i >= N-K:
            break
        # 더 이상의 충전 없이 종점에 도착할 수 있는 위치라면 반복문 종료
        

    print('#{} {}'.format(tc,charge))