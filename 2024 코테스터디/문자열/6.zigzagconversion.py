#240221
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        legnth = len(s)
        board = [[0] * len(s) for _ in range(numRows)]
        x,y = 0,0
        zig = False
        if numRows == 1:
          return s        
        for word in s:
            board[x][y] = word

            # 내려갈 때
            if zig == False and x < numRows-1:
                x += 1
            # 맨 아래
            elif zig == False and x == numRows-1:
                zig = True
                x -= 1
                y += 1
            # 대각선 상승 시
            elif zig == True and 0< x <numRows -1:
                x-=1
                y+=1
            # 맨 위
            elif zig == True and x == 0:
                zig = False
                x += 1
        
        res = ""
        
        for b in board:
            res += ''.join([x for x in b if isinstance(x, str)])

        return res

            

# 런타임 지랄났네 ㅋㅋㅋㅋㅋ