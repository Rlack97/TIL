# 240220
# 간단한 큐 문제
# ping을 t에 받고, 해당 핑이 발생한 시점부터 t-3000에 받은 핑의 수 반환
# 큐에 핑을 넣은 후, 맨 앞의 값부터 t와의 차이가 3000 이상인지 검증한다.
# 이후 큐의 길이를 반환

from collections import deque


class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)


# 리트코드는 풀이보다 코드구조를 잘 모르겠다.
# 클래스 쓸일이 있기나 했겠냐고
