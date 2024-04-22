# 가장 많은 물을 담을 수 있는 두 위치를 찾기

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 완전탐색 (시간초과)
        # start = 0
        # end = 1
        # max_amount = 0
        # while 0 <= start < end < len(height):
        #     vertical = min(height[start], height[end])
        #     horizontal = end-start
        #     water = vertical * horizontal
        #     max_amount = max(water, max_amount)
        #     if start+1 < end:
        #         start += 1
        #     elif start+1 == end:
        #         end += 1
        #         start = 0
        # return max_amount

        # 가장 넓은 가로값으로 시작해서 좁히기
        left = 0
        right = len(height)-1
        max_amount = 0

        while 0 <= left < right < len(height):
            vertical = min(height[left], height[right])
            horizontal = right-left
            water = vertical * horizontal
            max_amount = max(water, max_amount)

            # 두 포인터 중 높이가 작은 쪽을 땡긴다
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

        return max_amount
