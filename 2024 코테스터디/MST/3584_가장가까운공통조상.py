import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    parent = [0 for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        parent[b] = a  # a가 b의 부모
    A, B = map(int, input().split())
    a_parents, b_parents = [0, A], [0, B]

    # 노드 A,B의 모든 조상들을 리스트에 담는다
    while parent[A]:
        a_parents.append(parent[A])
        A = parent[A]
    while parent[B]:
        b_parents.append(parent[B])
        B = parent[B]

    a_level = len(a_parents)-1
    b_level = len(b_parents)-1

    while a_parents[a_level] == b_parents[b_level]:
        # 부모노드가 같으면 (공통 조상이면) 레벨을 한 단계씩 낮춰준다
        a_level -= 1
        b_level -= 1
        # 만약 다른 값이 나오면 직전 레벨이 최소공통조상
    print(a_parents[a_level+1])
