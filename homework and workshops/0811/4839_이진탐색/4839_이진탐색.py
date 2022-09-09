# 4839_이진탐색 풀이
# 2022-08-11

import sys
sys.stdin = open('input.txt','r')

#이진탐색 정의
def b_search(totalpage,goalpage):
    start = 1
    end = totalpage
    cnt = 0
    while start <= end:
        middle = (start + end) // 2  
        cnt += 1
        # 중간값을 찾고 카운팅

        if middle == goalpage:
            return cnt
            # 목표값을 찾았을 시 카운팅을 반환

        elif middle > goalpage:
            end = middle
            # 목표값이 더 작을 경우, 중간값을 검색범위의 끝으로 함

        else:
            start = middle
            # 목표값이 더 클 경우, 중간값을 검색범위의 시작으로 함



T= int(input())
for tc in range (1, T+1):
    P, A, B = map(int,input().split())

    if b_search(P,A) > b_search(P,B):
        winner = 'B'    
    elif b_search(P,A) < b_search(P,B):
        winner = 'A'  
    elif b_search(P,A) == b_search(P,B):
        winner = '0'
        
    # 목표값을 비교해서 승자 저장 후 출력
    
    print('#{} {}'.format(tc,winner))