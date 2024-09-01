import sys
input = sys.stdin.readline

N,M,t = map(int,input().split())

lines = [list(map(int,input().split())) for _ in range(M)]
lines.sort(key=lambda x : x[2])
# 모든 간선 양방향
# 한 번 이동할때마다 모든 도로의 비용이 t만큼 증가
# 모든 도시를 정복하는데 드는 최소비용

parents = [i for i in range(N+1)]

def find(x):
  if parents[x] != x:
    parents[x] = find(parents[x])
  
  return parents[x]

def union(a,b):
  a = find(a)
  b = find(b)

  if a<b:
    parents[b] =a
  else:
    parents[a] = b

answer = 0
count = 0

for a,b,cost in lines:
  if find(a) != find(b):
    union(a,b)
    answer += cost + (count*t)
    count+=1

print(answer)
