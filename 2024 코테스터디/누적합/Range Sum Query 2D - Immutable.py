# 1차원 누적합
# 리스트에 누적해서 합을 구해 저장해둠.
# 원하는 범위 n~m이 있다면 m까지의 누적합 - (n-1)까지의 누적합으로 구할 수 있음

# 2차원 리스트가 된다면?
# [a,b] 부터 [c,d] 까지
# [c,d] 까지의 누적합 - ([a-1,d]까지의 누적합 + [c,b-1]까지의 누적합) + [a-1,b-1]까지의 누적합 (겹치는 부분)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.NumMatrix = [[0]*(n+1) for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                self.NumMatrix[i][j] = self.NumMatrix[i][j-1] + self.NumMatrix[i -
                                                                               1][j] - self.NumMatrix[i-1][j-1] + matrix[i - 1][j - 1]
                # 이전까지의 누적합들 + 현재 위치 값

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.NumMatrix[row2+1][col2+1] - self.NumMatrix[row1][col2+1] - self.NumMatrix[row2+1][col1] + self.NumMatrix[row1][col1]

        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)
