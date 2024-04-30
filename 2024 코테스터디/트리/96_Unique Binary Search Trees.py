# n이 주어졌을 때, 가능한 이진 탐색 트리의 갯수를 구하여라.
# queue나 뭐 그런거 생각했는데 DP???
# 이진 탐색 트리의 하위 트리는 전부 이진 탐색 트리

class Solution:
    def numTrees(self, n: int) -> int:
        # n이 19까지이므로
        dp = [0] * 20
        dp[0] = 1
        dp[1] = 1
        # 나머지 n의 경우의 수
        for i in range(2, n+1):
            for j in range(1, i+1):
                # j-1 (왼쪽 이진트리 수)
                # i-j (오른쪽 이진트리 수)
                dp[i] = dp[i] + dp[j-1] * dp[i-j]

        return dp[n]
