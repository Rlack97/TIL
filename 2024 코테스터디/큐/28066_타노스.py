from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

que = deque(range(1, N + 1))  # 1부터 N까지의 청설모 큐 생성

while len(que) > 1:
    kp = que.popleft()  # 첫 번째 청설모 저장
    itercnt = min(K-1, len(que))  # K번째 청설모까지 제거
    for _ in range(itercnt):
        que.popleft()  # K-1마리 청설모 제거
    que.append(kp)  # 첫 번째 청설모 다시 추가

print(que[0])   # 마지막으로 남은 청설모 반환
