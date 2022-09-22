# 5189_전자카트 풀이
# 2022/09/22

import sys
sys.stdin = open("input.txt","r")


# 재귀함수 정의
def rooms(prev,here):
    global power

    visited[here] = 1
    # 현 위치를 방문처리

    power += area[prev-1][here-1]
    # 이전 위치에서 현 위치로 오는 데 필요한 사용량을 합친다

    for i in range(1,N+1):
        if visited[i] == 0:
            rooms(here, i)
            # 방문하지 않은 곳들 대상으로 재귀 실행
            power -= area[here-1][i-1]
            visited[i] = 0
            # return으로 올라오면서 해당 값을 제거

    # 방문처리를 함수 맨 앞에 하므로, 종료조건이 뒤로 감.
    if visited.count(0) == 1:
    
        power += area[here-1][0]
        power_list.append(power)
        # 모든 곳을 방문했을 때, 현위치에서 1로 돌아가는 값을 더해주고 해당 값을 저장

        power -= area[here-1][0]
        # 리턴 하기 전 계산 초기화
            


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    area = [list(map(int,input().split())) for _ in range(N)]
    visited =[0] * (N+1)

    power = 0
    power_list = []

    rooms(1,1)

    answer = min(power_list)
    print('#{} {}'.format(tc, answer))
