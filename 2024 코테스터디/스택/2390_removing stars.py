# 별이 포함된 문자열 s를 받는다
# 왼쪽에서 오른쪽으로 탐색 -> 별 왼쪽의 문자와 별을 같이 제거한다
# 남은 문자열 반환

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for code in s:
            if code == '*':
                stack.pop()
            else:
                stack.append(code)

        return ''.join(stack)
