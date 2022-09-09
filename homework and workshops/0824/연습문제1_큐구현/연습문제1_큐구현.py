# 연습문제1_큐 구현 풀이
# 2022-08-24

N = 3
# 길이가 3개인 데이터에 대하여

q = [0]*3
rear = -1
front = -1
# 비어있는 큐 생성

# 삽입은 리어를 1씩 더해가며 해당 인덱스에 값을 넣는다
rear += 1
q[rear] = 1
# 1 삽입

rear += 1
q[rear] = 2
# 2 삽입

rear += 1
q[rear] = 3
# 3 삽입


# 출력은 프론트를 1씩 더해가며 해당 인덱스의 값을 추출한다
# 그 후 해당 인덱스를 비움
front += 1
print(q[front], end = ', ')
q[front] = 0

front += 1
print(q[front], end = ', ')
q[front] = 0

front += 1
print(q[front])
q[front] = 0