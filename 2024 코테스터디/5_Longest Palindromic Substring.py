
# 240207 주어진 문자열에서 가장 긴 회문찾기
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 주어진 문자열이 회문인지 판단하는 함수
        def check_Palindrome(left, right):
            # 문자열 내부 영역을 벗어나지 않으면서 동일한 값인지 검사
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # 마지막 증가분을 제외하고 index를 반환
            return left + 1, right - 1

        longest = ""

        for i in range(len(s)):
            # 회문 길이가 홀수인경우
            left, right = check_Palindrome(i, i)
            palindrome_length = right - left + 1
            if palindrome_length > len(longest):
                longest = s[left:right+1]

            # 회문 길이가 짝수인경우
            left, right = check_Palindrome(i, i+1)
            palindrome_length = right - left + 1
            if palindrome_length > len(longest):
                longest = s[left:right+1]

        return longest
