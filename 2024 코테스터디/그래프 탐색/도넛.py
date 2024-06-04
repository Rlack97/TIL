# 도넛 = 간선이 n-1개인 순환그래프
# 막대 = 간선이 n-1개인 비순환그래프
# 8자 = 정점 2n+1, 간선 2n+2 
# 정점이 같은 도넛그래프 2개에서 정점 하나를 합침
# 모든 정점 한번씩 방문

# 별개의 정점 하나 생성 후 각 그래프에 하나씩 간선을 연결
# 이후의 간선정보를 통해 기존의 그래프 종류와 수를 파악해라.


# 나가는 간선이 2 이상, 들어오는 간선 0 = 새 정점
# 나가는 간선이 2, 들어오는 간선 2 이상 = 도넛그래프 수
# 나가는 간선 0, 들어오는 간선 1 (마지막 지점) = 막대그래프 수 
# 8자그래프 = 정점 나가는간선 - 나머지 그래프


def solution(edges):
    node_max = 0
    for s, e in edges:
        if s > node_max:
            node_max = s
        elif e > node_max:
            node_max = e
    out_line = [[] for _ in range(node_max+1)]
    in_line = [[] for _ in range(node_max+1)]

    for s,e in edges:
        out_line[s].append(e)
        in_line[e].append(s)
    
    new = 0
    answer = [0,0,0,0]

    for i,nodes in enumerate(out_line):
        if len(nodes) > 2:
            new = i
            answer[0] = new
        if len(nodes) >= 2:
            if len(in_line[i]) >= 2 and len(in_line[i]) >= 2:
              answer[3] += 1
            elif len(in_line[i]) == 0:
              new = i
              answer[0] = new
        if len(nodes) == 0 and len(in_line[i]) >= 1:
            answer[2] +=1
    print(new)            

    answer[1] = len(out_line[new]) - answer[2] -answer[3]
    return answer

