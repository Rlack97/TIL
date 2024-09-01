import sys
input = sys.stdin.readline

K, N, F = map(int, input().split())
friends = [list(map(int, input().split())) for _ in range(F)]

# 친구 관계를 저장할 인접 리스트
students = [[] for _ in range(N+1)]
for a, b in friends:
    students[a].append(b)
    students[b].append(a)

# 학생들을 정렬하여 사전 순으로 탐색할 수 있게 함
for i in range(1, N+1):
    students[i].sort()

# 그룹 내의 모든 학생들이 서로 친구인지 확인
def is_valid_group(group):
    for i in range(len(group)):
        for j in range(i+1, len(group)):
            if group[j] not in students[group[i]]:
                return False
    return True

# DFS로 백트래킹
def find_group(group, start):
    
    # 그룹 사이즈가 K가 되면 그룹 조건에 맞는지 검증
    if len(group) == K:
        if is_valid_group(group):
            return group
        return None
    
    # 친구 그룹에 해당 숫자 학생 추가
    for i in range(start, N+1):
        group.append(i)
        # 방금 추가한 학생을 제외하고, 나머지 학생들이 그 학생의 친구인지 확인
        if all(i in students[friend] for friend in group[:-1]):
            # dfs 재귀, 
            result = find_group(group, i + 1)
            # result가 존재 = 유효한 그룹이 반환됨
            if result:
                return result
        #추가했던 학생 제거
        group.pop()
    
    return None

result = find_group([], 1)

if result:
    for student in result:
        print(student)
else:
    print(-1)