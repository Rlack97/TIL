# 4836_색칠하기 풀이
# 2022-08-11

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    grid = [['']*10 for _ in range(10)]
    purple = 0
    # 10 x 10의 비어있는 리스트 및 정답 값 초기화

    for a in range(N):
        r1,c1,r2,c2,c = map(int,input().split())
        for i in range(r1-1,r2):
            for j in range(c1-1,c2):
                grid[i][j] += str(c)

        # 제시된 사각형의 위치에 색깔정보를 str로 집어넣음
        
    
    for s in range(10):
        for k in grid[s]:
            if '1' in k and '2' in k:
                purple += 1
    # 빨강의 색깔정보와 파랑의 색깔정보가 같이있는 칸이 보라색
    # 몇 번 칠해졌는지는 중요하지 않기 때문에 str로 값 오류를 배제

    print('#{} {}'.format(tc,purple))