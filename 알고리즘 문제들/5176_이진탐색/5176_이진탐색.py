# 5716_이진탐색 풀이
# 2022/09/15

# 루트값 및 N//2번 노드의 값을 출력
import sys
sys.stdin = open('input.txt','r')

def J2(node):
    global i 
    if node:
        J2(L[node])
        tree[node] = i
        i += 1
        J2(R[node])
# 왼쪽 아래부터 수를 채워넣는 함수



T = int(input())
for tc in range(1,T+1):
    N = int(input())

    tree = [0]*(N+1)
    L = [0]*(N+1)
    R = [0]*(N+1)
   # 트리값, 자식리스트

    if (N-1) % 2 == 0:
        for i in range(1,(N-1)//2+1):
            L[i] = (2*i)
            R[i] = (2*i+1)
    else:
        for i in range(1,(N-1)//2+1):
            L[i] = (2*i)
            R[i] = (2*i+1)
        L[(N-1)//2+1] = 2*((N-1)//2+1)
    # 자식리스트 넣기

    i = 1
    # 1부터 숫자를 넣는다
    
    J2(1)

    root = tree[1]
    root2 = tree[N//2]
    print('#{} {} {}'.format(tc, root, root2))