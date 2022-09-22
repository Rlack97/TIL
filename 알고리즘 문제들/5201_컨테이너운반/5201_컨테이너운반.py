# 5201_컨테이너운반 풀이
# 2022/09/22

import sys
sys.stdin = open("input.txt","r")


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    cargo = list(map(int,input().split()))
    truck = list(map(int,input().split()))
    total_weight = 0

    cargo.sort(reverse=True)
    truck.sort(reverse=True)
    # 트럭과 짐 리스트를 내림차순 정렬

    i,j = 0,0
    # 트럭과 짐 인덱스 설정

    while i < len(truck) and j < len(cargo):
        # 인덱스가 벗어나게 되면 중지 

        if truck[i] >= cargo[j]:
            # 짐이 트럭이 담을 수 있는 범위 이내의 값이라면

            total_weight += cargo[j]
            # 총 무게에 넣어주고

            i += 1
            j += 1
            # 다음 트럭과 짐을 확인한다

        else:
            j += 1
            # 못 담는 짐이라면 다음 짐을 확인한다.

    answer = total_weight
    print('#{} {}'.format(tc, answer))

# 트럭 하나의 시점에서 담을 수 있는 가장 큰 짐을 담는 그리디 로직.