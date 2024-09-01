import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
cities = [[1e9 for _ in range(n+1)] for _ in range(n+1)]
routes = [[[] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
  start, end, cost = map(int,input().split())
  if cities[start][end] > cost:
    cities[start][end] = cost
    routes[start][end] = [start,end]

  # 시작 및 도착이 정해진 단방향 그래프

"""
 n개의 줄을 출력하는데, i번째 출의 j번째 숫자는 i->j의 최소 비용.
 불가능하다면 0

 그 이후에 n*n개의 줄을 출력하는데, ixn + j번째 줄에는 i->j 최소 비용에 포함된 도시의 갯수 k
 그 다음 i->j의 경로를 출력 (i,j포함)
 갈 수 없다면 0 하나만 출력
"""
# 자기 자신에게 가는 비용 및 경로 초기화
for i in range(1, n+1):
    cities[i][i] = 0

for i in range(1,n+1): # 중간
  for j in range(1,n+1): # 시작
    for k in range(1,n+1): # 끝
      # 직통 경로가 존재하지 않거나, 우회로가 더 짧을 경우 갱신
      # 초기화 값이 1e9이므로, 중간 경로가 없는 경우는 걸러짐
      if cities[j][k] > cities[j][i] + cities[i][k]:
        cities[j][k] = cities[j][i] + cities[i][k]
        routes[j][k] = routes[j][i] + routes[i][k][1:] 


# 비용 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if cities[i][j] == 1e9:
            print(0, end=' ')
        else:
            print(cities[i][j], end=' ')
    print()

# 최소거리 루트 출력
for i in range(1, n+1):
    for j in range(1, n+1):
      if cities[i][j] == 1e9 or i == j:
        print(0)
      else:
         print(len(routes[i][j]), *routes[i][j])
        