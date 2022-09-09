# 1201_Ladder1 풀이
# 2022-08-11

import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    tn = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    # 테스트 케이스 번호 및 2차원 리스트 정보 수령

    dx = [-1,0,0]
    dy = [0,-1,1]
    d = 0
    
    # 방향 좌표 지정 (x값, y값, y값)

    for a in range(100):
        if ladder[99][a] == 2:
            x,y = 99,a
            # 도착지점에서 거꾸로 가야 연산수를 줄일 수 있음, 도착지점 좌표를 x,y로 저장

    while x > 0:       # 맨 위에 도착하면 반복문 종료

        if y != 0 and ladder[x][y-1] == 1:
            d = 1

        elif y != 99 and ladder[x][y+1]== 1:
            d = 2

        ladder[x][y] = 0
        x += dx[d]
        y += dy[d]
        d = 0            

    start = y
    # 지정된 도착점에 대응되는 출발점의 x좌표

    print('#{} {}'.format(tn,start))