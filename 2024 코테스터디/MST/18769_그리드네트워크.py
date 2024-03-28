#0328
import sys
input = sys.stdin.readline
#A,B,C
# 인접한 서버끼리 연결하는 비용이 같은 경우는 없음.
def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])

    return parent[x]

  
T = int(input())
for _ in range(T):
  R,C = map(int,input().split())
  parent = [i for i in range(R*C+1)]
  edges = []

  Node = 1
  for j in range(R):
          R_list=list(map(int,input().split()))
          for k in range(len(R_list)):
              edges.append((R_list[k] , Node , Node+1))
              Node+=1
          Node+=1

  Node=1
  for j in range(R-1):
      C_list=list(map(int,input().split()))
      for k in range(len(C_list)):
          edges.append((C_list[k] , Node , Node+C) )
          Node+=1
  
  edges.sort() 
  total=0

  
  for value, a,b in edges:
      a = find(parent,a)
      b = find(parent,b)

      if a != b:
        if a < b:
            parent[b] = a

        else:
            parent[a] = b
        
        total += value
  
  print(total)