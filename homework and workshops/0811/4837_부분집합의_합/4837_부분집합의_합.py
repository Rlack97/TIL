# 4837_부분집합의 합 풀이
# 2022-08-11

import sys
sys.stdin = open('input.txt','r')

A = [1,2,3,4,5,6,7,8,9,10,11,12]
MD = []

for i in range(1<<12):
    length = 0
    setsum = 0
    for j in range(12):
        if i & (1<<j):
            length += 1
            setsum += A[j]
    MD.append((length,setsum))

# 리스트의 부분집합의 길이와 합을 저장
    
T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    answer = 0
    for a in MD:
        if a[0] == N and a[1] == K:
            answer += 1

    # 조건에 맞는 경우를 출력

    print('#{} {}'.format(tc,answer))
