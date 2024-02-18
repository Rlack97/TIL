# 자신을 제외한 리스트 내부 값들의 곱을 기록한 리스트를 반환
# 다 곱해둔 후 자기 자신으로 나누면 됨
# 0이 한개일 경우 해당 수만 반환값이 0이 아니며, 0이 두 개 이상이면 모든 값이 0
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        flag = 0
        # 0 갯수 체크. 곱해둘 때 0은 빼놓고 계산한다.
        for num in nums:
            if num != 0:
                total = total * num
            else:
                flag += 1
                continue

        answer = [total] * len(nums)
        if flag >= 2:
            answer = [0] * len(nums)
        elif flag == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    answer[i] = 0
        else:
            for i in range(len(nums)):
                answer[i] = answer[i] // nums[i]
        return answer
