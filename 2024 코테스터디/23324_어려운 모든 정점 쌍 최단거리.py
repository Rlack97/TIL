import sys
input = sys.stdin.readline


def Find(x):

    if x != disjoint[x]:
        disjoint[x] = Find(disjoint[x])

    return disjoint[x]


def Union(a, b):

    a = Find(a)
    b = Find(b)

    if a > b:
        disjoint[a] = b
    else:
        disjoint[b] = a


def Answer(parent):

    tmp = 0
    for i in range(1, N+1):
        if Find(i) == parent:
            tmp += 1
    return tmp


N, M, K = map(int, input().split())

disjoint = [i for i in range(N+1)]

Node1, Node2 = 0, 0

for i in range(M):

    u, v = map(int, input().split())

    if i != K-1:  # 가중치가 있는 지점은 합치지않는다.
        Union(u, v)
    else:
        Node1, Node2 = u, v

if Find(Node1) == Find(Node2):  # 예제 2와 같다면
    print(0)
else:
    total = Answer(disjoint[1])

    print(total*(N-total))
