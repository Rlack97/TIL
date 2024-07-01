class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        # 두 문자 길이끼리 곱한 이중리스트
        # dp[i][j] = word1의 i까지를 word2의 j까지로 바꾸기 위한 행동횟수
        dp = [[0]*(n+1) for _ in range(m+1)]

        # 맨 첫 줄 기본값 입력
        for i in range(m+1):
            dp[i][0] = i

        for i in range(n+1):
            dp[0][i] = i

        # 이중dp리스트를 순회하면서
        for i in range(1, m+1):
            for j in range(1, n+1):

                # 두 단어의 맨 뒷글자가 같을경우
                # 그 글자를 제외한 단어끼리의 행동횟수를 가져온다
                if word2[i-1] == word1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 다를 경우
                    # 왼쪽, 위쪽, 대각선의 값 중 가장 작은 값 + 1
                    # 왼쪽: word2에서 끝글자 제외하고 만드는데 쓴 횟수 (한글자 더하기)
                    # 위쪽: word2 + 추가 글자 만드는데 쓴 횟수 (한글자 빼기)
                    # 대각선 : 끝 글자 제외하고 같게 만드는데 쓰는 횟수 (한글자 바꾸기)
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        # dp[n][m] 값을 리턴한다.
        return dp[-1][-1]
