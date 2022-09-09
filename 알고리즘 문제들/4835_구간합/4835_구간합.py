# 4835_구간합 풀이
# 2022-08-09

import sys
sys.stdin = open('input.txt','r')
# 입력값 받아오기

def Bubblesort(list,len):
    for i in range(len-1,0,-1):
        for j in range(0,i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1], list[j]
# 버블소팅을 사용할 것이므로 미리 정의함.

T = int(input())
# 테스트 케이스 갯수

for tc in range(T):
    N, M = map(int,input().split())          
    L = list(map(int,input().split()))       
    # 정수 리스트와 길이, 합을 구할 구간의 길이를 입력받음

    sumlist = []
    # 구간합들을 넣어둘 리스트 초기화

    for i in range(0,N-M+1):  
        #인덱스 에러 방지를 위해 N-M인덱스까지만 계산

        sum = 0
        #구간합 초기화

        for k in range(M):
            sum +=L[i+k]
            #구간 내 숫자들을 구간합 변수에 더함

        sumlist.append(sum)
        # 구간합들을 리스트에 넣음
    
    Bubblesort(sumlist,N-M+1)
    # 구간합 리스트를 거품 정렬함

    answer = sumlist[-1] - sumlist[0]
    # 오름차순 정렬이므로 맨 뒤의 최댓값과 맨 앞의 최솟값의 차를 구함

    print('#{} {}'.format(tc+1,answer))
    # 테스트케이스 숫자와 구한 값을 출력