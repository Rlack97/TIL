# 1221_GNS 풀이
# 2022-08-12

import sys
sys.stdin = open('input.txt','r')

ailen = {'ZRO': 0, 'ONE': 1,'TWO': 2,'THR': 3,'FOR': 4,'FIV': 5,'SIX': 6,'SVN': 7,'EGT': 8,'NIN': 9}
# 외계어 사전 작성
korean = dict(map(reversed,ailen.items()))
# 이를 뒤집은 지구어 사전 작성

# 10까지의 값을 정렬하는 카운트 정렬 정의
def mycountsort(list,len):
    emptylist = [0]*10
    sorted = []
    for i in range(len):
        emptylist[list[i]] += 1
    
    for k in range(10):
        for t in range(emptylist[k]):
            sorted.append(k)
    
    return sorted

T = int(input())
for tc in range(1,T+1):
    tn, total = map(str,input().split())
    numbers = list(map(str,input().split()))
    earth = []
    for k in numbers:
        earth.append(ailen[k])
        # 외계어를 지구어로 바꿔서 저장
    
    sorted = mycountsort(earth,int(total))
    # 숫자를 정렬

    returnword = []
    for z in sorted:
        returnword.append(korean[z])
        # 지구어를 다시 외계어로 변환

    answer = returnword

    print('#{}'.format(tc))
    print(*answer) # 리스트를 언패킹, 이거 진짜 편해서 좋다