#4861_회문 풀이
# 2022-08-16

import sys
sys.stdin = open('input.txt','r')


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) 
    # 정사각형 길이 N과, 회문 M의 길이를 입력

    Q = [input() for _ in range(N)]
    # str 형태로 문자들을 입력받음

    row = ''
    column = ''

    for a in range(N):
        m,n = 0,0
        # 회문 내부 인덱스 m과, 회문 시작지점 인덱스 n을 설정
        while n+M < N+1:
            S = Q[a][n:n+M]
            # 가로 상태에서는 슬라이싱해서 회문 길이만큼의 str을 생성

            if S[m] != S[-1-m]:
                # 양 끝을 비교하여 일치하지 않으면
                n += 1
                # 다음 인덱스로 넘어감
                m = 0
                # 내부 인덱스도 초기화

            m += 1
            # 일치할 경우 회문 내부의 인덱스 증가

            if m == M//2:
                # 절반이 서로 일치하면 회문
                row = S
                break
                # 값을 저장하고 브레이크

    for a in range(N) :
        m,n = 0,0
        while n+M < N+1:
            C = ''
            for k in range(n,M+n):
                C += Q[k][a]
                # 세로의 경우 슬라이싱을 통한 접근이 불가능하므로, 인덱스 활용 접근
                # 회문의 길이가 전체 길이보다 작은 경우, 시작값과 끝 값의 인덱스가 증가할 필요가 있음
            if C[m] != C[-1-m]:
                n += 1
                m = 0
            m += 1
            if m == M//2:
                column = C
                break
            # 나머지는 가로와 동일

    if row:
        answer = row
    elif column:
        answer = column
    
    # 회문은 하나 뿐이므로 True 판정을 통해 값을 저장
    
    print('#{} {}'.format(tc,answer))

