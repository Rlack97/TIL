import sys
from collections import deque

input = sys.stdin.readline


N = int(input())
students = []

for i in range(N):
    initial, X = map(str, input().split())
    X = int(X)
    students.append([initial,X])
    
queue = deque(students)

while len(queue) > 1:
    start = queue.popleft()
    
    # X-1번 패스를 진행
    for i in range(start[1]-1):
        pass_studuent = queue.popleft()
        queue.append(pass_studuent)
        
    # X번째 팀원과 팀을 구성
    team_up = queue.popleft()
    

# 한 명만 남았으므로 해당 학생의 이니셜 출력
print(queue[0][0])
    

    
    

