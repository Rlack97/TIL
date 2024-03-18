# 0312
# 음수 간선이 포함된 최단거리 = 벨만 포드 알고리즘
# 기본은 다익스트라 알고리즘
# 음의 간선이 순환에 포함되면 최단거리가 음의 무한대가 되는 경우 발생

import sys
input = sys.stdin.readline


def bf():
    # 도시 갯수 (노드 수) 만큼 반복
    for i in range(n):
        # 간선 수 (도로 + 웜홀)을 순회하면서
        for j in range(len(edges)):
            cur, next, cost = edges[j]

            # 다음 노드로 가는 거리가 현재 거리 + 가중치보다 클 경우 (현재 위치를 거쳐가는 것이 더 빠름)
            if dist[next] > dist[cur] + cost:

                # 더 짧은 거리로 갱신한 값을 기록
                dist[next] = dist[cur] + cost

                # 마지막에 값 변경이 있다면 음수 순환이 존재
                if i == n - 1:
                    return True
    return False


TC = int(input())

for _ in range(TC):
    n, m, w = map(int, input().split())
    edges = []
    dist = [1e9] * (n + 1)
    for i in range(m + w):
        s, e, t = map(int, input().split())

        # 웜홀
        if i >= m:
            t = -t
        else:
            edges.append((e, s, t))
        edges.append((s, e, t))

    # 음수 순환이 존재 = 출발보다 시간이 뒤로 감
    if bf():
        print("YES")
    else:
        print("NO")
