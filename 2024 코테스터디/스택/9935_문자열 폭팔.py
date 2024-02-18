# 240206
# .strip()이나 .join 등의 메서드를 기억할 것.
# 대놓고 탐색하면 죽여버리겠다는 건 읽을 수 있었지만,
# stack을 쓰는 것을 빠르게 생각해내진 못했음.
import sys
input = sys.stdin.readline

Text = str(input().strip())
Bomb = str(input().strip())
long = len(Bomb)

stack = []


for t in Text:
    stack.append(t)
    if ''.join(stack[-long:]) == Bomb:
        for _ in range(long):
            stack.pop()


if stack == []:
    print('FRULA')

else:
    print(''.join(stack))
