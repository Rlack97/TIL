# 5789-현주의 상자바꾸기 풀이
# 2022-08-09

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N,Q = map(int,input().split())
    # 박스가 N, 작업 횟수가 Q

    num = []
    for q in range(Q):
        L,R = map(int,input().split())
        num.append([range(L,R+1),q+1])
    # 작업의 범위와, 해당 작업의 횟수를 리스트에 저장

    boxes = [0]*N
    # 작업 횟수를 기록할 빈 리스트

    for a in range(Q):               # 각 작업에 대해서
        for z in num[a][0]:          # 주어진 범위 내의 숫자들을 인덱스로 하는 박스 리스트에
            boxes[z-1] = num[a][1]   # 작업 횟수를 업데이트


    print('#{}'.format(tc),end='')
    for i in range(N):
        print(' {}'.format(boxes[i]), end='')
    print('')
    # 출력 양식 맞추기