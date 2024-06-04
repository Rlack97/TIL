# 배열에서 k번째로 큰 수를 반환해라
# ... sort하고 list[-k] 하면 안되나?

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums를 heap으로 바꾼 뒤, 가장 작은수 len(nums)-k개 제거 후 남은 가장 작은 수
        heapq.heapify(nums)

        n = len(nums)
        cnt = 0
        while cnt < n-k:
            heapq.heappop(nums)
            cnt += 1

        return nums[0]
