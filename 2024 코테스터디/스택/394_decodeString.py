class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        strs = ''
        numStack = []
        strStack = []
        for ss in s:
            # 여는 괄호 만나면 숫자와 문자를 스택에 각각 쌓고 초기화
            if ss == '[':
                numStack.append(num)
                strStack.append(strs)
                num = 0
                strs = ''
                continue
            if ss== ']':
                strs = strStack.pop() + (strs * numStack.pop())  
                continue
                
            # 문자와 숫자 구분해서 누적
            # 숫자의 경우 [를 만나면 초기화되므로 
            # 입력값이 2개 이상일 경우 자릿수가 큰 수이므로 
            # 자릿수를 증가시킨 후 저장
            if ss.isalpha():
                strs += ss
            else:
                num = (num)*10 + int(ss)
        
        return strs