# 6485_삼성버스 풀이
# 2022-08-09
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())         # 버스 노선의 개수
    nosun = []
    for i in range(1,N+1):   
        # 각 버스 노선들에 대해서

        A, B = map(int,input().split())
        nosun.append(range(A,B+1))    
        # 제공되는 A,B의 범위를 빈 리스트에 저장

    P= int(input())
    Cj = []

    for p in range(1,P+1):
        C = int(input())
        Cj.append(C)
        # 몇번째의 버스정류장을 볼 것인지 지정하는 C값 저장

    answer = [0]*P
    # 기록을 할 빈 리스트 생성

    for i in range(0,P):  # P만큼의 정류장에 있어서
        cnt = 0
        t = Cj[i]  # 확인할 정류장은 Cj의 기록 순서에 맞게

        for k in range(N): 
            if t in nosun[k]: 
                cnt += 1
                # 해당 정류장 값이 노선 범위 안에 있다면 카운트 +1

        answer[i] = cnt
        # 해당 위치에 지나가는 총 노선 수를 기록

    print('#{}'.format(tc), end='')
    for z in answer:
        print(' {}'.format(z),end='')
    print('')
    # 입력 양식에 맞게 조절