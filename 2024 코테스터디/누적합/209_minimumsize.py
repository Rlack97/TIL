class Solution(object):
    def minSubArrayLen(self, target, nums):

        # 1. 시작 지점을 가리키는 포인터 left를 초기화한다.
        left = 0

        # 2. 배열의 최소 길이를 무한대로 설정한다.
        minLength = float('inf')

        # 3. 현재 부분 배열의 합을 나타내는 변수를 초기화한다.
        currentSum = 0

        # 4. nums 배열의 요소만큼 반복하는 for 문을 선언한다.
        # 반복마다 right 포인터 변수를 + 1만큼 이동한다.
        for right in range(len(nums)):
            # 5. 현재 합계에 right 포인터가 가리키고 있는 원소 값을 추가한다.
            currentSum += nums[right]

            # 6. 현재 합계가 목표값 이상인 동안 반복하는 while 문을 선언한다.
            while currentSum >= target:
                # 7. 최소 길이를 현재 최소 길이와 현재 부분 배열의 길이 중 작은 값으로 업데이트한다.
                minLength = min(minLength, right - left + 1)

                # 8. 부분 배열의 합에서 left 포인터가 가리키는 원소를 빼서 윈도우를 이동시킨다.
                currentSum -= nums[left]

                # 9. left 포인터 변수를 + 1 만큼 이동시킨다.
                left += 1

        # 10. for 문 이 종료되면 배열의 최소길이를 return 한다.
        # 만약 배열의 최소 길이가 할당되지 않았다면 0을 return 한다.
        return minLength if minLength != float('inf') else 0
