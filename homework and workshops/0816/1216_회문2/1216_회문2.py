# 1216_회문 풀이
# 2022-08-16

import sys
sys.stdin = open('input.txt','r')



for T in range(1,11):
    tc = int(input())
    Q = [input() for _ in range(100)]
    maxlength = 0
    # 입력 및 정답 초기화

    for i in range(1,51):
    # 회문의 길이를 순회
        for a in range(100):
        # 가로행 순회
            m, n = 0, 0
            while n+i <= 100:
                S = Q[a][n:n+i]
                # 회문 길이만큼 슬라이싱한 str 형성

                if S == S[::-1] and i > maxlength:
                    maxlength = i
                    # 회문판별은 그냥 ::-1 사용하면 깔끔함
                else:
                    n+=1
            
                    


    Q2 = [[0]*100 for _ in range(100)]
    for a in range(100):
        for b in range(100):
            Q2[a][b] = Q[b][a]
        Q2[a] = "".join(Q2[a])
    
    # 주어진 문자열 반전


    for i in range(1,51):
        for a in range(100):
            m, n = 0, 0
            while n+i <= 100:
                S = Q2[a][n:n+i]
                if S == S[::-1] and i > maxlength:
                    maxlength = i
                else:
                    n+=1
    # 위와 동일

    print('#{} {}'.format(tc, maxlength))