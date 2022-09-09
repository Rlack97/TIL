# 우선순위 큐 풀이
#2022-08-04


# 데이터의 수 N


N = 10
# 큐 생성
def createqueue():
    global q, rear
    q = []
    rear = -1

# 우선도가 1인 경우가 가장 우선도가 높다고 가정
# 큐 삽입

def enQueue(priority, item):
    global q, rear
    if q == [] or q[-1][0] <= priority:
        q.append((priority, item))
        rear +=1
        # 큐가 비어 있거나, 맨 뒤의 요소의 우선순위가 자신과 같을 경우
        # 리스트의 맨 뒤에 삽입
    else:
        for i in range(0,rear+1): # 우선도에 맞는 곳에 삽입
            if q[i][0] > priority:
                q.insert(i,(priority,item))
                break
        
        rear += 1
    
    print(q)


#큐 출력
def deQueue():
    global q
    print(q.pop(0))



createqueue()

enQueue(3,1)
enQueue(2,2)
enQueue(3,4)
enQueue(1,3)

deQueue()
deQueue()
deQueue()
