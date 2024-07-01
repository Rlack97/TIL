N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(M)]
dist = [1e9] * (N+1)
dist[1] = 0
# C = 0 또는 음수가 존재할 수 있다
# 나머지 도시로 가는 가장 빠른 시간은?
# 무한히 과거로 갈 수 있는 경우 -1만 출력
# 특정 도시로 가는 길이 없으면 해당 줄에만 -1 출력
# = 벨만 포드 알고리즘 

def BF():
    # 도시 갯수 (노드 수) 만큼 반복
    for i in range(1,N+1):
        # 간선 범위를 순회하면서
        for j in range(M):
            cur, next, cost = graph[j]
            # 다음 노드로 가는 거리가 현재 거리 + 가중치보다 클 경우 (현재 위치를 거쳐가는 것이 더 빠름)
            if dist[cur] != 1e9 and dist[next] > dist[cur] + cost:
                # 더 짧은 거리로 갱신한 값을 기록
                dist[next] = dist[cur] + cost
                # N번째에도 값 변경이 있다면 음수 순환이 존재
                if i == N:
                    return True
    return False

if BF():
    print(-1)
else:
    for i in range(2, N + 1):
        if dist[i] == 1e9:
            print(-1)
        else:
            print(dist[i])