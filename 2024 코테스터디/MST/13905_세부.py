import sys
input = sys.stdin.readline

N,M = map(int,input().split())
s,e = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(M)]
graph.sort(key = lambda x: x[2], reverse=True)
parents = [i for i in range(N+1)]
answer = 0
def find(x):
  if parents[x] != x:
    parents[x] = find(parents[x])
  
  return parents[x]

def union(a,b):
  a = find(a)
  b = find(b)

  if a<b:
    parents[b] = a
  else:
    parents[a] = b

for a, b, limit in graph:
  
  if find(a) != find(b):
    union(a,b)

    if find(s) == find(e):
      answer = limit
      break

print(answer)


# 다리 가중치 = 무게제한
# 즉, s->e의 경로 중 '최소가중치가 가장 높은' 경로의 최소가중치
# 최대 최소 경로

# 1. 가중치 기준 내림차순 정렬
# 2. find-union 실행
# 3. union 시 s,e의 find가 같다면 (같은 집단이 된다면) 해당 시점의 가중치가 '최대 최소'

# 52%에서 컷.