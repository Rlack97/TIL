# https://imzzan.tistory.com/175

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def makeTree(currentNode, parent):
    for Node in graph[currentNode]:
        if Node != parent:
            child[currentNode].append(Node)
            parents[Node] = currentNode
            makeTree(Node, currentNode)


def countSubtreeNodes(currentNode):
    # 자신도 자신을 루트로 하는 서브트리에 포함되므로 0이 아닌 1에서 시작한다.
    size[currentNode] = 1
    for Node in child[currentNode]:
        countSubtreeNodes(Node)
        size[currentNode] += size[Node]


N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
child = [[] for _ in range(N+1)]
parents = [-1] * (N+1)
size = [0] * (N+1)

for n in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


makeTree(R, -1)
countSubtreeNodes(R)

# q를 루트로 하는 서브트리에 속한 정점의 수를 출력
for q in range(Q):
    u = int(input())
    print(size[u])
