# 5249_최소신장트리 풀이
# 2022/09/29
# 뭐, 수업 때 제대로 안보긴 했다만... 아예 모르겠다.

import sys
sys.stdin = open("input.txt","r")

def get(x):
    if parent[x] != x:
        parent[x] = get(parent[x])
    return parent[x]
# 해당 값이 포함된 그래프의 대표값 출력

def union(x,y):
    a = get(x)
    b = get(y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
    # 두 그래프를 하나로 합치는 함수, 더 큰값을 대표값으로 둔다

def same(x,y):
    return get(x) == get(y)
            

T = int(input())
for tc in range(1,T+1):
    answer = 0
    V,E = map(int,input().split())
    parent = [i for i in range(V+1)]
    edge = []
    for _ in range(E):
        n1, n2, w = map(int,input().split())
        edge.append((n1,n2,w))
    
    edge.sort(key=lambda x : x[2])
    while edge:
        a,b,v = edge.pop(0)
        if not same(a,b):
            # 대표값이 다름 == 사이클이 아니다.
            union(a,b)
            answer += v
            # 두 개를 합치고, 가중치를 답에 더해줌
    
    print('#{} {}'.format(tc, answer))

    # 간선 갯수를 세지 않아도 MST가 되는 이유???