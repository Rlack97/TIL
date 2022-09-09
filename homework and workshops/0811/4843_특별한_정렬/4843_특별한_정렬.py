# 4843_특별한 정렬 풀이
# 2022-08-11

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    L = list(map(int,input().split()))
    sorted = []
    C =[0]*101
    # 카운트 정렬을 위해 비어있는 리스트와 카운트 리스트 C를 작성

    for i in range(0,N):
        C[L[i]] += 1
    # 제시된 정수를 인덱스 위치로 하는 카운트 리스트를 생성

    for k in range(0,101):
        if C[k] != 0:
            for a in range(C[k]):
                sorted.append(k)
        # 카운트 리스트를 읽으면서 값이 0이 아니면 해당 인덱스를 
        # 정렬 리스트에 삽입, 중복값이 있을 수 있으므로 카운트 리스트에 기록한
        # 값만큼 반복함

    print('#{}'.format(tc),end='')
    for i in range(1,11):
        if i % 2 != 0:
            print(' {}'.format(sorted[-(i//2+1)]),end='')
        elif i % 2 == 0:
            print(' {}'.format(sorted[(i//2)-1]),end='')
        
        # 정렬된 리스트는 오름차순이므로
        # -1,0,-2,1,-3,2,-4,3,-5,4 순으로 프린트

    print()

