import sys
input = sys.stdin.readline
import heapq

V,E,P = map(int,input().split())
edges = [list(map(int,input().split()))for _ in range(E)]
graph = [[] for _ in range(V+1)]
for line in edges:
  s,e,c = line
  graph[s].append((e,c))
  graph[e].append((s,c))
dist = [1e9] * (V+1)

# 다익스트라자
# 1 -> P -> V의 합과 1->V가 같은지 확인만 하면 됨

def dijk(start):
  dist[start] = 0
  queue = []
  heapq.heappush(queue,(0,start))
  while queue:
    total,cur = heapq.heappop(queue)
    for i in graph[cur]:
      next, cost = i
      if dist[next] > dist[cur] + cost:
        dist[next] = dist[cur] + cost
        heapq.heappush(queue,(total + cost, next))

dijk(1)
to_friend = dist[P]
to_end = dist[-1]

dist = [1e9] * (V+1)
dijk(P)

friend_to_end = dist[-1]

if to_friend + friend_to_end == to_end:
  print("SAVE HIM")
else:
  print("GOOD BYE")