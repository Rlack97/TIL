# 큐 풀이
#2022-08-04

# 데이터의 수 N

N = 10
global q, front, rear

# 큐 생성
def createqueue(N):
    q = [0]*N
    front = -1
    rear = -1

#큐 삽입
def enQueue(item):
    rear +=1
    q[rear] = item

#큐 출력
def deQueue():
    front += 1
    print(q[front])
    q[front] = 0

#큐 상태 확인
def isEmpty():
    if front == rear:
        return True
    else: False



def isFull():
    if rear == N-1:
        return True
    else: False
