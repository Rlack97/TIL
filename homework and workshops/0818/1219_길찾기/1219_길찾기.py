# 1219_길찾기 풀이
# 2022-08-18

import sys
sys.stdin = open('input.txt','r')

# DFS 정의
def roadsearch(road1,road2,startpoint):
    stack = []
    visited = [0]*100
    # 방문리스트 생성 

    visited[startpoint] = True
    # 출발지점 방문처리

    while True:
        if startpoint == 99:
            return 1
            # 목적지에 도달하면 1을 리턴

        if visited[road1[startpoint]] == 0:
            stack.append(startpoint)
            startpoint = road1[startpoint]
            visited[startpoint] = True
            # 첫번째 갈림길을 진행하지 않았을 경우 정점을 기록 후 이동

        elif visited[road2[startpoint]] == 0:
            stack.append(startpoint)
            startpoint = road2[startpoint]
            visited[startpoint] = True
            # 두번째 갈림길을 진행하지 않았을 경우 정점을 기록 후 이동

        elif visited[road2[startpoint]] == True and visited[road1[startpoint]] == True:
            if stack:
                startpoint = stack.pop()
                # 두 갈림길을 전부 가봤을 경우 스택을 pop하여 이전 정점으로 이동

            else:
                return 0
                # 더 이상 갈 곳이 없을 경우 목적지에 도달하지 못한 것이므로 0리턴

while True :
    tc, road = map(int,input().split())
    road1 = [0]*100
    road2 = [0]*100
    # 인덱스가 0부터 99까지 있는 리스트 생성
    cluster = list(map(int,input().split()))
    for a in range(len(cluster)):
        if a%2 == 0:
            if road1[cluster[a]] == 0:
                road1[cluster[a]] = cluster[a+1]
            else:
                road2[cluster[a]] = cluster[a+1]
    # 입력값 처리

    
    answer = roadsearch(road1,road2,0)

    print('#{} {}'.format(tc,answer))


    if tc == 10:
        break
    # 총 테스트케이스 갯수를 알려주지 않아 하드코딩으로 브레이크 설정
    # 입력이 끊기면 EOF에러가 나는데, 자동으로 읽어들이는 걸 멈추는 방법이 없을까?