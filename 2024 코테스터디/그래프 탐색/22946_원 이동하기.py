# 0224
# https://pypy333.tistory.com/20
import math
import sys
input = sys.stdin.readline

# 그래프 생성용 dfs


def dfs(x):
    ax, ay, ar = circles[x]

    # 자기 자신을 제외한, 방문하지 않은 원과의 관계를 계산
    for i in range(x+1, n+1):
        if visited[i] == 0:
            bx, by, br = circles[i]
            d = math.sqrt(((ax-bx)*(ax-bx)+(ay-by)*(ay-by)))

            # 내부관계일 경우 그래프에 기록
            if abs(ar-br) > d:
                graph[x].append(i)
                graph[i].append(x)
                visited[i] = 1
                dfs(i)


# 가장 먼 거리 찾는 함수
def lfs(L, x):
    global res, start_point
    if L > res:
        res = L
        start_point = x

    for y in graph[x]:
        if visited[y] == 0:
            visited[y] = 1
            lfs(L+1, y)
            visited[y] = 0


N = int(input())
circles = []
for n in range(N):
    x, y, R = map(int, input().split())
    circles.append((x, y, R))

# 원들의 포함 관계를 계산하여 그래프로 만든다.
# 반지름이 무한인, 가장 바깥의 원을 추가하고 반지름 큰 순으로 정렬
circles.append((0, 0, float('inf')))
circles.sort(reverse=True, key=lambda x: x[2])

# 그래프 생성
graph = [[]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
dfs(0)

# 답 변수
res = 0
start_point = 0

# 그래프 생성에 방문리스트를 사용하였으니 초기화
# 한 지점에서 가장 먼 곳을 탐색
visited = [0]*(n+1)
visited[0] = 1
lfs(0, 0)

# 해당지점에서 가장 먼 곳을 재탐색, 두 지점 간의 거리 구함.
visited = [0]*(n+1)
lfs(0, start_point)
print(res)
