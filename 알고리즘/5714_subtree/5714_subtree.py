# 5714_subtree 풀이
# 2022/09/15

import sys
sys.stdin = open('input.txt','r')

T = int(input())

def node_count(root):
    global cnt 

    if root:
        node_count(L[root])
        cnt += 1
        node_count(R[root])
# 입력값 아래의 노드를 세는 함수

for tc in range(1,T+1):
    E, N = map(int,input().split())
    L = [0]*(E+2)
    R = [0]*(E+2)
    input_list = list(map(int,input().split()))

    for i in range(E):
        if L[input_list[2*i]] == 0:
            L[input_list[2*i]] = input_list[2*i+1]
        else:
            R[input_list[2*i]] = input_list[2*i+1]
    # 자식 리스트 생성

    cnt = 0
    node_count(N)

    print('#{} {}'.format(tc, cnt))