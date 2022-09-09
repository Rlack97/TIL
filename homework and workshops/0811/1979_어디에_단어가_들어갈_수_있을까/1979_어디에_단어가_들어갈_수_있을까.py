# 1979_어디에 단어가 들어갈 수 있을까 풀이
# 2022-08-11

import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]
    answer = 0
    for a in puzzle:
        #가로 행 하나에 대해서

        word = ''
        for w in a:
            word += str(w)
        # 모든 요소를 str화 하여 합침

        length = list(word.split('0'))
        # 합친 요소를 0으로 자른다.

        for l in length:
            cnt = 0
            for q in l:
                cnt += 1
            # 자른 뒤 남아있는 요소들의 길이를 잰 뒤

            if cnt == K:
                answer += 1
            # 길이가 K와 같다면 정답수 +1


    

    puzzle_rotated = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            puzzle_rotated[i][j] = puzzle[j][i]
    # 세로 칸을 세기 위해 x,y를 반전시킨 퍼즐 리스트를 생성, 
    # 이하 수식 동일
    
    for a in puzzle_rotated:
        word = ''
        for w in a:
            word += str(w)
        
        length = list(word.split('0'))
        for l in length:
            cnt = 0
            for q in l:
                cnt += 1
            if cnt == K:
                answer += 1
    
                
    print('#{} {}'.format(tc,answer))