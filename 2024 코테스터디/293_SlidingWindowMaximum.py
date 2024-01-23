# 리트코드 239번
# 슬라이딩 윈도우를 옮기면서 내부의 최댓값을 max로 추출
# 시간복잡도 O(k*n)
# def maxSlidingWindow(self, nums, k):
#     r=[]
#     for i in range(len(nums) -k +1):
#         r.append(max(nums[i:i+k]))
#     return r

# 큐를 통한 최적화
class Solution:
    def maxSlidingWindow(self, nums, k):
        from collections import deque
        q = deque() # 인덱스 기록용
        result = [] # 정답 반환용

        for i, cur in enumerate(nums):

            # 큐 안에 값이 있고 q[-1]을 인덱스로 가지는 값이 i, 그러니까 윈도우에 추가될 새로운 값보다 작을 때
            # 큐의 맨 오른쪽을 pop으로 계속 제거해 줌.
            # 만약 더 작은 값이 들어오면 기록해 두고, 아래에서 popleft로 빠지면 자연스럽게 그 녀석이 최댓값이 됨.
            while q and nums[q[-1]] <= cur: 
                q.pop()

            # 큐에 값의 위치를 기록 (즉 q[0]은 최댓값의 위치를 나타낸다.)
            q.append(i)
            
            # q[0], 즉 최댓값의 위치가 윈도우의 범위 밖이라면 popleft로 버림.
            if q[0] == i - k:
                q.popleft()

            # i >= k-1, 즉 윈도우가 가득 찼을 때
            # q[0] 위치의 값 (최댓값)을 정답 리스트에 기록.
            if i >= k - 1:
                result.append(nums[q[0]])

        return result