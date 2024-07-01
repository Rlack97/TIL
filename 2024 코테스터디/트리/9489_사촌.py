import sys
input = sys.stdin.readline

while True:
  n,k = map(int,input().split())
  if n == 0 and  k == 0:
    break

  numbers = list(map(int,input().split()))
  root = numbers[0]
  layer = [[numbers[0]],[[numbers[1]]]]
  wigs = [1]
  depth = 1
  count = 0
  rec_depth = 0
  for i in range(2,n):
    if numbers[i] == numbers[i-1]+1:
      layer[depth][count].append(numbers[i])
    else:
      if len(layer[depth]) == wigs[depth-1]:
        layer.append([[numbers[i]]])
        wigs.append(len(layer[depth][0]))
        depth += 1
        count = 0
      else:
        layer[depth].append([numbers[i]])
        count += 1
    
    if k == numbers[i]:
      rec_depth = depth

  answer = 0
  for d in layer[rec_depth]:
    if k in d:
      continue
    else:
      answer += len(d)

  print(layer)

  print(answer)

  # 연속된 수끼리 그룹 형성
  # 그룹이 부모 계층의 노드 수만큼 형성되면 다음 계층으로 진행 (최초는 1개)
  # 목표노드 k와 부모가 다르지만 계층이 같은 노드의 수 리턴
  # 예제는 맞았지만, index에러가 나기도 하고, answer 카운팅 시 같은 depth에서 부모 다른
  # 노드들의 수를 세기 때문에 틀림

  #--------------

  # 부모를 기록하면 됨

import sys
input = sys.stdin.readline

while True:
    n,k = map(int,input().rstrip().split())
    if n==0 and k == 0:
        break
    
    #루트노드의 부모 = -1
    a = [-1] + list(map(int,input().rstrip().split()))

    # 부모 기록 리스트
    parent = [0]*(n+1)
    parent[0] = -1

    target = 0
    idx = -1

    for i in range(1,n+1):
        # 타겟 노드 기록
        if a[i] == k:
            target = i

        # 연속되는 값이 아닐 때 idx 값 증가 (depth)
        if a[i] != a[i-1]+1:
            idx+=1
        
        # i번째 노드의 부모 = idx
        parent[i] = idx
    answer = 0
    for i in range(1,n+1):
        # 부모가 목표노드와 다르면서, 부모의 부모가 같은 노드들의 수
        if parent[i] != parent[target] and parent[parent[i]] == parent[parent[target]]:
            answer+=1
    print(answer)
