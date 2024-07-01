# without using the library's sort function.
# 0 -> 1-> 2 순서대로, 같은 색끼리 인접하도록 '내부정렬'함
# == 추가 할당이나 메모리를 사용하지 않는다는 뜻
# 버블 정렬O(n^2) 이나 삽입정렬O(n)등이 적합
class Solution:
    def sortColors(self, nums: List[int]) -> None:
      for end in range(1, len(nums)):
          # 배열의 각 위치에서 맨 앞까지의 범위 내에서
          for i in range(end, 0, -1):
              # 값이 역순이면 자리를 바꿔준다
              # 앞 부분은 정렬되어 있으므로 추가되는 값만 배치시키면 되기 때문에
              # range의 끝부분부터 거꾸로 비교해 내려간다
              if nums[i - 1] > nums[i]:
                  nums[i - 1], nums[i] = nums[i], nums[i - 1]   

        