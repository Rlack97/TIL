# 1966_숫자를 정렬하자 풀이
# 2022-08-11
import sys
sys.stdin = open('input.txt','r')

# 버블소트 사용
def bubblesort(list,length):
    for i in range(length-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    nlist = list(map(int,input().split()))
    bubblesort(nlist,N)


    print('#{}'.format(tc,),end=' ')
    print(*nlist)
