# 가장 유효한 괄호의 길이
# (로 시작해서 )로 끝나며, 중간에 갯수가 안맞으면 안된다....


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        stk.append(-1)
        ans = 0
        for i in range(len(s)):
            if s[i] == '(' : 
                stk.append(i)
            else:
                stk.pop()
                if len(stk)==0 : 
                    stk.append(i)
                else:
                    ans = max(ans,i - stk[-1])
        return ans
                
                
                

            