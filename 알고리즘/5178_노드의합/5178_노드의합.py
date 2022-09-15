# 5178_노드의합 풀이
# 2022/09/15

#  마지막 노드의 조상 노드에 저장된 정수의 합
import sys
sys.stdin = open('input.txt','r')

def Tsum(node):
    if node:
        if node in leaves:
            return tree[node]

        else:
            sum_value = Tsum(L[node]) + Tsum(R[node])
            tree[node] = sum_value
            return sum_value
    else:
        return 0
 
# 아래 두 자손을 합쳐서 올리는 함수
        

T = int(input())
for tc in range(1,T+1):
    N, M, L1 = map(int,input().split())
  
    tree = [0]*(N+1)
    L = [0]*(N+1)
    R = [0]*(N+1)
    # 트리값, 자손 리스트

    leaves = []
    # 이파리 인덱스 리스트
    
    for m in range(M):
        leaf_num, number =  map(int,input().split())
        tree[leaf_num] = number
        leaves.append(leaf_num)
        # 리프값 입력, 리프 리스트에 추가

    if (N-1) % 2 == 0:
        for i in range(1,(N-1)//2+1):
            L[i] = (2*i)
            R[i] = (2*i+1)
    else:
        for i in range(1,(N-1)//2+1):
            L[i] = (2*i)
            R[i] = (2*i+1)
        L[(N-1)//2+1] = 2*((N-1)//2+1)
    # 자손리스트 작성
 
    Tsum(1)

    answer = tree[L1]
    print('#{} {}'.format(tc, answer))