# 연습문제1-스택구현 풀이
# 2022-08-12

size = 10
stack = [0] * size
top = -1
# 스택의 기본 구조 형성


top += 1
stack[top] = 1
# push(1)

top += 1
stack[top] = 10
# push(10)

top += 1
stack[top] = 100
# push(100)

top -= 1
temp = stack[top+1]
print(temp)
# pop()

top -= 1
temp = stack[top+1]
print(temp)
# pop()

top -= 1
temp = stack[top+1]
print(temp)
# pop()

stack2 = []
stack2.append(1)
stack2.append(10)
stack2.append(100)
print(stack2.pop())
print(stack2.pop())
print(stack2.pop())
#동일한 과정
