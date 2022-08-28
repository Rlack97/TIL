# 4828-min-max
# 2022-08-09

import sys
sys.stdin = open('input.txt','r')

def Bubblesort(list,len):
    for i in range(len-1,0,-1):
        for j in range(0,i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
# 버블소트를 정의

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    Y = list(map(int,input().split()))
    Bubblesort(Y,N)
    # 버블소트를 사용하여 리스트 정렬
    sorted = Y
    Max, Min = sorted[-1], sorted[0]
    # 오름차순이므로 최댓값의 인덱스는 -1, 최솟값의 인덱스는 0
    answer = Max - Min
    print('#{} {}'.format(tc,answer))