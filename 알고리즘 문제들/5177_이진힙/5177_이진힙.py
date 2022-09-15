# 5177_이진힙 풀이
# 2022/09/15

#  마지막 노드의 조상 노드에 저장된 정수의 합
import sys
sys.stdin = open('input.txt','r')

def enq(node):
    global last
    last += 1
    heap[last] = node

    c = last
    p = c // 2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p  = c // 2
# 힙 삽입 함수

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))

    heap = [0]*(N+1)
    L = [0]*(N+1)
    R = [0]*(N+1)

    if (N-1) % 2 == 0:
        for i in range(1,(N-1)//2+1):
            L[i] = (2*i)
            R[i] = (2*i+1)
    else:
        for i in range(1,(N-1)//2+1):
            L[i] = (2*i)
            R[i] = (2*i+1)
        L[(N-1)//2+1] = 2*((N-1)//2+1)
    # 이진트리 자식리스트

    last = 0
    for i in num_list:
        enq(i)
    # 이진트리 삽입

    answer = 0
    i = N

    while True:
        answer += heap[i//2]
        if i == 1: 
            break
        i = i//2
    # 조상 더하기        


    print('#{} {}'.format(tc, answer))