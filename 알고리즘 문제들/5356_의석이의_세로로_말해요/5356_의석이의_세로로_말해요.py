# 5356_의석이의_세로로_말해요 풀이
# 2022-08-16

import sys
sys.stdin = open('input.txt','r')


T = int(input())
for tc in range(1,T+1):
    Q = [input() for _ in range(5)] 
    # 입력값 저장 

    answer = ''
    a, b = 0, 0

    while b <= 15:
        # 전체 단어 길이 15자 동안

        for a in range(5):
            cnt = 0
            for q in Q[a]:
                cnt += 1
            if b < cnt:
                # 인덱스가 존재하는 경우에만 

                answer += Q[a][b]
                # 답을 저장

        b += 1

    print('#{} {}'.format(tc, answer))